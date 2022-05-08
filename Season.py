import imp
from inspect import findsource
from Game import Game
from consts import gameConsts
from os import path

PROJECT_PATH = basepath = path.dirname(__file__)


class Season:
    def __init__(self, teamNameList, teamDetail):
        self.nameList = teamNameList
        self.teamDetail = teamDetail
        self.teamCount = len(teamNameList)
        self.standings = []
        self.createStandings(self.standings, teamNameList, teamDetail)
        self.schedule = []
        self.createSchedule(teamNameList)
        self.scoreLog = []
        self.rosters = [value["roster"] for value in teamDetail.values()]
        self.seasonStats = {}
        self.createSeasonStats(self.rosters)

    def createStandings(self, standings, teamNameList, teamDetail):
        teamCount = len(teamNameList)
        for i in range(teamCount):
            team = {
                "name": teamDetail[teamNameList[i]]["name"],
                "initial": teamNameList[i],
                "wins": 0,
                "losses": 0,
                "winRate": 0.0,
                "ranking": i + 1,
            }

            teamDetail[team["initial"]]["ranking"] = team["ranking"]
            standings.append(team)

    def createSchedule(self, teams):
        def findSpace(schedule):
            for i in range(len(schedule)):
                if schedule[i][0] == "":
                    return i

        self.schedule = [["", ""] for i in range(self.teamCount * (self.teamCount - 1))]
        gameNo = 0
        for i in range(self.teamCount - 1):
            idx = i + 1
            homeCount = 0
            while idx != self.teamCount:
                self.schedule[gameNo][homeCount % 2] = teams[i]
                self.schedule[gameNo][(homeCount + 1) % 2] = teams[idx]
                idx += 1
                gameNo += 2
                homeCount += 1

            idx -= 1

            while idx != i:
                self.schedule[gameNo][homeCount % 2] = teams[i]
                self.schedule[gameNo][(homeCount + 1) % 2] = teams[idx]
                idx -= 1
                gameNo += 2
                homeCount += 1

            gameNo = findSpace(self.schedule)

    def createSeasonStats(self, rosters):
        seasonStats = {}
        for roster in rosters:
            for player in roster:
                seasonStats[player] = {
                    "totalPoints": 0,
                    "gamesPlayed": 0,
                    "ppg": 0.0,
                    "totalAssists": 0,
                    "apg": 0.0,
                }

        self.seasonStats = seasonStats

    def simulateSeason(self):
        with open(path.join(PROJECT_PATH, "logFiles", "gameLogs.txt"), "w") as f:
            f.write("")

        for i in range(len(self.schedule)):
            homeInitial = self.schedule[i][0]
            awayInitial = self.schedule[i][1]
            rosters = [
                self.teamDetail[homeInitial]["roster"],
                self.teamDetail[awayInitial]["roster"],
            ]
            initials = (homeInitial, awayInitial)
            game = Game(rosters, initials, gameConsts)
            game.play()
            score = game.score
            self.scoreLog.append(
                str(homeInitial)
                + " "
                + str(score[0])
                + " - "
                + str(score[1])
                + " "
                + str(awayInitial)
            )

            homeStanding = self.standings[self.teamDetail[homeInitial]["ranking"] - 1]
            awayStanding = self.standings[self.teamDetail[awayInitial]["ranking"] - 1]

            if game.winner == 0:
                homeStanding["wins"] += 1
                awayStanding["losses"] += 1
            else:
                homeStanding["losses"] += 1
                awayStanding["wins"] += 1

            homeStanding["winRate"] = float(
                homeStanding["wins"] / (homeStanding["wins"] + homeStanding["losses"])
            )
            awayStanding["winRate"] = float(
                awayStanding["wins"] / (awayStanding["wins"] + awayStanding["losses"])
            )

            self.standings = sorted(
                self.standings, key=lambda team: team["winRate"], reverse=True
            )
            for i in range(len(self.standings)):
                self.standings[i]["ranking"] = i + 1
                self.teamDetail[self.standings[i]["initial"]]["ranking"] = i + 1

            self.addGameStats(game.stats.stats)

    def addGameStats(self, stats):
        for i in range(2):
            for player in stats[i].keys():
                stat = self.seasonStats[player]
                stat["totalPoints"] += stats[i][player]["points"]
                stat["gamesPlayed"] += 1
                stat["ppg"] = float(stat["totalPoints"]) / stat["gamesPlayed"]
                stat["totalAssists"] += stats[i][player]["assists"]
                stat["apg"] = float(stat["totalAssists"]) / stat["gamesPlayed"]

    def printStandings(self):
        i = 1
        for team in self.standings:
            print(
                "{}. ".format(i)
                + team["name"]
                + ":\t\t"
                + str(team["wins"])
                + "W"
                + "\t"
                + str(team["losses"])
                + "L"
                + "\t"
                + ".{}".format((str(float(team["winRate"]) * 1000)[:3]))
            )
            i += 1

    def printSchedule(self):
        print(self.schedule)

    def printGameScores(self):
        for score in self.scoreLog:
            print(score)

    def printSeasonStats(self):
        sortedList = sorted(
            self.seasonStats.items(),
            key=lambda k_v: float(k_v[1]["ppg"]),
            reverse=True,
        )
        idx = 1
        for k, v in sortedList:
            print(
                str(idx)
                + ". "
                + k
                + ":"
                + "\t"
                + "{:.1f}P".format(v["ppg"])
                + "\t{:.1f}A".format(v["apg"])
            )
            idx += 1
