# Lab 04 - User Stories and Acceptance Criteria

## User Story Format

> As a **[user role]**, I want to **[goal/action]**, so that **[benefit/value]**.

---

# User Stories

| Story ID | Interview | Role                         | User Story                                                                                                                                                                                | Related Requirement                               | Priority | Acceptance Criteria                                                                                                                                                                                    | Demo Evidence            |
| -------- |-----------|------------------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |---------------------------------------------------| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| US-01    | R1        | University Anime Illustrator | As a university anime illustrator, I want to receive constructive critiques instead of only likes, so that I can improve my coloring and lighting skills.                                 | **F-04 – Comment System**                         | Must     | Given my artwork is published, when another user submits structured feedback, then the critique is displayed under my artwork.                                                                         | Critique page            |
| US-02    | R2        | Hobby Character Designer     | As a hobby character designer, I want to find artists who are willing to provide meaningful feedback, so that I can improve my character designs.                                         | **F-04 – Comment System**                         | Must     | Given I upload artwork and request critique, when other artists review it, then I receive detailed feedback instead of simple reactions.                                                               | Critique page            |
| US-03    | R3        | Student Digital Illustrator  | As a student digital illustrator, I want to browse artworks by style and skill level, so that I spend less time searching for relevant artwork.                                           | **F-03 – Style & Fandom Categorized Feed**        | Must     | Given I select categories or tags, when I browse the gallery, then only matching artworks are displayed.                                                                                               | Gallery filter demo      |
| US-04    | R4        | VTuber Fan Artist            | As a VTuber fan artist, I want my artwork to remain discoverable within my fandom community, so that it doesn't disappear quickly in general social media feeds.                          | **F-03 – Style & Fandom Categorized Feed**        | Must     | Given I tag my artwork as "VTuber", when users browse that fandom, then my artwork appears in the filtered gallery.                                                                                    | Tagged gallery           |
| US-05    | R5        | Comic Artist                 | As a comic artist, I want to upload my comic as a multi-page project and specify that I want storytelling feedback, so that readers can view the comic in order and give useful critiques. | **F-02 – Multi-page Upload & Critique Spec Form** | Must     | Given I upload multiple comic pages and select "Storytelling" as the critique focus, when users open the project, then the pages appear sequentially and reviewers can provide storytelling critiques. | Comic upload demo        |
| US-06    | R6        | First-Year Art Student       | As a first-year art student, I want to request structured critiques from experienced artists, so that I can improve my drawing skills faster.                                             | **F-04 – Comment System**                         | Must     | Given I publish my artwork, when experienced users submit categorized critiques, then I can review them easily.                                                                                        | Critique interface       |
| US-07    | R7        | Freelance Illustrator        | As a freelance illustrator, I want a professional portfolio that showcases my artworks in one place, so that I no longer need to manage multiple platforms.                               | **F-01 – Landing & Navigation Portal**            | Must     | Given I upload my portfolio, when visitors open my profile, then all artworks are presented in an organized portfolio.                                                                                 | Portfolio page           |
| US-08    | R8        | Touhou Enthusiast            | As a Touhou enthusiast, I want to search artworks and artists by fandom, so that I can easily find other Touhou fans and discuss our artwork together.                                    | **F-03 – Style & Fandom Categorized Feed**        | Must     | Given I search for the "Touhou" fandom, when matching artists and artworks exist, then they are displayed together.                                                                                    | Fandom search demo       |
| US-09    | R9        | Community Member             | As a casual art creator, I want a personal artwork album feature so that I can easily organize my old works. I also want to know how many people like my work and follow my channel because of the work | F-05 Creator Analytics & Critique Karma           | Could    | **Given** I view my profile page, **when** there is a dashboard , **then** I can know which work get most likes and total reactions to my works| a dashboard screenshot   |
| US-10    | R10       | Competitive Digital Artist              | As a Digital Artist, I want to edit my profile and artist information so that others can learn about me and my artwork. | **F-01 – Landing & Navigation Portal**            | Should   | **Given** I edit my profile, **when** I save my changes, **then** the updated information appears on my profile page.                 | Profile editing demo       |

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
