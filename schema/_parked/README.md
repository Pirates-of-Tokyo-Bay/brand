# Parked schema

Schema for pages that are not live right now. Nothing in this folder should be
pasted into Squarespace until the page it belongs to is live again.

| File | Page | Why it is parked | Before you use it |
|---|---|---|---|
| `university.json` | `/university` | The page is paused. `/university` and `/improv-university` both 302 to `/info`, so there is no page for this markup to live on. | Un-pause the page first. Then check every date and price against the real cohort. |

## Note on `university.json`

The dates in this file are from the July 2026 draft:

- `validThrough: 2026-08-20`
- `startDate: 2026-08-27`
- `endDate: 2026-09-17`
- `availability: InStock`

Those describe a cohort that was planned but never ran. Google treats Course and
Offer markup that does not match the page as a violation, so do not publish this
until the dates are real.

The `FAQPage` node is fine to keep, but Google limited FAQ rich results to
government and health sites in August 2023, so it will not earn search snippets.
It is still worth keeping because AI answer engines read it.
