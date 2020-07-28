[![Generic badge](https://img.shields.io/github/workflow/status/mrtolkien/leaguepedia_parser/Python%20application)](https://shields.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Leaguepedia Parser

A parser for Leaguepedia focused on accessing esports data, which largely keeps game data in the [community-defined LoL DTO format](https://github.com/mrtolkien/lol_dto).

It's very minimal at the moment and focused on my own usage of Leaguepedia’s data.
Pull requests to add features are more than welcome! (See ["Contributing"](https://github.com/mrtolkien/leaguepedia_parser#Contributing))

# Install

`pip install leaguepedia_parser`

# Demo

![Demo](leaguepedia_parser_demo.gif)

# Usage

````python
import leaguepedia_parser

# Gets a list of region names as strings:
regions = lpp.get_regions()

# Gets a list of tournament dictionaries for a region, by default only returns primary tournaments:
tournaments = lpp.get_tournaments("Korea", year=2020)

# Gets a list of game dictionaries for a tournament, name comes from lpp.get_tournaments()[x]['OverviewPage']
games = lpp.get_games("LCK 2020 Spring")

# Gets a dictionary of picks/bans, gold, kills, and other details from a game, game comes from lpp.get_games()[x]
game = leaguepedia_parser.get_game_details(games[0])

# Gets a string of the URL to the team’s logo
logo_url = leaguepedia_parser.get_team_logo('T1')
```

More usage examples can be found in the [\_tests folder](https://github.com/mrtolkien/leaguepedia_parser/tree/master/leaguepedia_parser/_tests).

# Contributing

**To Do List:**

- Add more fields/functions from [Leaguepedia tables](https://lol.gamepedia.com/Special:CargoTables). These are commented as `#TODO` in transmuter/parser files
- Add functions to export or write data directly to SQL/SQLite3/CSV/R using pandas
- Potentially find a way to import information on plates taken, and to whom the gold was distributed

**General Philosopy:**

- We try to adhere to the [Google JSON Style Guide](https://google.github.io/styleguide/jsoncstyleguide.xml?showone=Property_Name_Format#Property_Name_Format)
- We use [black](https://pypi.org/project/black/) formatting
- Ensure that all tests on the latest master branch are passing on yours
  - We only use pytest for testing in the repo, so if you'd like to add new tests please also use pytest ([examples in \_tests folder](https://github.com/mrtolkien/leaguepedia_parser/tree/master/leaguepedia_parser/_tests))

**Adding-to/modifying functions:**

- Information should be input as close as possible to the objects it refers to
  - Player-specific information is directly under player objects
  - Team-wide information is directly under team objects
- Field names are coherent and comply with modern LoL nomenclature
  - Every field that is an identifier ends with id
  - Fields like cs or monstersKilled use current game vocabulary (as of June 2020)
  - All durations from the game start are expressed in seconds

Thanks for your interest! :D
````
