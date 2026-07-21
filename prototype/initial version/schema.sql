-- ==========================================
-- IceCream Supabase Database Schema
-- Run in: Supabase → SQL Editor → Paste All → Run
-- ==========================================

-- ==========================================
-- 1. 用户资料表 (profiles) — 连接 Supabase Auth
-- ==========================================
CREATE TABLE profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username VARCHAR(50) UNIQUE NOT NULL,
    avatar_url VARCHAR(255),
    role VARCHAR(20) DEFAULT 'user' NOT NULL,      -- 'user', 'admin', 'moderator'
    status VARCHAR(20) DEFAULT 'active' NOT NULL,   -- 'active', 'banned'
    bio TEXT DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    deleted_at TIMESTAMPTZ
);

CREATE INDEX idx_profiles_status ON profiles(status) WHERE deleted_at IS NULL;
CREATE INDEX idx_profiles_username ON profiles(username);

-- 自动创建 profile（用户注册时触发）
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, username, avatar_url)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'username', split_part(NEW.email, '@', 1)),
    NEW.raw_user_meta_data->>'avatar_url'
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION handle_new_user();


-- ==========================================
-- 2. 作品表 (artworks)
-- ==========================================
CREATE TABLE artworks (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    image_urls JSONB NOT NULL,                      -- 多图: ["url1","url2"]
    view_count INT DEFAULT 0 NOT NULL,
    like_count INT DEFAULT 0 NOT NULL,
    comment_count INT DEFAULT 0 NOT NULL,
    sanity_level SMALLINT DEFAULT 0 NOT NULL,       -- 0:全年龄, 1:R-15, 2:R-18
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    deleted_at TIMESTAMPTZ,

    CONSTRAINT fk_artworks_user FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE
);

CREATE INDEX idx_artworks_user ON artworks(user_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_artworks_latest ON artworks(created_at DESC) WHERE deleted_at IS NULL;
CREATE INDEX idx_artworks_ranking ON artworks(like_count DESC, view_count DESC);
CREATE INDEX idx_artworks_sanity ON artworks(sanity_level);


-- ==========================================
-- 3. 标签表 (tags)
-- ==========================================
CREATE TABLE tags (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL
);


-- ==========================================
-- 4. 作品-标签关联表 (artwork_tags)
-- ==========================================
CREATE TABLE artwork_tags (
    artwork_id BIGINT NOT NULL,
    tag_id BIGINT NOT NULL,

    PRIMARY KEY (artwork_id, tag_id),
    CONSTRAINT fk_bridge_artwork FOREIGN KEY (artwork_id) REFERENCES artworks(id) ON DELETE CASCADE,
    CONSTRAINT fk_bridge_tag FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

CREATE INDEX idx_artwork_tags_tag_id ON artwork_tags(tag_id);


-- ==========================================
-- 5. 收藏表 (bookmarks)
-- ==========================================
CREATE TABLE bookmarks (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    artwork_id BIGINT NOT NULL,
    is_private BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,

    CONSTRAINT uk_user_artwork_bookmark UNIQUE (user_id, artwork_id),
    CONSTRAINT fk_bookmarks_user FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE CASCADE,
    CONSTRAINT fk_bookmarks_artwork FOREIGN KEY (artwork_id) REFERENCES artworks(id) ON DELETE CASCADE
);

CREATE INDEX idx_bookmarks_user ON bookmarks(user_id, is_private);


-- ==========================================
-- 6. 评论表 (comments)
-- ==========================================
CREATE TABLE comments (
    id BIGSERIAL PRIMARY KEY,
    artwork_id BIGINT NOT NULL,
    user_id UUID,                                   -- NULL = 用户已注销
    parent_id BIGINT,                               -- 楼中楼回复
    content TEXT NOT NULL,
    images TEXT[] DEFAULT '{}',                     -- 可选评论配图
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    deleted_at TIMESTAMPTZ,

    CONSTRAINT fk_comments_artwork FOREIGN KEY (artwork_id) REFERENCES artworks(id) ON DELETE CASCADE,
    CONSTRAINT fk_comments_user FOREIGN KEY (user_id) REFERENCES profiles(id) ON DELETE SET NULL,
    CONSTRAINT fk_comments_parent FOREIGN KEY (parent_id) REFERENCES comments(id) ON DELETE CASCADE
);

CREATE INDEX idx_comments_artwork ON comments(artwork_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_comments_parent ON comments(parent_id) WHERE parent_id IS NOT NULL;


-- ==========================================
-- 7. 关注表 (follows)
-- ==========================================
CREATE TABLE follows (
    follower_id UUID NOT NULL,
    following_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,

    PRIMARY KEY (follower_id, following_id),
    CONSTRAINT fk_follows_follower FOREIGN KEY (follower_id) REFERENCES profiles(id) ON DELETE CASCADE,
    CONSTRAINT fk_follows_following FOREIGN KEY (following_id) REFERENCES profiles(id) ON DELETE CASCADE
);

CREATE INDEX idx_follows_following_id ON follows(following_id);


-- ==========================================
-- 8. Row Level Security (RLS)
-- ==========================================
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE artworks ENABLE ROW LEVEL SECURITY;
ALTER TABLE tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE artwork_tags ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookmarks ENABLE ROW LEVEL SECURITY;
ALTER TABLE comments ENABLE ROW LEVEL SECURITY;
ALTER TABLE follows ENABLE ROW LEVEL SECURITY;

-- profiles
CREATE POLICY "Profiles readable by everyone" ON profiles FOR SELECT USING (true);
CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);
CREATE POLICY "Users can insert own profile" ON profiles FOR INSERT WITH CHECK (auth.uid() = id);

-- artworks
CREATE POLICY "Artworks readable by everyone" ON artworks FOR SELECT USING (true);
CREATE POLICY "Users can insert own artworks" ON artworks FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own artworks" ON artworks FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own artworks" ON artworks FOR DELETE USING (auth.uid() = user_id);

-- tags
CREATE POLICY "Tags readable by everyone" ON tags FOR SELECT USING (true);
CREATE POLICY "Admins can manage tags" ON tags FOR ALL USING (EXISTS (SELECT 1 FROM profiles WHERE id = auth.uid() AND role = 'admin'));

-- artwork_tags
CREATE POLICY "Artwork-tags readable by everyone" ON artwork_tags FOR SELECT USING (true);
CREATE POLICY "Owners can manage artwork tags" ON artwork_tags FOR INSERT WITH CHECK (
  EXISTS (SELECT 1 FROM artworks WHERE id = artwork_id AND user_id = auth.uid())
);
CREATE POLICY "Owners can delete artwork tags" ON artwork_tags FOR DELETE USING (
  EXISTS (SELECT 1 FROM artworks WHERE id = artwork_id AND user_id = auth.uid())
);

-- bookmarks
CREATE POLICY "Bookmarks readable by everyone" ON bookmarks FOR SELECT USING (is_private = FALSE OR user_id = auth.uid());
CREATE POLICY "Users can manage own bookmarks" ON bookmarks FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can delete own bookmarks" ON bookmarks FOR DELETE USING (auth.uid() = user_id);

-- comments
CREATE POLICY "Comments readable by everyone" ON comments FOR SELECT USING (true);
CREATE POLICY "Auth users can insert comments" ON comments FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can delete own comments" ON comments FOR DELETE USING (auth.uid() = user_id);

-- follows
CREATE POLICY "Follows readable by everyone" ON follows FOR SELECT USING (true);
CREATE POLICY "Auth users can follow" ON follows FOR INSERT WITH CHECK (auth.uid() = follower_id);
CREATE POLICY "Users can unfollow" ON follows FOR DELETE USING (auth.uid() = follower_id);

-- ==========================================
-- RPC Functions (bypass RLS for counts)
-- ==========================================
CREATE OR REPLACE FUNCTION increment_view(artwork_id BIGINT)
RETURNS void AS $$
BEGIN
  UPDATE artworks SET view_count = view_count + 1 WHERE id = artwork_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE OR REPLACE FUNCTION toggle_like(artwork_id BIGINT, increment INT)
RETURNS void AS $$
BEGIN
  UPDATE artworks SET like_count = like_count + increment WHERE id = artwork_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
