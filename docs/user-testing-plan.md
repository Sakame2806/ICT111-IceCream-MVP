# Lab 13 User Testing Plan - IceCream

## 1. Testing Objective

Determine whether target users can understand IceCream, complete its core publish-and-discover pathway without major guidance, and identify the remaining usability or requirement gaps before Lab 14.

## 2. Test User Profile

| User Type | Planned Number | Why This User Type Matters |
| --- | ---: | --- |
| Campus digital artist / illustrator | 3 | Represents the primary uploader and portfolio user. |
| Comic or multi-page artwork creator | 1 | Tests ordered multi-image presentation and upload clarity. |
| Campus artwork viewer | 1 | Tests gallery discovery, artwork detail, and mobile navigation. |

The planned moderated round uses aliases only and does not collect student IDs, passwords, private contact details, or artwork the tester does not have permission to share.

## 3. Testing Tasks

| Task ID | User Task | Related Requirement | Success Criteria | Observation Focus |
| --- | --- | --- | --- | --- |
| T01 | Start at the landing page and explain what IceCream is for. | FR-01, FR-13 | User correctly identifies the target user, problem, and primary action within 30 seconds. | Value-message clarity and first-time guidance. |
| T02 | Create an alias account, log in, and locate the profile/logout menu. | FR-10, FR-15 | Account and login complete without assistance; user can find logout. | Field labels, validation, session feedback. |
| T03 | Upload a two-image artwork with a title and at least one tag. | FR-03, FR-04, FR-10, FR-11 | Upload succeeds, success feedback appears, and images remain in selected order. | File guidance, tag entry, content-level wording, confirmation. |
| T04 | Find an artwork using a partial title, then using a tag. | FR-05, FR-06 | User finds a relevant record through both methods within 60 seconds. | Search-mode clarity and zero-result feedback. |
| T05 | Open artwork detail, inspect all pages, and like the work. | FR-05, FR-13 | User understands image order, creator, tags, and like action. | Image order, like feedback, and navigation back to results. |
| T06 | Open the creator profile and dashboard. | FR-05, FR-12 | User finds uploaded work and correctly explains at least one metric. | Metric labels, empty states, ownership clarity. |

## 4. Metrics

- Task completion: **Yes / Partial / No**
- Completion time per task
- Number of hints required
- Ease of use (1-5)
- Usefulness (1-5)
- Confusion point and observed error
- Would use again: **Yes / Maybe / No**
- Improvement action linked to an FR requirement

### Acceptance Thresholds

- At least 80% completion across core tasks T01-T06.
- Average ease and usefulness of at least 4.0/5.
- No critical privacy or destructive-data issue.
- Every failed/partial task produces an owner and improvement action.

## 5. Testing Procedure

1. Start `prototype/server.py` and open the landing page.
2. Explain that the prototype and feedback are for class learning.
3. Assign an anonymous tester code and device type.
4. Ask the tester to complete tasks without guidance.
5. Give a hint only after the tester is stuck for 30 seconds; record it.
6. Record completion, time, comments, and observable problems.
7. Ask the tester to rate ease, usefulness, and willingness to reuse.
8. Remove any test upload that the participant does not want retained.
9. Convert findings into the prioritized final improvement list.

## 6. Evidence Sources

- `data/validation-results.csv`: 20 anonymized historical validation records.
- `docs/prototype-testing-notes.md`: earlier end-to-end prototype observations.
- `screenshots/user-testing-evidence.png`: Lab 13 evidence summary.
- `docs/user-testing-results.md`: current results and desk-based smoke verification.

## 7. Ethical Reminder

Participation is voluntary. Use aliases and anonymous tester IDs, avoid unnecessary personal data, explain how uploaded images will be stored, and accept only artwork the tester has the right to share.
