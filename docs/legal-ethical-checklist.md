# Legal and Ethical Checklist

## Project Title
IceCream - Campus Digital Art Community Platform

## Screens and Features Reviewed
| Screen / Feature | Collects User Data? | Displays User Data? | Updates User Data? | May Expose User Data? | Evidence / Notes |
|---|---|---|---|---|---|
| Landing page / homepage | No, unless search/navigation activity is tracked | Yes | No | Low | Displays featured artwork, platform purpose, and CTA buttons. Use sample or approved artwork only. |
| Sign-up screen | Yes | Yes | Yes | Medium | Collects nickname/alias and authentication data. Avoid real names, student IDs, and plain-text passwords. |
| Login screen | Yes | Yes | Yes | Medium | Collects login credentials and updates user session state. Error messages should not reveal private account information. |
| Gallery feed | Yes | Yes | No | Medium | Uses search terms, style tags, fandom tags, and critique filters. Displays artwork title, thumbnail, creator alias, tags, and critique badge. |
| Artwork upload form | Yes | Yes | Yes | High | Collects title, description, image/file address, tags, fandom, critique focus, and creator user ID. Uploaded files may contain copyrighted or personal content. |
| Artwork detail / comic reader | Possibly | Yes | Possibly | High | Displays full artwork/comic pages, creator alias, tags, critique request, and comments. High-resolution artwork could be copied or misused. |
| Structured critique / comment form | Yes | Yes | Yes | Medium | Collects comment content, critique category, user ID, artwork ID, and status. Comments may expose opinions or harmful language. |
| Creator profile / portfolio page | Yes | Yes | Yes | Medium | Displays alias, profile details, uploaded works, and portfolio. Public profile fields should be optional. |
| Creator dashboard / analytics page | Yes | Yes | Yes | Medium | Displays views, likes, critique counts, and critique karma. Analytics should be private to the creator/admin. |
| Moderator dashboard | Yes | Yes | Yes | High | Displays reported content and allows moderators to change status, remove comments, or pin critiques. Admin access must be separated from normal users. |
| Firebase / local mock data storage | Yes | Yes | Yes | High | Stores users, artworks, comments, statuses, and file addresses. Mock records must stay anonymized and avoid real passwords. |

## Ethical Review
| Check Item | Yes/No | Evidence / Notes | Mitigation Action | Owner | GitHub Issue/Commit |
|---|---|---|---|---|---|
| Users are informed about the purpose of the prototype. | Yes | `system-requirements.md` and the landing page describe IceCream as a campus digital art community for sharing artwork and receiving structured critique. | Keep the homepage purpose clear and add a short prototype/testing notice during user tests. | Documentation Lead | To be added |
| The prototype avoids misleading claims. | With revision | Homepage and gallery may show featured/popular artwork, but prototype data may be sample data. | Label demo records, featured artwork, and analytics as sample/prototype data unless they come from real validated users. | UX/UI Lead | To be added |
| The prototype does not collect unnecessary sensitive data. | With revision | `data-structure.md` includes User ID, nickname, and password. FR-15 says aliases should be used instead of real names/student IDs. | Do not store real passwords in CSV/mock records; use aliases only; avoid real names, student IDs, phone numbers, and private contact details. | Technical Lead | To be added |
| Users can understand what happens after submission. | With revision | Upload, critique, and status features include confirmation messages and status values such as Published, Underchecking, and Withdrawn. | Add clear confirmation messages after upload/comment submission and explain each status value in the interface. | UX/UI Lead | To be added |
| Admin or manager actions are clearly separated from user actions. | Yes | FR-09 and `technical-architecture.md` define an Art Club Moderator Dashboard for reported entries, comment removal, pinned critiques, and Underchecking status. | Restrict moderator actions to admin/moderator accounts and keep normal user screens separate. | Technical Lead | To be added |
| The prototype avoids unfair or harmful treatment of users. | With revision | Structured critique and moderation reduce harmful comments, but comments/tags can still create harassment or unfair categorization. | Add moderation/reporting, minimum critique length, respectful critique guidance, and avoid public ranking based only on likes or karma. | Product Lead | To be added |

## Summary Decision
- Safe to continue: With revision
- Required revision before implementation:
  - Add a short consent/data-use statement near sign-up and upload forms.
  - Use aliases only and avoid collecting real names, student IDs, private contact details, or real passwords.
  - Label sample artwork, sample analytics, and mock data clearly during prototype testing.
  - Add upload confirmation that users own or have permission to share the artwork.
  - Keep creator analytics private to the creator/admin.
  - Restrict moderator dashboard actions to authorized moderator accounts.
  - Explain status values such as Published, Underchecking, and Withdrawn to users.
