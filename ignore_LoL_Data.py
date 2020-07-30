import leaguepedia_parser
import os
import pandas
import time

regions = leaguepedia_parser.get_regions()  # fetch/define region names

official_tournaments = []  # container for official tournaments
official_games = []
desired_level = "Primary"  # list the tournament levels of interest
desired_year = ""
desired_patch = None

# iterate through regions
for region in regions:
    # check to see if "region" is blank
    if region not in "":
        # printing current progress
        print(
            "Currently processing region ",
            regions.index(region) + 1,
            "/",
            len(regions),
            ": ",
            region,
        )

        region_tournaments = leaguepedia_parser.get_tournaments(region)

        for tournament in region_tournaments:
            if type(tournament) is list:
                print("Had to split ", tournament[0]["name"])
                region_tournaments.remove(tournament)

                for x in tournament:
                    region_tournaments.append(x)

                continue

            if tournament["isOfficial"] is True:
                print(
                    region_tournaments.index(tournament) + 1,
                    "/",
                    len(region_tournaments),
                    " tournaments processed for ",
                    region,
                )

                tournament_games = leaguepedia_parser.get_games(
                    tournament["overviewPage"]
                )

                official_tournaments.append(tournament)
                official_games = official_games + tournament_games

                # for game in tournament_games:
                #     if game is not []:
                #         official_games.append(leaguepedia_parser.get_game_details(game))

print(
    len(official_games),
    " games processed for ",
    len(official_tournaments),
    " tournaments",
)

game_df = pandas.DataFrame.from_dict(official_games)
tournament_df = pandas.DataFrame.from_dict(official_tournaments)

game_df.to_sql("Official Games", Lv1_pro_games)
tournament_df.to_sql("Official Tournaments", Lv1_pro_games)
