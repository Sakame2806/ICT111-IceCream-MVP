# Technical Architecture

- **Chosen Platform**: Web-based application
- **Frontend**: Vue.js 3, HTML, TailwindCSS, and CSS Grid
- **Storage Method**: Firebase Firestore database for real-time storage and user sessions
- **Admin Mechanism**: Art Club Moderator Dashboard (allows moderators to review reported entries, delete off-topic comments, pin high-quality critiques, and set content status to "Underchecking")
- **Dashboard Method**: Creator Dashboard (displays views, likes, critique breakdown by category, and a "Critique Karma" score)
- **Simulated Features**: If Firebase is not fully implemented, data storage, user sessions, and backend functionalities will be simulated using local browser storage and mock data files (mock-users.csv, mock-artworks.csv, mock-comments.csv).
