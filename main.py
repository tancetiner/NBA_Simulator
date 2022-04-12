from consts import teamNameList, teamDetail
from Season import Season

season = Season(teamNameList, teamDetail)
season.simulateSeason()
season.printLog()
print()
season.printStandings()
print()
season.printSeasonStats()
