import random as rd
from Stats import Stats
from os import path

PROJECT_PATH = basepath = path.dirname(__file__)


class Game:
    def __init__(self, rosters, initials, consts):
        self.rosters = rosters
        self.actionStrings = consts["actionStrings"]
        self.possessionCount = consts["numberOfPossessions"]
        self.log = ""
        self.initials = initials
        self.score = [0, 0]
        self.stats = Stats(rosters, self.initials)
        self.winner = 0
        self.overtimeCount = 0

    def gameloop(self, i):
        pos = rd.randint(1, 110)
        player = rd.randint(0, 4)
        name = self.rosters[i % 2][player]
        assisted = rd.randint(1, 100) <= 24
        if assisted:
            assistName = self.rosters[i % 2][player]
            while assistName == name:
                assistName = self.rosters[i % 2][rd.randint(0, 4)]
        if 1 <= pos < 8:
            player2 = rd.randint(0, 4)
            name2 = self.rosters[(i + 1) % 2][player2]
            self.log += self.actionStrings["steal"][rd.randint(0, 1)].format(
                name2, name
            )
        elif 8 <= pos < 11:
            self.log += self.actionStrings["badPass"][rd.randint(0, 1)].format(
                name, self.initials[(i + 1) % 2]
            )
        elif 11 <= pos < 14:
            self.log += self.actionStrings["outOfBounds"][rd.randint(0, 1)].format(
                name, self.initials[(i + 1) % 2]
            )
        elif pos == 14:
            self.log += self.actionStrings["shotClockViolation"][
                rd.randint(0, 1)
            ].format(self.initials[(i + 1) % 2])
        elif 15 <= pos < 37:
            self.score[i % 2] += 2
            self.log += (
                self.actionStrings["layupMade"][rd.randint(0, 1)].format(name)
                + " "
                + self.scoreString()
                + " "
            )
            self.stats.scores(i % 2, name, 2)
            if assisted:
                self.stats.assists(i % 2, assistName)
                self.log += self.actionStrings["assist"][rd.randint(0, 2)].format(
                    assistName
                )
        elif 37 <= pos < 49:
            self.log += self.actionStrings["layupMissed"][rd.randint(0, 1)].format(name)
        elif 49 <= pos < 55:
            self.score[i % 2] += 2
            self.log += (
                self.actionStrings["midrangeMade"][rd.randint(0, 1)].format(name)
                + " "
                + self.scoreString()
                + " "
            )
            self.stats.scores(i % 2, name, 2)
            if assisted:
                self.stats.assists(i % 2, assistName)
                self.log += self.actionStrings["assist"][rd.randint(0, 2)].format(
                    assistName
                )
        elif 55 <= pos < 63:
            self.log += self.actionStrings["midrangeMissed"][rd.randint(0, 1)].format(
                name
            )
        elif 63 <= pos < 75:
            self.score[i % 2] += 3
            self.log += (
                self.actionStrings["3made"][rd.randint(0, 1)].format(name)
                + " "
                + self.scoreString()
                + " "
            )
            self.stats.scores(i % 2, name, 3)
            if assisted:
                self.stats.assists(i % 2, assistName)
                self.log += self.actionStrings["assist"][rd.randint(0, 2)].format(
                    assistName
                )
        elif 75 <= pos < 96:
            self.log += self.actionStrings["3missed"][rd.randint(0, 1)].format(name)
        elif 96 <= pos < 101:
            player2 = rd.randint(0, 4)
            name2 = self.rosters[(i + 1) % 2][player2]
            self.log += self.actionStrings["shotBlocked"][rd.randint(0, 1)].format(
                name, name2
            )
        else:
            player2 = rd.randint(0, 4)
            name2 = self.rosters[(i + 1) % 2][player2]
            self.log += (
                self.actionStrings["foul"][rd.randint(0, 1)].format(name, name2) + "\n"
            )
            for n in range(2):
                foul = rd.randint(0, 99)
                if foul < 77:
                    self.score[i % 2] += 1
                    self.log += (
                        self.actionStrings["freeThrowMade"][n].format(name)
                        + " "
                        + self.scoreString()
                    )
                    self.stats.scores(i % 2, name, 1)
                else:
                    self.log += self.actionStrings["freeThrowMissed"][n].format(name)

                if n == 0:
                    self.log += "\n"

        self.log += "\n"

        if i % 50 == 0 and i != 0:
            self.log += "End of the {}. quarter".format(int(i / 50)) + "\n\n"

            if i != 200:
                self.log += "{}. quarter takes off!\n".format(int(i / 50) + 1)

    def play(self):
        for i in range(self.possessionCount):
            self.gameloop(i)

        while self.score[1] == self.score[0]:
            if self.overtimeCount != 0:
                self.log += "Overtime period {} is over!\n".format(self.overtimeCount)
                self.log += "Score is {}".format(
                    self.initials[0]
                    + " "
                    + str(self.score[0])
                    + " - "
                    + str(self.score[1])
                    + " "
                    + self.initials[1]
                    + "\n\n"
                )

            self.overtimeCount += 1
            self.log += "Overtime period {} starts!\n".format(self.overtimeCount)
            for i in range(16):
                self.gameloop(i)

        if self.score[1] > self.score[0]:
            self.winner = 1

        self.log += "\nEnd of the game\n"

        self.log += (
            "Score: "
            + self.initials[0]
            + " "
            + str(self.score[0])
            + " - "
            + str(self.score[1])
            + " "
            + self.initials[1]
            + "\n"
        )

        self.writeLog()

    def scoreString(self):
        return (
            self.initials[0]
            + " "
            + str(self.score[0])
            + " - "
            + str(self.score[1])
            + " "
            + self.initials[1]
        )

    def printLog(self):
        print(self.log)
        return

    def printStats(self):
        self.stats.printStats()

    def writeLog(self):
        with open(path.join(PROJECT_PATH, "logFiles", "gameLogs.txt"), "a") as f:
            f.write(self.log + "\n\n")
