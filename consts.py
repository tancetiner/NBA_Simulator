from rosters import *

gameConsts = {
    "numberOfPossessions": 2 * 100,
    "actionStrings": {
        "layupMade": ["{} goes for a layup... It's good!", "{} lays the ball in."],
        "layupMissed": [
            "{} goes for a layup... No good.",
            "{} couldn't lay the ball in.",
        ],
        "midrangeMade": [
            "{} from midrange... It's in!",
            "{} tries from midrange... Count that!",
        ],
        "midrangeMissed": [
            "{} from midrange... It's out.",
            "{} tries from midrange... Misses it.",
        ],
        "3made": ["{} for three... Bang!", "{} takes the three... Count that!"],
        "3missed": ["{} for three... No good.", "{} takes the three... Misses it."],
        "shotClockViolation": [
            "They couldn't shoot the ball! {} ball...",
            "It's a shot clock violation, great D by {}!",
        ],
        "shotBlocked": ["{}'s shot blocked by {}!", "{}'s shot is erased by {}!"],
        "steal": ["{} steals the ball from {}!", "{} picks {}'s pocket!"],
        "foul": ["{} is fouled by {}.", "{} gets the foul call. It's on {}."],
        "badPass": [
            "Bad pass by {}. {} ball.",
            "{} throws the ball out! {} possession.",
        ],
        "outOfBounds": [
            "{} steps out of bounds. {} ball.",
            "{}'s foot is on the line. {} ball.",
        ],
        "freeThrowMade": [
            "First free throw for {}. It's in.",
            "{} shoots the second one. Makes it.",
        ],
        "freeThrowMissed": [
            "First free throw for {}. It's not good.",
            "{} shoots the second one. No good.",
        ],
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
