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

## Lab 06: MVP Experiment Plan

### What We Completed
1. Defined the MVP experiment objective to validate if artists and hobbyists can easily navigate IceCream to find artworks that match their preferences.
2. Determined the requirement scope for the experiment (Detail view, Upload Page, Tagging function).
3. Selected a backend/database prototype as the MVP experiment type.
4. Identified the test user groups (Hobbyists and Artists).

### What We Learned
1. How to structure an experiment to validate core assumptions effectively.
2. The importance of selecting the right type of prototype (backend/database) to test our specific community engagement hypotheses.

### Evidence of Work
- MVP Experiment Plan: [mvp-experiment-plan.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/mvp-experiment-plan.md)

### Plan for Next Week
- Create the experiment script and conduct the actual user testing using the backend/database prototype.

## Lab 07: Experiment Script & Testing

### What We Completed
1. Created a structured experiment script to guide test users through the IceCream prototype.
2. Defined a specific test scenario where users act as campus artists and hobbyists looking to discover relevant artwork.
3. Detailed a set of 5 concrete tasks (e.g., browse gallery, use filters, open artwork details) to evaluate the requirements.
4. Observed users and recorded answers to closing questions regarding what was easy, confusing, or most useful.

### What We Learned
1. How to conduct user testing without bias by focusing on the product experience rather than testing the user.
2. The landing page clearly communicates the value proposition, but some users may find the tagging and structured critique focus slightly confusing initially.
3. The upload flow and structured critique features are considered the most useful parts of the MVP.

### Evidence of Work
- Experiment Script: [experiment-script.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/experiment-script.md)

### Plan for Next Week
- Analyze the experiment results in detail and refine the prototype's interface and flow based on the user feedback gathered.

## Lab 08: MVP Data Analysis and Decision Making

### What We Completed
1. Analyzed the MVP validation data (N=20) using PowerBI to identify quantitative performance indicators.
2. Created an Analytics Insights report to break down usability bottlenecks and role-based segmentations.
3. Synthesized findings into a Customer Validation Summary to outline the validation status and critical friction points.
4. Drafted an MVP Decision & Strategic Roadmap to shift focus from feature expansion to experience optimization.

### What We Learned
1. How to use data analysis tools like PowerBI to extract actionable insights from user testing data.
2. The core functionality of our MVP was validated, but significant UX friction exists (65% confusion rate).
3. The importance of prioritizing UI/UX refinement, specifically for new/general users, over adding new features.

### Evidence of Work
- Analytics Insights: [analytics-insights.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/analytics-insights.md)
- Customer Validation Summary: [customer-validation-summary.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/customer-validation-summary.md)
- MVP Decision: [mvp-decision.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/mvp-decision.md)
- PowerBI Dashboard Screenshot: ![PowerBI Dashboard](/Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/screenshots/lab08-powerbi-dashboard.png)

### Plan for Next Week
- Implement the high-priority UX redesigns identified in the MVP decision roadmap.

## Lab 09: Legal, Ethical, IP, Privacy, and Security Check

### What We Completed
1. Reviewed the IceCream prototype from a responsible IT development perspective, focusing on legal, ethical, privacy, IP, data protection, and security risks.
2. Created a legal and ethical checklist to identify which screens and features collect, display, update, or expose user data.
3. Created a privacy and data protection document listing each data field used by the prototype and classifying it as necessary, optional, personal, sensitive, public, internal, creator-only, or admin-only.
4. Reviewed third-party assets used or planned in the prototype, including Tailwind CSS, Font Awesome, Unsplash, Lorem Picsum, Pixiv-inspired references, Firebase, Vue.js, mock datasets, and AI-generated material disclosure.
5. Created a basic security risk check covering form validation, admin access, public links, exposed records, data editing, file upload, status updates, and sample data handling.
6. Created a risk register with privacy, ethical, IP, security, legal, and data quality risks, including severity, likelihood, mitigation, owner, and evidence.
7. Created an updated requirements note because the Lab 09 review showed that FR-03, FR-09, FR-10, FR-12, and FR-15 need clarification before final implementation.

### What We Learned
1. Responsible design is not separate from prototype development; privacy, security, legal, and ethical concerns must be checked before implementation continues.
2. The prototype should use aliases and anonymized sample data instead of real names, student IDs, private contact details, or real passwords.
3. External assets and brand references need clear source, license, credit, or replacement decisions before final submission.
4. Admin and moderator actions must be clearly separated from normal user actions to reduce misuse and unauthorized changes.
5. Upload, tag, comment, and status features require stronger validation and clearer user feedback.

### Problems or Difficulties
1. Some prototype screens still include Pixiv branding, Pixiv-style wording, external placeholder images, and one unrelated prototype file that should be removed or replaced before final submission.
2. The sign-up screen currently collects gender and date of birth, but these fields are not required by the current IceCream MVP data model.
3. Upload and form validation are described in requirements, but the static prototype does not fully enforce required fields, file type limits, file size limits, or duplicate tag prevention.
4. GitHub issue or commit references still need to be added to the Lab 09 documents after the team creates traceable evidence.

### Evidence of Work
- Legal and Ethical Checklist: [legal-ethical-checklist.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/legal-ethical-checklist.md)
- Privacy and Data Protection: [privacy-and-data-protection.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/privacy-and-data-protection.md)
- IP and Third-Party Assets Register: [ip-and-third-party-assets.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/ip-and-third-party-assets.md)
- Security Risk Check: [security-risk-check.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/security-risk-check.md)
- Risk Register: [risk-register.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/risk-register.md)
- Updated Requirements Note: [updated-requirements-note.md](file:///Users/kyawnaingsoe/Desktop/ICT111-IceCream-MVP/docs/updated-requirements-note.md)

### Decision Made This Week
The IceCream prototype is safe to continue building **with mitigation**. The team must clarify responsible design requirements, replace or credit third-party assets, avoid unnecessary sensitive data, improve validation, and restrict moderator/admin actions before final implementation.

### Plan for Next Week
- Create GitHub issues or commits for the Lab 09 mitigation actions.
- Replace Pixiv branding and external placeholder artwork with IceCream-branded or properly credited assets.
- Update prototype forms to reduce unnecessary data collection and improve validation messages.
- Continue implementing UX improvements while following the updated responsible design requirements.
