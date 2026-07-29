# Lab 13 User Testing Results - IceCream

## 1. Testing Summary

- **Evidence reviewed:** 20 anonymized validation records dated 2026-07-20 to 2026-07-25.
- **Current smoke-test date:** 2026-07-29.
- **Prototype:** local IceCream server at `http://127.0.0.1:8000/`.
- **Historical participants:** 20 anonymized prototype testers.
- **Historical devices:** 8 mobile, 6 desktop, 4 laptop, and 2 tablet.
- **Current verification type:** read-only, team-style simulated final demo check (allowed by the Lab 13 task sheet).

The historical dataset represents broader prototype validation and includes concepts beyond the currently implemented local HTML/CSV build. The current smoke test was therefore used to confirm which screens and read-only pathways work today. No new external participants are claimed for 2026-07-29.

## 2. Historical Validation Metrics

| Metric | Result | Interpretation |
| --- | ---: | --- |
| Task completion | 17/20 (85%) | Meets the 80% completion target. |
| Average ease of use | 3.9/5 | Slightly below the 4.0 target. |
| Average usefulness | 4.4/5 | Strong perceived value. |
| Would use again | 16 Yes, 3 Maybe, 1 No | 80% definite return interest. |
| Records with a confusion point | 13/20 (65%) | Navigation and control clarity remain priorities. |
| Decision signal | 13 Validated, 4 Partial, 3 Revise | Core value is supported, but final scope needs focused fixes. |

## 3. Current Task Verification

| Task ID | Tester Role / Method | Task Attempted | Result | Issue Found | Improvement Action |
| --- | --- | --- | --- | --- | --- |
| T01 | Team validation reviewer / HTTP smoke test | Open landing page and gallery. | **Success** | Both pages returned successfully; the local-server prerequisite may be missed by first-time users. | Keep the landing-page “How to use” section and include startup instructions in the demo. |
| T02 | Team validation reviewer / screen and route check | Access sign-up and login. | **Partial** | Screens load, but no new account was created during the read-only check. | Run the moderated account task before Lab 14 and record validation messages. |
| T03 | Team validation reviewer / screen and implementation check | Access upload and confirm storage pathway. | **Partial** | Upload screen and server handler exist; the check avoided writing a new record. Historical testing reported content-level wording confusion. | Run a copyright-safe two-image upload and clarify the content-level label. |
| T04 | Team validation reviewer / live read-only API test | Search by the existing `touhou` tag. | **Success** | Search returned five matching artworks. | Repeat the task with target users and record completion time. |
| T05 | Team validation reviewer / live read-only API test | Open artwork detail for `A010`. | **Success** | Detail data and the multi-image display loaded successfully. | Verify the like response and return navigation during moderated testing. |
| T06 | Team validation reviewer / HTTP smoke test | Open profile and creator dashboard. | **Partial** | Both pages load; displayed totals were not compared with the current CSV records during the smoke test. | Verify calculations against CSV records and add clear empty states/metric definitions. |

### Smoke-Test Technical Evidence

- Landing, homepage, sign-up, login, upload, search, profile, and dashboard pages all returned HTTP 200.
- Homepage data returned five recommended artwork cards.
- Tag search for `touhou` returned five results.
- Artwork detail for `A010` returned successfully.

## 4. Common Usability and Scope Issues

| Issue ID | Issue Description | Severity | Related Requirement | Proposed Fix |
| --- | --- | --- | --- | --- |
| UI-01 | Content/sanity-level wording caused historical confusion. | Important | FR-03, FR-10 | Replace technical labels with plain language and short explanations. |
| UI-02 | Mobile controls and subtle indicators caused confusion in historical tests. | Useful | FR-13, FR-14 | Increase touch targets and verify key flows at mobile width. |
| UI-03 | The final moderated user round has not yet been conducted. | Important | FR-16 | Run the five-participant plan and record task time, hints, and outcomes. |
| UI-04 | Dashboard values require a final comparison with stored CSV records. | Useful | FR-12 | Verify displayed totals and add metric definitions and empty states. |

## 5. User Feedback Summary

Participants valued multi-image publishing, tag-based discovery, chronological artwork browsing, profiles, and quick engagement. The strongest negative signals concerned unclear controls on mobile, content-level wording, duplicate tag handling, and workflows that were conceptually tested but are not fully present in the current local build.

## 6. Evidence-Based Decision

**Ready for final usability refinement.**

The publish-and-discover pathway is demonstrable and historical usefulness is strong. Before Lab 14, the team should run the planned moderated test, clarify content-level wording, verify dashboard values, and complete mobile/presentation polish.
