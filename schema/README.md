# Site schema / 構造化データ

Version control for the JSON-LD we inject into Squarespace.

## Why this folder exists

Squarespace code injection has **no version history**. If a schema block breaks,
there is no diff and no rollback. You find out from Google Search Console weeks
later and then guess at what changed.

This folder fixes that. One file per page. Git gives you the diff and the history.

A real example: our organization `sameAs` list pointed at
`https://github.com/PiratesOfTokyoBay` for months. That account does not exist and
returns a 404. It was sitting inside the same list as our Wikipedia, Wikidata and
Google Maps links, quietly weakening the entity cluster those links exist to
build. It was live on every page that carried our schema. A diff would have caught
it the day it was introduced.

## How to use it

**These files are the source of truth.** The live site should match them, not the
other way around.

1. Edit the JSON here first.
2. Run the audit: `python3 scripts/audit-schema.py`
3. Paste into Squarespace, page by page: **Page Settings → Advanced → Page Header
   Code Injection**, wrapped in `<script type="application/ld+json">` tags.
4. Verify with Google's Rich Results Test.
5. Commit.

## What is in here

| File | Page |
|---|---|
| `about.json` | `/about` |
| `audition-info.json` | `/audition-info` |
| `blog.json` | `/blog` |
| `business.json` | `/business` |
| `contact.json` | `/contact` |
| `faq.json` | `/faq` |
| `framework.json` | `/framework` |
| `friends.json` | `/friends` |
| `giftcard.json` | `/giftcard` |
| `group-management-kit.json` | `/group-management-kit` |
| `guests.json` | `/guests` |
| `improv-resources.json` | `/improv-resources` |
| `info.json` | `/info` |
| `linestamps.json` | `/linestamps` |
| `live-comedy.json` | `/live-comedy` |
| `media.json` | `/media` |
| `private-shows.json` | `/private-shows` |
| `schedule.json` | `/schedule` |
| `shows.json` | `/shows` |
| `sponsors.json` | `/sponsors` |
| `styleguide.json` | `/styleguide` |
| `training.json` | `/training` |
| `_parked/` | Pages that are not live. See [`_parked/README.md`](_parked/README.md). |

`index.json` maps each page to its SEO title and description.

## House rules

These are what `scripts/audit-schema.py` checks.

1. **One organization identity.** Every `PerformingGroup` or `Organization` node
   that is us uses `"@id": "https://www.piratesoftokyobay.com/#organization"`.
   Anonymous org nodes create a second competing entity and waste the `sameAs`
   list.
2. **Correct GitHub URL.** `github.com/Pirates-of-Tokyo-Bay`, with hyphens.
   `github.com/PiratesOfTokyoBay` is a 404.
3. **Japanese first.** `"inLanguage": ["ja", "en"]`, never `["en", "ja"]`.
4. **No banned words.** The word "bilingual" and バイリンガル must not appear in
   any schema text. See [`../brand.json`](../brand.json) for why.
5. **HTTPS only.** No `http://www.piratesoftokyobay.com` anywhere.
6. **FAQ topics belong to one page.** Do not repeat the same `FAQPage` questions
   across pages. It causes duplicate FAQPage errors in Search Console.

## Known gaps

- `/nextshow` declares `canonical: https://www.piratesoftokyobay.com`, so it tells
  Google to index the homepage instead of itself, while still appearing in the
  sitemap. Decide which one you want.
- `/shows`, `/business`, `/styleguide` and `/faq` are live and indexable but are
  not listed in `sitemap.xml`. Squarespace builds the sitemap from the navigation
  structure, so check whether they are sitting in the Not Linked section.
- Google limited `FAQPage` rich results to government and health sites in August
  2023. Our FAQ markup will not earn snippets, but AI answer engines still read
  it, so it is worth keeping.
