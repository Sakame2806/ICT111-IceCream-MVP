# IceCream Startup / Product Metrics

> These metrics measure whether IceCream is attracting users, helping artists
> publish and discover artwork, encouraging constructive interaction, and
> providing an easy-to-use experience. Each metric is tied to a product
> decision rather than being treated as a vanity number.

## 1. Metrics Summary

| Metric ID | Metric Name | Metric Type | Why This Metric Matters | Formula / How to Calculate | Data Source | Prototype Screen |
|---|---|---|---|---|---|---|
| M-01 | Registered Users | Acquisition | Shows whether target users are willing to create an IceCream account and enter the community. | Count unique `User_id` values | `data/Users_records.csv` | Sign-Up, Login, User Dashboard |
| M-02 | Published Artworks | Usage | Measures whether creators complete IceCream's main contribution activity instead of only browsing. | Count artwork records where `Status = Published` | `data/artworks_records.csv` | Upload, Homepage/Gallery, User Dashboard |
| M-03 | Artwork Publication Rate | Content Health | Reveals how much submitted artwork becomes visible to the community and whether review or withdrawal creates friction. | Published artworks / total artwork records × 100 | `data/artworks_records.csv` | User Dashboard, future Moderator Dashboard |
| M-04 | Constructive Comments per Published Artwork | Engagement | Measures meaningful feedback between artists, which is a core value proposition of IceCream. | Number of published comments / number of published artworks | `data/comments_records.csv`, `data/artworks_records.csv` | Artwork Detail, User Dashboard |
| M-05 | Task Completion Rate | Validation | Shows whether users can complete the tested core workflows, including upload, discovery, commenting, following, and account registration. | Completed validation tasks / total validation tasks × 100 | `data/validation-results.csv` | Analytics Summary / testing report |
| M-06 | User Confusion Rate | Usability | Identifies navigation and interaction friction even when users eventually finish a task. | Test sessions with a recorded confusion point / total test sessions × 100 | `data/validation-results.csv` | Analytics Summary / testing report |
| M-07 | Average Usefulness Score | Value Validation | Indicates whether users believe the product solves a worthwhile problem for artists and art enthusiasts. | Sum of usefulness scores / number of valid responses | `data/validation-results.csv` | Analytics Summary / testing report |
| M-08 | Return-Interest Rate | Retention Potential | Estimates whether the prototype provides enough value for users to return after their first experience. | Users answering “Yes” to `WouldUseAgain` / total test users × 100 | `data/validation-results.csv` | Analytics Summary / testing report |

## 2. Metrics Interpretation

The current prototype contains **6 registered user records**, **5 artwork
records**, and **5 comment records**. Of the five artworks, three are published,
giving an initial **artwork publication rate of 60%**; the remaining records are
under checking or withdrawn. Three comments are published, producing an initial
average of **1 published comment per published artwork**. These content figures
are only a small prototype baseline and should not be interpreted as evidence
of market traction yet.

The stronger validation evidence comes from the 20-participant MVP test. The
recorded **task completion rate is 85%**, above the project's 80% success
threshold, while the **average usefulness score is 4.40/5** and the
**return-interest rate is 80%**. Together, these results indicate that the core
idea is useful and that users can generally complete important workflows.
However, the **65% confusion rate** is substantially above the project's target
of 30% or lower. The team should therefore prioritize clearer navigation,
larger and more visible action controls, better explanations for tags and
content settings, and first-time-user guidance before expanding the feature
set. After these changes, the same task-completion and confusion metrics should
be measured again to determine whether the redesign actually reduces friction.

## 3. Link to Final Prototype

The final prototype will demonstrate these metrics in two places:

1. **Creator Dashboard:** display the signed-in creator's published artwork
   count, total views, likes, favorites, and published comments. The dashboard
   should calculate values from stored records rather than showing fixed sample
   numbers.
2. **Analytics Summary:** display community-level registered users, published
   artworks, publication rate, comments per artwork, task completion rate,
   confusion rate, usefulness score, and return-interest rate. Validation
   metrics may be loaded from the test-results dataset, while live product
   metrics should come from user, artwork, and comment records.

For the current local prototype, user acquisition is demonstrated through
`Sign-Up.html` and `login.html`, which write to and read from
`data/Users_records.csv`. Artwork and comment activity is represented by
`data/artworks_records.csv` and `data/comments_records.csv`. In a production
version, these same formulas should be calculated from the application database
and filtered by a clearly stated reporting period, such as the last 7 or 30
days.
