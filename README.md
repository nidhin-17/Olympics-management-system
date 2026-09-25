# Olympics Player Management System

A simple command-line tool for managing Olympic athlete records. You can add players, search for them, update their medal counts, remove them, and pull up leaderboards for top players and top countries — all backed by a plain CSV file, no database needed.

## What this is

I built this for the VITyarthi "Build Your Own Project" submission. The idea was to take some core programming concepts — file handling, CSV I/O, modular functions, sorting and aggregation — and apply them to something concrete: tracking Olympic medal data and turning it into rankings.

It's menu-driven. Run `main.py`, pick a number from the menu, the app does its thing, and it keeps looping until you decide to quit.

## Features

- **Add Player** (`playeradd.py`) — Adds a new player (id, name, country, event, medals) and works out their points automatically. Won't let you add a duplicate player ID.
- **Search Player** (`searchplayer.py`) — Look up a player by ID and see their full record.
- **Update Prize** (`prizeupdation.py`) — Add new medals to an existing player and recalculate their points.
- **Remove Player** (`removeplayer.py`) — Delete a player record by ID.
- **View Top Players** (`topplayer.py`) — Ranks everyone from highest to lowest points.
- **View Top Countries** (`country.py`) — Rolls up medals and points by country and ranks them.

Points are calculated as: `(gold × 5) + (silver × 3) + (bronze × 1)`

## Built with

- Python 3
- Just the standard library — `csv` and `os`, nothing fancy
- `olympics.csv` as the data store
- Git / GitHub for version control

## Project layout

```
olympics-management-system/
├── main.py              # menu controller / entry point
├── playeradd.py         # add player
├── searchplayer.py      # search player
├── prizeupdation.py     # update medals/points
├── removeplayer.py      # remove player
├── topplayer.py         # top players leaderboard
├── country.py           # top countries leaderboard
├── olympics.csv          # data file (created automatically if missing)
├── diagrams/             # architecture, workflow, UML & schema diagrams
├── statement.md          # problem statement & scope
└── README.md
```

## CSV format

Each row in `olympics.csv` is one player:

```
player_id, player_name, country, item, gold, silver, bronze, points
```

## Getting it running

You'll need Python 3.7+.

1. Clone it:
   ```bash
   git clone https://github.com/<your-username>/olympics-management-system.git
   cd olympics-management-system
   ```
2. Optionally create an empty data file first (the app will create it for you if you skip this):
   ```bash
   type nul > olympics.csv        # Windows
   touch olympics.csv             # macOS / Linux
   ```
3. Run it:
   ```bash
   python main.py
   ```
4. Pick an option from the menu (1–6). After each action it'll ask if you want to continue — type `yes` to keep going, anything else exits.

## How to test it

No test framework needed, just walk through it manually:

1. Add two or three players from different countries with different medal counts.
2. Search for one of the IDs you just added and check the record comes back right.
3. Update a player's medals and confirm the points recalculate correctly.
4. Check the top players view — should be sorted highest to lowest.
5. Check the top countries view — medals and points should be aggregated properly per country.
6. Remove a player, then confirm they're gone from search and both leaderboards.
7. Enter an invalid menu option (like `9`) — it should show an error and bring the menu back up, not crash.
8. Try searching or removing a player ID that doesn't exist — it should say so cleanly instead of throwing an error.

## Docs

The `diagrams/` folder has the architecture, workflow, use case, class/component, and sequence diagrams along with the data schema. The problem statement and scope are in `statement.md`.

## What I'd add next

- Swap CSV for SQLite so it handles concurrent access and data integrity better
- Proper input validation (no negative medals, no garbage input)
- Unit tests with `pytest`
- Maybe a GUI or web frontend instead of the console menu

## Author

Built for the VITyarthi *Build Your Own Project* coursework.
