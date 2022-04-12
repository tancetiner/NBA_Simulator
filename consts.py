from rosters import *

gameConsts = {
    "numberOfPossessions": 2 * 100,
    "actionStrings": {
        "shotMade": "shoots... Bang!",
        "shotMissed": "takes the shot... Misses it",
        "turnover": "turns the ball over!",
    },
}

seasonConsts = {"gameCount": 6}

teamNameList = [
    "LAL",
    "BKN",
    "BOS",
    "PHX",
    "HOR",
    "ATL",
    "MIA",
    "CHI",
    "UTA",
    "GSW",
    "PHI",
    "MIL",
]

teamDetail = {
    "LAL": {"name": "Los Angeles Lakers", "roster": lakersRoster},
    "BKN": {"name": "Brooklyn Nets", "roster": netsRoster},
    "BOS": {"name": "Boston Celtics", "roster": bostonRoster},
    "PHX": {"name": "Phoenix Suns", "roster": phoenixRoster},
    "HOR": {"name": "Chorlette Hornets", "roster": hornetsRoster},
    "ATL": {"name": "Atlanta Hawks", "roster": hawksRoster},
    "MIA": {"name": "Miami Heat", "roster": heatRoster},
    "CHI": {"name": "Chicago Bulls", "roster": bullsRoster},
    "UTA": {"name": "Utah Jazz", "roster": jazzRoster},
    "GSW": {"name": "Golden State Warriors", "roster": warriorsRoster},
    "PHI": {"name": "Philadelphia 76ers", "roster": sixersRoster},
    "MIL": {"name": "Milwaukee Bucks", "roster": bucksRoster},
}
