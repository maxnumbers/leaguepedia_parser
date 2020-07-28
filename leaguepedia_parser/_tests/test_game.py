import leaguepedia_parser
from pprint import pprint
from leaguepedia_parser.transmuters.game import game_fields
import pandas as pd

regions_names = ["China", "Europe", "Korea"]
tournaments_overviews = [
    "LEC/2020 Season/Spring Season",
    "LCK/2020 Season/Spring Season",
    "LPL/2020 Season/Spring Season",
]


def test_regions():
    regions = leaguepedia_parser.get_regions()
    print(regions)

    assert all(region in regions for region in regions_names)


def test_tournaments():
    for region in regions_names:
        tournaments = leaguepedia_parser.get_tournaments(region, year=2020)

        for tournament in tournaments:
            print(tournament["overviewPage"])

            # test log prints tournament overview and tournament dict for region 1, tournament 1
            if tournaments[0] and regions_names[0]:
                pprint(tournament)

        assert len(tournaments) > 0


def test_games():
    for tournament_overview in tournaments_overviews:
        games = leaguepedia_parser.get_games(tournament_overview)

        if tournament_overview is tournaments_overviews[0]:
            pprint(games[0])

        assert len(games) > 0


def test_used_ScoreboardGames_fields():
    # starting w/ just scoreboard games, however should make it more robust and check all tables used
    url = "https://lol.gamepedia.com/Template:ScoreboardGames/CargoDec"
    match = "ScoreboardID_Wiki"

    used_ScoreboardGames_fields = leaguepedia_parser.transmuters.game.game_fields

    # grabs set of field names from the cargo template defined on Leaguepedia
    df = pd.read_html(url, match=match, index_col=1)[0]["N"]
    actual_ScoreboardGames_fields = set(df.to_dict().keys())

    unused_ScoreboardGames_fields = (
        actual_ScoreboardGames_fields - used_ScoreboardGames_fields
    )
    print(unused_ScoreboardGames_fields)

    assert len(unused_ScoreboardGames_fields) > 0


# def test_used_ScoreboardTeams_fields():
#     url = "https://lol.gamepedia.com/Template:ScoreboardTeams/CargoDec"


# def test_used_ScoreboardPlayers_fields():
#     url = "https://lol.gamepedia.com/Template:ScoreboardPlayers/CargoDec"


def test_get_details():
    for tournament_overview in tournaments_overviews:
        games = leaguepedia_parser.get_games(tournament_overview)

        # First, test without pageId
        leaguepedia_parser.get_game_details(games[0])

        # Then test with pageId
        game = leaguepedia_parser.get_game_details(games[0], True)

        if tournament_overview[0]:
            pprint(game)

        assert "picksBans" in game

        for team in "BLUE", "RED":
            assert len(game["teams"][team]["players"]) == 5
            for player in game["teams"][team]["players"]:
                assert "irlName" in player["uniqueIdentifiers"]["leaguepedia"]
                assert "birthday" in player["uniqueIdentifiers"]["leaguepedia"]
                assert "pageId" in player["uniqueIdentifiers"]["leaguepedia"]
