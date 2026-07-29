# IceCream Final Prototype Demo Script

## Demo Objective

Show the complete working pathway from the IceCream landing page to account access, artwork upload, gallery discovery, artwork detail, creator profile, and dashboard. The demo must also state honestly which final requirements still need work before Lab 14.

## Presenter Roles

| Member | Role in Demo | Part Presented |
| --- | --- | --- |
| Gwyndolin | Product and documentation lead | Problem, target user, landing page, value, closing |
| Kyaw Naing Soe | Technical and validation lead | Server setup, account flow, upload, storage, search |
| RunluQing | UX/UI lead | Artwork detail, profile/dashboard, usability findings |

## Pre-Demo Setup

1. Open a terminal in the repository root.
2. Run `python prototype/server.py`.
3. Keep the terminal open.
4. Open `http://127.0.0.1:8000/landing-page/`.
5. Prepare an alias account and one copyright-safe JPEG/PNG/GIF test image.

## Demo Flow

| Step | Screen / Feature | Presenter Action and Script | Requirement ID | Expected User Value |
| --- | --- | --- | --- | --- |
| 1 | Landing page | "IceCream is for campus digital artists whose work disappears in busy chat feeds. The landing page explains the problem, audience, privacy approach, and how to start the local prototype." Click **Explore the gallery**. | FR-01, FR-13, FR-15 | Understand the product and enter the prototype confidently. |
| 2 | Homepage / gallery | Show the latest works, recommended works, and up to ten tags drawn from stored artwork records. Explain that the gallery keeps work visible beyond a chat timeline. | FR-04, FR-05 | Discover current community artwork in one place. |
| 3 | Sign-up and login | Open **Create an account**, register with an alias, then demonstrate login. Point out validation and that the prototype stores records locally. | FR-10, FR-15 | Enter the workflow without providing a real name or student ID. |
| 4 | Upload artwork | Open **Upload**, select one or more images, enter a title, description, tags, and content level, then publish. Show the confirmation response and explain CSV/image storage. | FR-03, FR-04, FR-10, FR-11 | Publish single- or multi-image artwork with useful metadata. |
| 5 | Search and tags | Search using part of an artwork title, then repeat with a tag. Open one matching result. | FR-05, FR-06 | Find relevant work without exact title matching. |
| 6 | Artwork detail | Show all images from top to bottom, the creator, tags, description, and like control. | FR-05, FR-13 | View an entire project in the intended order and understand its context. |
| 7 | Profile and logout | Click the avatar, open the profile, show all uploads for the signed-in user, then demonstrate the logout menu. | FR-05, FR-13, FR-15 | Keep a coherent portfolio and control the session. |
| 8 | Creator dashboard | Open the creator dashboard and explain the current engagement summary. | FR-12 | Review simple engagement information in one view. |
| 9 | Responsive and validation check | Resize to a mobile width or show mobile evidence, then demonstrate a required-field error without submitting invalid data. | FR-10, FR-14 | See that the interface prevents common errors and adapts to smaller screens. |
| 10 | Closing | "IceCream already proves the publish-and-discover workflow. Testing achieved 85% task completion and 4.4/5 usefulness across 20 anonymized validation records. Before Lab 14, we will complete final usability testing and presentation polish." | FR-16 | Connect the demo, evidence, and next decision. |

## Demo Recovery Notes

- If the server is unavailable, rerun `python prototype/server.py` and reload the browser.
- If a CSV file cannot be written, close it in Excel and retry.
- If upload data is unsuitable for a public demo, use a copyright-safe team-owned test image.

## Closing Statement

IceCream gives campus artists a focused place to publish multi-image work, remain discoverable through titles and tags, and build a visible portfolio.
