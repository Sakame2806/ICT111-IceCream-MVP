# Lab 10 - Implementation Plan

## 1. Project Information
- Group name: IceCream
- Project title: ICT111-IceCream-MVP
- Repository link: https://github.com/Sakame2806/ICT111-IceCream-MVP
- Selected platform/tools: HTML, CSS, JavaScript, Tailwind CSS CDN, planned Vue.js 3, planned Firebase Auth and Firestore
- Backend status: Simulated backend for Sprint 1, with possible Firebase implementation later

## 2. Prototype Scope for Sprint 1
List the features your group will implement in Lab 10.

| Feature | Requirement ID | User Story ID | Screen/Module                                               | Sprint 1 Status |
|---|---|---|-------------------------------------------------------------|---|
| Homepage / landing and gallery screen | FR-01, FR-05, FR-13 | US-03, US-07 | `prototype/wireframe/homepage.html`                         | In Progress |
| Account login screen | FR-15 | US-10 | `prototype/wireframe/login.html`                            | In Progress |
| Account sign-up screen | FR-15 | US-10 | `prototype/wireframe/Sign-Up.html`                          | Needs Revision |
| Artwork upload / submission form | FR-03, FR-10, FR-11, FR-15 | US-02, US-05, US-06 | `prototype/wireframe/Upload.html`                           | In Progress |
| Record list / artwork feed | FR-05, FR-06, FR-08 | US-03, US-04, US-08 | `prototype/wireframe/homepage.html`                         | In Progress |
| Search and filter | FR-06 | US-03, US-08 | `homepage.html`, `Artwork.html`, shared header search       | In Progress |
| Artwork detail and comments | FR-02, FR-07, FR-10 | US-01, US-02, US-06 | `prototype/wireframe/Artwork.html`                          | In Progress |
| Creator profile / portfolio | FR-01, FR-12, FR-15 | US-07, US-09, US-10 | `prototype/wireframe/User-Profile.html`                     | In Progress |
| Creator dashboard / analytics | FR-12 | US-09 | `prototype/wireframe/User-Dashboard.html.html`                          | In Progress |
| Status tracking | FR-08, FR-09 | US-04, US-06 | Artwork cards, upload status fields, moderator status rules | Planned |
| Admin / moderator function | FR-09 | US-06 | Moderator dashboard module still to be finalized            | Planned |
| Responsible design updates | FR-03, FR-09, FR-10, FR-12, FR-15 | US-01 to US-10 | All forms, dashboard, upload, admin flow                    | Needs Revision |

## 3. Implementation Approach
Explain how your prototype will be built.

- Frontend:
  - Continue with the current HTML/CSS/JavaScript wireframes in `prototype/wireframe/`.
  - Standardize the shared IceCream header across `homepage.html`, `Artwork.html`, `Upload.html`, `login.html`, `Sign-Up.html`, `User-Profile.html`, and `User-Dashboard.html`.
  - Replace remaining Pixiv-style wording and labels with IceCream branding.
  - Keep the first sprint focused on a simple clickable workflow: login/sign-up -> browse gallery -> upload artwork -> open artwork detail -> view profile/dashboard.

- Data source/storage:
  - Use simulated backend data from CSV/mock files during Sprint 1.
  - Main data sources: `data/Users_records.csv`, `data/artworks_records.csv`, and `data/comments_records.csv`.
  - Keep sample records anonymized and avoid real passwords, real names, student IDs, or private contact details.
  - Firebase Auth and Firestore remain planned tools for a later implementation stage.

- Admin/status handling:
  - Use the existing statuses `Published`, `Underchecking`, and `Withdrawn`.
  - Normal users should only withdraw their own artworks/comments.
  - Moderators should be the only users allowed to set content to `Underchecking`, remove harmful comments, or pin critiques.
  - Sprint 1 can simulate these role rules in documentation or mock UI if a real backend is not ready.

- Search/filter approach:
  - Use artwork tags, titles, creator aliases, fandom tags, and critique status as the first search/filter fields.
  - Prevent duplicate or invalid tags in the upload/tag workflow.
  - Keep search and filter labels clear and consistent across homepage/gallery/detail screens.

- Validation approach:
  - Add visible validation messages for required upload fields: title, image, tags, AI-generated disclosure, and critique/status fields.
  - Add file type and file size checks for image upload, based on the upload page note: JPEG/GIF/PNG up to 32MB.
  - Add minimum length and constructive guidance for critique/comment submission.
  - Remove or justify unnecessary sign-up fields such as gender and date of birth.
  - Add upload ownership/permission confirmation before submission.

- Screenshots/evidence approach:
  - Capture screenshots of each implemented Sprint 1 screen.
  - Save prototype evidence in the `screenshots/` folder.
  - Record implementation progress in `docs/weekly-logbook.md`.
  - Link final evidence to requirement IDs and user stories in project documentation.

## 4. Member Responsibilities

| Member | Responsibility | Evidence of Contribution |
|---|---|---|
| Gwyndolin | Product scope, requirement traceability, responsible design notes, privacy/consent wording, weekly logbook updates | Commit / issue / documentation files |
| Kyaw Naing Soe | Technical implementation, shared header cleanup, form validation, simulated data connection, status/admin logic | Commit / issue / prototype files |
| RunluQing | UI consistency, IceCream branding, screen layout cleanup, asset replacement, screenshots and visual evidence | Commit / issue / wireframe files |

## 5. Risks or Blockers
Write technical problems your team faced and how you plan to solve them.

| Risk / Blocker | Impact | Planned Solution |
|---|---|---|
| Some wireframe files still contain Pixiv-style branding or layout references. | Final prototype may appear copied or legally risky. | Replace Pixiv text, premium labels, and layout references with IceCream branding and original UI wording. |
| `persionview.html` filename is misspelled. | File naming may confuse team members or documentation links. | Rename to `personview.html` or `profile.html` after updating links. |
| Sign-up form collects gender and date of birth. | These fields are not required by the MVP and create privacy risk. | Remove these fields or document a clear approved reason for collecting them. |
| Upload form does not fully enforce validation in static HTML. | Users may submit incomplete or unsafe records. | Add required fields, file type/size checks, duplicate tag prevention, and clear error messages. |
| Admin/moderator function is planned but not fully implemented. | Normal users may appear able to perform admin actions if role separation is unclear. | Create a separate moderator dashboard or clearly marked simulated moderator flow. |
| Backend is not fully implemented yet. | Dynamic upload, comments, sessions, and status updates may remain static. | Use simulated CSV/mock records for Sprint 1 and document Firebase as the planned backend direction. |
| External placeholder images are used. | Asset/license risk and weak project identity. | Replace with original, approved, licensed, or clearly credited sample artwork. |
| Duplicate tag creation caused issues in validation data. | Search/filter workflow may crash or produce inaccurate results. | Normalize tags, prevent duplicates, and show user-friendly validation messages. |
