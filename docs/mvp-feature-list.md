# Lab 04 - MVP Feature List

## MVP Decision Rule
The MVP should include the smallest set of features that can demonstrate the core problem-solution fit by the end of the semester. For **IceCream**, this means enabling artists to post illustrations/comics and receive high-quality structured feedback from their peers without posts getting lost.

## MoSCoW Prioritization

| Feature ID | Feature Name                                 | Problem Solved | Related User Story | Priority (Must/Should/Could/Won't) | Technical Complexity (1-5) | User Value (1-5) | Evidence Strength (1-5) | Include in Final Prototype? |
|---|----------------------------------------------|---|---|---|---:|---:|---:|---|
| **F01** | **Landing & Navigation Portal**              | Campus artists lack a dedicated showcase entrance; confusing navigation. | US-01 | Must | 2 | 5 | 5 | Yes |
| **F02** | **Multi-page Upload & Critique Spec Form**   | Standard uploads don't support multi-page comic layouts; artists can't ask for specific critique focuses. | US-02 | Must | 3 | 5 | 5 | Yes |
| **F03** | **Style & Fandom Categorized Feed**          | Works get buried instantly in chat channels; hard to find specific anime/comic niches. | US-03 | Must | 2 | 5 | 5 | Yes |
| **F04** | **Comment System**                           | Standard comments result in shallow emojis/stickers instead of anatomy or lighting help. | US-04 | Must | 3 | 5 | 5 | Yes |
| **F05** | **Creator Analytics & Critique Karma**       | Slow learning loops; lack of incentive to write high-quality critiques for peers. | US-05 | Should | 3 | 4 | 4 | Yes |
| **F06** | **Moderator Admin Dashboard**                | Off-topic spams, non-constructive critiques, and inappropriate posts. | US-06 | Should | 3 | 3 | 3 | Yes |
| **F07** | **Collaborative Contests & Fandom Events**   | Difficult to find local illustration partners or team project collaborators. | US-07 | Could | 4 | 4 | 3 | No |
| **F08** | **Commission Matching / Transaction System** | Finding commercial clients and payment security issues. | US-08 | Won't | 5 | 3 | 2 | No |

---

## Must-Have Features

### F01: Landing & Navigation Portal
- **Description**: An initial landing page showing featured student artwork, popular styles, and direct CTA paths to browse the gallery or upload portfolios.
- **Why**: Essential first impression that establishes a dedicated, professional "campus art community" feel.

### F02: Multi-page Upload & Critique Spec Form
- **Description**: Form that supports uploading single illustrations or multi-page layouts (essential for manga/comic storyboards). Creators specify which critique areas they want help with (e.g., Anatomy, Coloring, Storytelling).
- **Why**: Solves the issue where comic artists had nowhere to share full sequences, and helps beginners explicitly ask for targeted advice.

### F03: Style & Fandom Categorized Feed
- **Description**: A grid gallery that allows users to search titles/tags and filter by style (Anime, Comic/Manga, Concept Art) and fandom (Touhou, VTuber, Original).
- **Why**: 8/10 customer interviewees wanted categorized galleries to prevent their art from getting buried in generic feeds.

### F04: Comment System
- **Description**: Comments section that separates standard chat from structured critiques. Reviewers select a category (Anatomy, Coloring, Storytelling) and write reviews, with an enforced minimum character limit.
- **Why**: Resolves the biggest paint point where artists receive nothing but superficial "nice art" comments or stickers.

---

## Should-Have Features

### F05: Creator Analytics & Critique Karma
- **Description**: A dashboard showing views, likes, and structured critique tallies, alongside a "Karma Score" that increases when the user leaves helpful critiques on other artists' posts.
- **Why**: Encourages community feedback reciprocity (giving critiques to receive them) and tracks learning progress.

### F06: Moderator Admin Dashboard
- **Description**: A panel allowing appointed Art Club leaders to review reported uploads, delete spam, and pin top critiques.
- **Why**: Keeps the community constructive, safe, and focused on art learning.

---

## Could-Have / Future Features

### F07: Collaborative Contests & Fandom Events
- **Description**: A system for organizing virtual art jams, fandom drawing challenges, and recruitment cards for campus collaboration (e.g., game dev teams).
- **Why**: While valuable for networking, the core portfolio-critique loop is more urgent for initial validation.

---

## Not in MVP (Won't-Have)

### F08: Commission Matching & Transaction System
- **Description**: Payment gateways, escrow, and commercial contract templates.
- **Why**: Customer discovery revealed that local artists prioritize community feedback and local visibility over instant monetization. A third-party payment system is highly complex and introduces significant cybersecurity/privacy overhead that is not feasible for Lab 04.
