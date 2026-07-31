# Lab 10 - Feature Implementation Status

## Purpose
Use this file to prove that your prototype implementation is connected to `system-requirements.md`.

| Req ID | Required Functionality | Prototype Screen/Module | Current Status | Evidence | Next Fix Needed |
|---|---|---|---|---|---|
| FR-01 | Homepage or landing screen | Homepage / gallery entry screen | Completed | `prototype/wireframe/homepage.html` | Continue replacing any remaining placeholder/Pixiv-style content with IceCream branding. |
| FR-02 | User input or data submission | Upload form and comment input | Completed | `prototype/wireframe/Upload.html`, `prototype/wireframe/Artwork.html` comment field | Add ownership confirmation, privacy warning, required validation, and safer free-text handling. |
| FR-03 | Data storage or simulated storage | Mock CSV data records | Completed | `data/Users_records.csv`, `data/artworks_records.csv`, `data/comments_records.csv` | Connect screens to simulated records or document how CSV data maps to UI. |
| FR-04 | View records or information list | Artwork gallery/feed | Completed | `prototype/wireframe/homepage.html`; artwork cards with thumbnails and creator info | Replace placeholder images with approved/credited artwork. |
| FR-05 | Search, filter, or category function | Header search and gallery/tag browsing | In Progress | Search bars in `homepage.html`, `Artwork.html`, `Upload.html`, `login.html`, `Sign-Up.html`, `User-Profile.html`, `User-Dashboard.html` | Implement real filtering behavior and duplicate/invalid tag prevention. |
| FR-06 | Detail view for each record | Artwork detail page with comment area | Completed | `prototype/wireframe/Artwork.html` | Add structured critique category selection and connect comments to mock comment records. |
| FR-07 | Status or progress tracking | Artwork/comment status records and status labels | In Progress | `data/artworks_records.csv`, `data/comments_records.csv`; status values `Published`, `Underchecking`, `Withdrawn` | Show status badges clearly in UI and explain status meanings to users. |
| FR-08 | Admin or manager function | Moderator/admin function | Not Started | `docs/technical-architecture.md`, `docs/security-risk-check.md`, `docs/risk-register.md` describe planned moderator function | Create or finalize a moderator dashboard screen with role-separated actions. |
| FR-09 | Validation and error prevention | Upload form, sign-up/login forms, comment input | Needs Fix | `prototype/wireframe/Upload.html`, `Sign-Up.html`, `login.html`, `Artwork.html`; `docs/security-risk-check.md` | Enforce required fields, file type/size checks, minimum critique length, sanitization, and validation messages. |
| FR-10 | Confirmation or feedback message | Upload/comment confirmation behavior | Not Started | Requirement documented in `docs/system-requirements.md`; no clear toast/confirmation found in current HTML | Add success/error messages after upload, comment submission, and moderation/status actions. |
| FR-11 | Dashboard or summary view | Creator analytics/dashboard and profile | Working Draft | `prototype/wireframe/User-Dashboard.html`, `prototype/wireframe/User-Profile.html` | Keep analytics creator-only and clarify chart/metric meanings. |
| FR-12 | UI consistency | Shared IceCream header and common visual style | In Progress | Shared header appears across current wireframe files; `docs/implementation-plan.md` | Finish standardizing labels, branding, spacing, and button styles across all pages. |
| FR-13 | Mobile-friendly/responsive design | Responsive gallery/profile/detail layouts | In Progress | `homepage.html` uses responsive artwork grid; `User-Profile.html` uses responsive artwork grid; `Artwork.html` uses Tailwind responsive grid classes | Test and capture screenshots on desktop/mobile widths. |
| FR-14 | Privacy and responsible data handling | Alias-based user data, anonymized mock records, privacy/security docs | In Progress | `data/Users_records.csv` uses `ANONYMIZED`; `docs/privacy-and-data-protection.md`; `docs/updated-requirements-note.md` | Remove or justify unnecessary sign-up fields such as gender and date of birth; keep raw IDs/passwords private. |
| FR-15 | Final prototype traceability | Requirement, user story, feature, and Lab 09/10 documentation | Working Draft | `docs/feature-requirement-mapping.md`, `docs/implementation-plan.md`, `docs/updated-requirements-note.md`, this file | Add screenshots, demo links, and commit/issue IDs when available. |

## Summary
- Features working today: FR-01, FR-02, FR-03, FR-04, FR-06, FR-11, FR-15
- Features partially working: FR-05, FR-07, FR-12, FR-13
- Features not yet started: FR-08, FR-10
- Features requiring instructor feedback: FR-09, FR-14, and the Lab 09 requirement clarifications for FR-02, FR-08, FR-09, FR-11, and FR-14
