# Lab 04 - User Stories and Acceptance Criteria

## User Story Format

> As a **[user role]**, I want to **[goal/action]**, so that **[benefit/value]**.

---

# User Stories

| Story ID | Role             | User Story                                                                                                                       | Related Requirement             | Priority | Acceptance Criteria                                                                                                                   | Demo Evidence              |
| -------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| US-01    | Student Artist   | As a student artist, I want to upload my artwork to my personal portfolio so that I can showcase my work in one organized place. I also want feedback on quality of my painting | FR-01 Portfolio Management      | Must     | **Given** I am logged in, **when** I upload an artwork with a title and image, **then** it appears in my portfolio gallery.           | Portfolio page and Comment system  |
| US-02    | Digital Artist   | As a digital artist, I want to tag my artwork by style and category so that other artists can easily discover it.                | FR-02 Artwork Categories & Tags | Must     | **Given** I upload artwork, **when** I assign tags (e.g., Anime, Concept Art), **then** the artwork appears under those categories.   | Upload page Tagging System    |
| US-03    | Art Hobbyist     | As an art hobbyist, I want to browse artworks by category and tags so that I can quickly find artwork matching my interests.     | FR-03 Artwork Discovery         | Must     | **Given** I select a category or tag, **when** I search, **then** only matching artworks are displayed.                               | Gallery filtering demo     |
| US-04    | Student Artist   | As a student artist, I want to receive constructive comments on my artwork so that I can improve my drawing skills.              | FR-04 Comment System            | Must     | **Given** my artwork is published, **when** another user comments, **then** the comment appears beneath my artwork.                   | Artwork comments demo      |
| US-05    | Artist           | As an artist, I want to organize my artworks in my own gallery so that my portfolio remains easy to browse.                      | FR-05 Portfolio Gallery         | Must     | **Given** I have uploaded several artworks, **when** I visit my profile, **then** all artworks are displayed in an organized gallery. | Profile gallery screenshot |
| US-06    | Art Enthusiast   | As an art enthusiast, I want to follow artists whose work I enjoy so that I can easily see their future artwork.                 | FR-06 Follow Artists            | Should   | **Given** I visit an artist's profile, **when** I click Follow, **then** the artist is added to my following list.                    | Follow feature demo        |
| US-07    | Student Artist   | As a student artist, I want to search for artists with similar interests so that I can connect and collaborate with them.        | FR-07 Artist Search             | Should   | **Given** I search by tags or interests, **when** matching artists exist, **then** their profiles are displayed.                      | Artist search screenshot   |
| US-08    | Comic Artist     | As a comic artist, I want to upload multiple pages for a project so that readers can view my comics in order.                    | FR-08 Multi-image Upload        | Could    | **Given** I upload multiple images, **when** I publish the project, **then** readers can browse the pages sequentially.               | Comic upload demo          |
| US-09    | Community Member | As a community member, I want to report inappropriate content so that the community remains safe and welcoming.                  | FR-09 Report Content            | Could    | **Given** I view an artwork, **when** I click Report, **then** the report is submitted successfully.                                  | Report dialog screenshot   |
| US-10    | Registered User  | As a registered user, I want to edit my profile and artist information so that others can learn about me and my artwork.         | FR-10 User Profile              | Should   | **Given** I edit my profile, **when** I save my changes, **then** the updated information appears on my profile page.                 | Profile editing demo       |

---

# Acceptance Criteria Checklist

A good acceptance criterion should be:

* ✅ Testable
* ✅ Observable in the final prototype
* ✅ Connected to a functional requirement
* ✅ Connected to interview evidence
* ✅ Clear and specific

---

# Rejected / Future User Stories

| Story ID | Reason for Postponing                     | Future Condition                                                                 |
| -------- | ----------------------------------------- | -------------------------------------------------------------------------------- |
| FUT-01   | Integrated payment system for commissions | Implement after validating demand from a larger artist community                 |
| FUT-02   | Commission marketplace                    | Add after community growth and stable user activity                              |
| FUT-03   | Mobile application                        | Validate whether users prefer a dedicated mobile app or responsive website first |
| FUT-04   | AI artwork recommendation                 | Consider after a sufficiently large artwork database exists                      |

---

# Traceability to Customer Discovery

| Interview Finding                              | Related User Stories |
| ---------------------------------------------- | -------------------- |
| Artwork gets buried in existing platforms      | US-01, US-05         |
| Artists want structured feedback               | US-04                |
| Artists struggle to discover similar artwork   | US-02, US-03         |
| Communities are fragmented                     | US-06, US-07         |
| Artists need organized portfolios              | US-01, US-05         |
| Payment features are not an immediate priority | FUT-01, FUT-02       |
