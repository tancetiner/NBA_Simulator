# some imports


class Stats:
    def __init__(self, rosters, initials):
        self.rosters = rosters
        self.stats = []
        self.initials = initials
        self.createStats(self.stats, self.rosters)

    def createStats(self, stats, rosters):
        for i in range(2):
            roster = rosters[i]
            self.stats.append({})
            for n in range(len(rosters[i])):
                stats[i][roster[n]] = 0

    def scores(self, team, name, points):
        self.stats[team][name] += points

    def printStats(self):
        print("Box Score:")
        for i in range(2):
            print("\t" + self.initials[i])
            for key in self.stats[i].keys():
                print("\t" + key + ": " + str(self.stats[i][key]))
