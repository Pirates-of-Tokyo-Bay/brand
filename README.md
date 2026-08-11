# Pirates of Tokyo Bay / パイレーツ・オブ・東京湾

Brand, schema and show data for [Pirates of Tokyo Bay](https://www.piratesoftokyobay.com),
an English and Japanese improv comedy group in Tokyo. Performing monthly in Ebisu
since 2010.

**The style guide people read lives at
[piratesoftokyobay.com/styleguide](https://www.piratesoftokyobay.com/styleguide).**
This repository holds the things a web page is bad at holding: machine-readable
facts, versioned structured data, and real production data.

---

## What is here

| | |
|---|---|
| [`brand.json`](brand.json) | Every brand fact in one machine-readable file. Names, colors, font, venue, ticket price, and the phrasing rules below. Start here if you are building something. |
| [`press-kit.md`](press-kit.md) | For journalists, venues and partners. MC scripts in both languages, show length, technical needs, venue address, awards, logo links. Copy any of it. |
| [`press/`](press/) | One-page media fact sheets, August 2026: [日本語](press/factsheet-ja.md) / [English](press/factsheet-en.md), with print-ready A4 PDFs. |
| [`schema/`](schema/) | The JSON-LD we inject into Squarespace, one file per page, under version control. |
| [`shows/`](shows/) | 147 improv formats with language, cast size and how often we have actually played each one. Plus 78 shows of set list history. |
| [`handbook/`](handbook/) | Cast onboarding manual, including our framework for performing to a mixed-language room. |
| [`tools/`](tools/) | `assigner.py`, the script that builds our set lists. |
| [`scripts/`](scripts/) | `audit-schema.py`, which checks the schema files against our house rules. |

---

## The rules that matter most

If you take nothing else from this repository, take these. They apply to all
marketing, social media, press coverage and partner content.

### 1. Never write "bilingual" or「バイリンガル」

Not in titles, descriptions, captions, hashtags or spoken introductions.

The word suggests you need both languages to enjoy the show. You do not. Using it
turns away exactly the people who would have had the best night.

| Use this | Not this |
|---|---|
| English and Japanese improv comedy | Bilingual improv comedy |
| 日本語と英語で楽しめる即興コメディ | バイリンガル即興コメディ |

Better still, say the quiet part out loud: "No Japanese needed" /
「英語がわからなくても楽しめる」

### 2. Japanese first

In Japanese content, write 日本語 before English.
Correct: 日本語と英語で楽しめる即興コメディ

### 3. Half-width numbers in Japanese text

Correct: 2,500円（1ドリンク付）
Wrong: ２，５００円（１ドリンク付）

### 4. Link to `/shows`, never `/tickets`

`/tickets` redirects off-domain and leaks link equity.

---

## About the style

We aim to be simple but not simplistic, fun but not too funny.

Simplicity is not all we are after. We are a comedy group that plays public and
private shows and runs corporate workshops, so the brand should carry some of the
energy of the service. We do that through color, typography and form in design,
and through show structure on stage.

Our colors come from the festive parties of Mardi Gras: orange and gold up front,
with dark purple, light purple and warm gray supporting. Our font is **Zen Kaku
Gothic New**, a modern sans-serif that covers Japanese and English so both read as
one voice on every device.

Our vision is for everyone to laugh, whatever language they speak.

### Colors

| Color | Hex | RGB |
|---|---|---|
| Orange | `#f09a22` | 240, 154, 34 |
| Yellow Orange | `#f0c514` | 240, 197, 20 |
| Purple | `#8d52a1` | 141, 82, 161 |
| Dark Purple | `#794191` | 121, 65, 145 |
| Slate | `#343433` | 52, 52, 51 |
| White | `#ffffff` | 255, 255, 255 |

### Logo

Logo files, favicon and app icon are in
**[Google Drive](https://drive.google.com/drive/folders/0B-9s6txnzeMAfmNzYVpVMHkyQ3hKSWFJbFM1T29GRmxZZnZGd193bFRGZVJlUkxuOXEtVGM)**.

The logotype is custom drawn. The letterforms are based on traditional typefaces
with subtly contrasted stroke weight, and the "of Tokyo Bay" banner is a nod to
the flags pirates flew.

Large binary assets stay in Drive. This repository holds text and data.

---

## Come to a show

**What the Dickens!**, Roob 6 Bldg 4F, 1-13-3 Ebisunishi, Shibuya-ku, Tokyo
150-0021. Three minutes from JR Ebisu Station, one stop from Shibuya.

Monthly on Sunday evenings. 2,500円, first drink free.
Tickets and dates: [piratesoftokyobay.com/shows](https://www.piratesoftokyobay.com/shows)

🏆 Peatix Community Award 2026, Creative Arts Community, selected from more than
250 communities nationwide.

---

## Using our stuff

Take the press kit, the MC scripts, the colors and the logo and use them. That is
what they are for. Follow the four rules above and we are happy.

The show format library and the cast handbook are published for other improv
groups. If you run a show in a mixed-language city, take what is useful.

Questions: **info@japancomedy.com**
