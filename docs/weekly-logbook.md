# Weekly Venture Logbook
## Lab 1: Lab Setup and IT Venture Repository
### What We Completed
1. Created the repository for ICT111 on Github
2. Created the team-profile and Tasks were assigned to team members.
3. Created the README.md
### What We Learned
1. Basic usage of GitHub
2. Basic usage of Markdown
3. Basic usage of Visual Studio Code
### Problems or Difficulties
1. Add a correct SSH key.
### Evidence of Work
- GitHub repository link: https://github.com/Sakame2806/ICT111-IceCream-MVP
- Screenshot:
- File created:
- Commit link: https://github.com/Sakame2806/ICT111-IceCream-MVP/commits/main/
### Decision Made This Week
We decided on our communication channels and and IT Venture.
### Plan for Next Week
To decide which idea we are going to continue.

## Lab 02: IT Opportunity Scanning
### What We Completed
1. Shared our opinions on those six ideas.
2. Decided idea 5 as our semester project idea according to NUF.
3. Decided what to do next week.
### Selected Opportunity
 Online artists Community.
### Why We Selected It
Explain the decision using NUF scoring. We seleted idea 5. It is suitable for artists and we can collect data when they use our service we can track their behavior and collect user data.
### What We Rejected
 We rejected idea 2 because it requires third-part payment API, so it need advanced cybersecurity to protect private user infomation. That's the reason we rejected it.
### What We Learned
1. To avoid too complecated project ideas which we can hardly to realize.
2. Using NUF to value our idea
3. Knowing what tools to be used for our project.
### Evidence of Work
- Opportunity scan file:
- NUF scoring file:
- Selected opportunity file:
- GitHub issue screenshot:
- Commit link:
### Plan for Lab 03
Write how the team will conduct customer problem discovery.

## Lab 3: Collect user responses and analyse them.
### What We Completed
1. discussed what should be included in the survey.
2. Collect Customer's responses and created an Assumption-Evidence Table
3. Analyse user's responses
### What We Learned
1. How to create a survey.
2. Discorver insights from Customer's responses.

### Problems or Difficulties
1. Analyze the customer's true thoughts.
### Evidence of Work
- GitHub repository link: https://github.com/Sakame2806/ICT111-IceCream-MVP
- Raw response table: 
### Decision Made This Week
We decided to continue our project using current ideas.
### Plan for Next Week
Create the flowchart and prototype of our project.

## Lab 04: User Persona, Requirements, and User Stories

### Primary Target User
Digital visual artists (student illustrators, designers) and art hobbyists in Thailand who want to share their artwork, receive constructive feedback, and find style/fandom-specific groups without their posts getting lost in unstructured chat feeds.

### Persona Summary
- Persona name:
- User type:
- Main goal:
- Main pain point:
- Current workaround:

### Key Requirements
| Req ID | Requirement | Priority | Related Evidence |
|---|---|---|---|
| FR-01 | Dedicated landing page showcasing featured student art and clear CTA to join | Must | 10/10 respondents need a dedicated campus community space |
| FR-03 | Artwork upload form (with single/multi-page options for comics) and structured critique form | Must | Respondents 1, 2, 3, 5, 10 demand structured feedback (anatomy, coloring) and comic layouts |
| FR-06 | Style, fandom, and critique focus filters (Anime, Comic, Touhou, VTuber, Needs Anatomy Critique) | Must | Respondents 3, 8 requested search/filtering by fandom/style to prevent fragmentation |
| FR-10 | Input validations (required upload fields, min word count for critiques) to prevent emoji/sticker-only spam | Must | Respondents 1, 2, 6, 10 highlight the lack of constructive critique and prevalence of empty reactions |
| NFR-01 | Responsive user interface design supporting seamless mobile and desktop web browsing | Must | Student preference for web-based portfolio setup and high-resolution mobile browsing |

### MVP Feature Scope
| Feature | Priority | Included in Final Prototype? |
|---|---|---|
| F01: Landing & Navigation Portal | Must | Yes |
| F02: Multi-page Upload & Critique Spec Form | Must | Yes |
| F03: Style & Fandom Categorized Feed | Must | Yes |
| F04: Structured Critique Engine | Must | Yes |
| F05: Creator Analytics & Critique Karma | Should | Yes |
| F06: Moderator Admin Dashboard | Should | Yes |
| F07: Collaborative Contests & Fandom Events | Could | No |
| F08: Commission Matching System | Won't | No |

### Diagram Links
- User flow diagram: [Icecream_flowchart.drawio.png](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/diagrams/Icecream_flowchart.drawio.png)
- Use case diagram: [Use Case Diagrams.drawio.png](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/diagrams/Use%20Case%20Diagrams.drawio.png)

### GitHub Contribution Evidence
All members contributed to this repository through commits, issues, or pull requests.

## Lab 05: Product Concept, Wireframing, and Usability Review

### What We Completed
1. **Defined Product Concept**: Detailed the target audience (campus artists/hobbyists), problem statement, proposed solution (IceCream website with structured critique system), value proposition, and MVP scope vs. out-of-scope boundaries. (Recorded in [product-concept.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/product-concept.md))
2. **Mapped Features to Requirements**: Mapped planned MVP screens and features (Landing, Upload Form, Gallery Feed, Detail Page, dashboards) to functional requirements from `system-requirements.md` and user stories from `user-stories.md`. (Recorded in [feature-requirement-mapping.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/feature-requirement-mapping.md))
3. **Designed Minimum Required Screens**: Designed layout structures for the core screens (Landing Page, Upload/Submission Form, Detail View, and authentication screens) to support Pixiv-inspired/IceCream mockups. (Detailed in [wireframe-specification.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/wireframe-specification.md))
4. **Created User Flow**: Mapped out the user journey (Landing -> Registration/Login -> Browse/Filter Gallery -> View Detail -> Post Artwork -> Structured Critique/Comment) to verify seamless navigation.
5. **Built Clickable HTML Draft**: Developed HTML/CSS mockups in `prototype/wireframe/` representing actual interface states with realistic sample content:
   - Landing & Gallery Detail Feed: [userpage.html](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/prototype/wireframe/userpage.html)
   - Artwork Upload Form: [input.html](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/prototype/wireframe/input.html)
   - Sign Up Screen: [sign.html](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/prototype/wireframe/sign.html)
   - Login Screen: [login.html](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/prototype/wireframe/login.html)
6. **Reviewed Usability Coverage**: Evaluated the wireframe pages against a usability checklist covering navigation, content clarity, form styling, accessibility, and mobile/responsive designs. (Recorded in [wireframe-usability-checklist.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/wireframe-usability-checklist.md))

### What We Learned
1. Translating customer pain points into a clear and scoped product concept definition.
2. Building responsive HTML/CSS layouts that represent realistic UI prototypes.
3. Performing structured requirement-to-feature coverage reviews using checklists.

### Problems or Difficulties
1. Structuring the critique comment form UI to make it feel encouraging and helpful without being cluttered.
2. Balancing the layout of the gallery card grid so that tags and status badges are readable on smaller device viewports.

### Evidence of Work
- Product Concept: [product-concept.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/product-concept.md)
- Feature Mapping: [feature-requirement-mapping.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/feature-requirement-mapping.md)
- Usability Checklist: [wireframe-usability-checklist.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/wireframe-usability-checklist.md)
- Wireframe Specs: [wireframe-specification.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/wireframe-specification.md)
- Prototype Codebase: [prototype/wireframe/](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/prototype/wireframe/)

### Decisions Made This Week
- We decided on a Pixiv-style gallery format with a focus on categorized feeds and a custom structured feedback comment component.
- We opted to skip commercial and payment features in the MVP to minimize technical complexity and focus on community feedback.

### Plan for Next Week
- Transition the HTML/CSS wireframes into a fully connected, interactive prototype with working navigation and mock data.