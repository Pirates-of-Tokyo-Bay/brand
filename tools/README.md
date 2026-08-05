# Tools

Small scripts we actually use to run the group.

## `assigner.py`

Builds a show set list. It reads the game catalogue and a performer roster, then
assigns performers to games while balancing four things:

- who is available
- language fit, so a Japanese-heavy game does not land on an English-only cast
- who has already been assigned, so stage time spreads evenly
- preferred and disliked games, so nobody is pushed into a format they hate

### Running it

```bash
python3 assigner.py
```

It expects two CSV files in the working directory:

| File | What it is |
|---|---|
| `GameCatalogue.csv` | The game list. Use [`../shows/game-catalogue.csv`](../shows/game-catalogue.csv). |
| `PerformerProfile.csv` | Your roster. Copy [`performers.example.csv`](performers.example.csv) and fill in your own. |

```bash
cp ../shows/game-catalogue.csv GameCatalogue.csv
cp performers.example.csv PerformerProfile.csv
python3 assigner.py
```

No dependencies beyond the Python standard library.

### About `performers.example.csv`

This file is **made up**. Fake names, invented ratings.

Our real roster file rates named cast members on overall skill, English fluency,
Japanese fluency, singing and guessing. That is not going in a public repository,
and it should not go in yours either. Keep your real roster local and out of git.

The columns are:

| Column | Meaning |
|---|---|
| `Performer Name` | Display name |
| `Availability` | 1 to 5, higher means more available |
| `Overall` | 1 to 5 |
| `English Fluency` | 1 to 5 |
| `Japanese Fluency` | 1 to 5 |
| `Singing Skill` | 1 to 5 |
| `Guessing Skill` | 1 to 5 |
| `Preferred Games` | Comma separated game names |
| `Disliked Games` | Comma separated game names |
| `Assigned Count` | Running total, start at 0 |

> If you fork this, add `PerformerProfile.csv` to your `.gitignore` before you
> put real names in it.
