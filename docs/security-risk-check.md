# Basic Security Risk Check

| Area | Risk Question | Current Status | Risk Level | Mitigation | Owner |
|---|---|---|---|---|---|
| Form input | Can incomplete or invalid data be submitted? | The upload form marks Tags, Age Limit, and AI-generated as required, but the prototype HTML does not enforce `required` attributes or validation. Login/sign-up fields also lack visible validation rules. | Medium | Add required-field validation for title, image, tags, critique focus/status, login email, and password. Show clear validation messages before submission. | Technical Lead |
| Form input | Can users submit unsafe or harmful text content? | Critique/comment content and artwork descriptions are planned, but the current prototype does not show sanitization or minimum-length validation in the HTML screens. | Medium | Enforce a minimum critique length, escape/sanitize displayed text, block empty or emoji-only comments, and add constructive-comment guidance. | Technical Lead |
| Sign-up data | Does the sign-up form collect more data than needed? | `sign.html` collects nickname, gender, date of birth, and terms agreement. The current data model only requires User ID, nickname, and authentication data. | Medium | Limit sign-up fields to nickname/alias and authentication only for MVP. Remove gender and date of birth unless a clear requirement is documented. | Product Lead |
| Admin function | Can normal users access admin actions? | `technical-architecture.md` defines an Art Club Moderator Dashboard for reviewing reports, deleting comments, pinning critiques, and changing content to Underchecking. Role enforcement is not yet visible in the prototype files. | High | Separate normal user and moderator routes/screens. Require moderator role before showing remove, pin, report-review, ban, or status-change actions. | Technical Lead |
| Data display | Is private information visible to everyone? | Public screens display creator aliases, artwork thumbnails, tags, critique badges, and comments. Current mock data uses anonymized passwords, but raw `User_id` values exist in CSV files. | Medium | Display nicknames instead of raw user IDs. Keep passwords and auth data internal. Keep creator analytics and moderation notes private/admin-only. | Documentation Lead |
| Status update | Can records be edited without control? | Artworks and comments use statuses: Published, Underchecking, and Withdrawn. The data model says admins can update Underchecking and users can withdraw their own records, but role rules are not implemented in static HTML. | High | Only creators can withdraw their own artworks/comments. Only moderators can set Underchecking or restore Published after review. Add confirmation messages and status-change logs. | Technical Lead |
| Public links | Does a public link expose data that should be private? | Prototype pages use public placeholder image URLs from Unsplash and Picsum. Future Firebase or static links may expose artwork files, profile images, or mock records if shared publicly. | Medium | Use sample/public assets only in public pages. Avoid private local file paths. For Firebase, use storage rules and publish only intended-public records. | Technical Lead |
| File upload | If used, can unsafe or unrelated files be uploaded? | The upload page says JPEG/GIF/PNG up to 32MB, but the prototype uses a button instead of an actual validated file input. There is no visible file type or size enforcement. | High | Add file input restrictions for image types only, file size limit, upload error messages, and moderation review for reported or inappropriate files. | Technical Lead |
| Data editing | Can users edit or delete records they do not own? | Lab 08 validation data mentions editing artwork descriptions, deleting uploaded artwork, updating profile bio/avatar, and admin banning. Ownership checks are not visible in the prototype files. | High | Check record ownership before edit/delete actions. Use soft delete for artworks/comments and restrict admin-only user status updates. | Technical Lead |
| Sample data | Is real sensitive data stored in the repository? | `Users_records.csv` uses `ANONYMIZED` for passwords. Validation data uses test IDs such as `U001`, but team profile contains real student IDs. | Medium | Keep prototype datasets anonymized. Do not include real passwords, private contact details, or unnecessary student IDs in public-facing Lab 09 materials. | Documentation Lead |
| Search and tags | Can search/tag input break filtering or create duplicate/invalid tags? | Lab 08 validation found that bulk creating new tags failed when duplicate tag names were inserted. | Medium | Normalize tag names, prevent duplicates, limit tag length, and show a friendly error instead of crashing. | Technical Lead |
| External scripts | Can third-party scripts affect prototype security? | `login.html` and `userpage.html` load Tailwind from CDN; `userpage.html` loads Font Awesome from cdnjs. | Low / Medium | Use trusted CDNs only for prototype. For final build, pin versions and consider local/package-managed dependencies. | Technical Lead |

## Security Decision
- Continue without change / Continue with mitigation / Redesign required: **Continue with mitigation**

## Required Mitigations Before Final Prototype
- Add validation messages for required upload, sign-up, login, tag, and critique fields.
- Remove unnecessary sign-up fields such as gender and date of birth unless the team documents why they are needed.
- Use no real passwords or sensitive personal data in CSV/mock records.
- Separate normal user actions from moderator/admin actions.
- Restrict artwork/comment status changes by role.
- Validate image upload type and size before accepting files.
- Display aliases instead of raw user IDs on public screens.
- Prevent duplicate/invalid tags and show clear error messages.
- Keep creator analytics and moderation records private or admin-only.
