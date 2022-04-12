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

    def play(self):
        overtimeCount = 0
        self.log += self.initials[0] + " - " + self.initials[1] + "\n"
        for i in range(self.possessionCount):
            pos = rd.randint(0, 9)
            player = rd.randint(0, 4)
            name = self.rosters[i % 2][player]
            if 0 <= pos <= 4:
                self.log += name + " " + self.actionStrings["shotMissed"] + "\n"
            elif 5 <= pos <= 8:
                self.score[i % 2] += 2
                self.stats.scores(i % 2, name, 2)
                self.log += (
                    name
                    + " "
                    + self.actionStrings["shotMade"]
                    + " "
                    + self.initials[0]
                    + " "
                    + str(self.score[0])
                    + " - "
                    + str(self.score[1])
                    + " "
                    + self.initials[1]
                    + "\n"
                )
            else:
                self.log += name + " " + self.actionStrings["shotMissed"] + "\n"

            if i % 50 == 0 and i != 0:
                self.log += "\nEnd of the {}. quarter".format(int(i / 50)) + "\n"

        while self.score[1] == self.score[0]:
            if overtimeCount != 0:
                self.log += "Overtime period {} is over!\n".format(overtimeCount)
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

            overtimeCount += 1
            self.log += "Overtime period {} starts!\n".format(overtimeCount)
            for i in range(16):
                pos = rd.randint(0, 9)
                player = rd.randint(0, 4)
                name = self.rosters[i % 2][player]
                if 0 <= pos <= 4:
                    self.log += name + " " + self.actionStrings["shotMissed"] + "\n"
                elif 5 <= pos <= 8:
                    self.score[i % 2] += 2
                    self.stats.scores(i % 2, name, 2)
                    self.log += (
                        name
                        + " "
                        + self.actionStrings["shotMade"]
                        + " "
                        + self.initials[0]
                        + " "
                        + str(self.score[0])
                        + " - "
                        + str(self.score[1])
                        + " "
                        + self.initials[1]
                        + "\n"
                    )
                else:
                    self.log += name + " " + self.actionStrings["shotMissed"] + "\n"

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

    def printLog(self):
        print(self.log)
        return

    def printStats(self):
        self.stats.printStats()

    def writeLog(self):
        with open(path.join(PROJECT_PATH, "logFiles", "gameLogs.txt"), "a") as f:
            f.write(self.log + "\n\n")
