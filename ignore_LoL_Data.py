import leaguepedia_parser
import os
import pandas

regions = leaguepedia_parser.get_regions()  # fetch/define region names

official_tournaments = []  # container for official tournaments
official_games = []
desired_level = "Primary"  # list the tournament levels of interest
desired_year = ""
desired_patch = None

# iterate through regions
for region in regions:
    if region not in "":
        print((regions.index(region) + 1), "/", len(regions), " regions processed")

        region_tournaments = leaguepedia_parser.get_tournaments(region)

        for tournament in region_tournaments:
            if type(tournament) is list:
                region_tournaments.remove(tournament)

                print("Had to split ", tournament[0]["name"])
                for x in tournament:
                    region_tournaments.append(x)

                continue

            if tournament["isOfficial"] is True:
                print(
                    region_tournaments.index(tournament) + 1,
                    "/",
                    len(region_tournaments),
                    " tournaments",
                )

                tournament_games = leaguepedia_parser.get_games(
                    tournament["overviewPage"]
                )
                official_tournaments.append(tournament)

                for game in tournament_games if not []:
                    official_games.append(leaguepedia_parser.get_game_details(game))

print(
    len(official_games), " games processed, ", len(official_tournaments), " tournaments"
)

