lakersRoster = [
    "Russell Westbrook",
    "Malik Monk",
    "Talen Tucker",
    "LeBron James",
    "Anthony Davis",
]

netsRoster = ["Kyrie Irving", "Seth Curry", "Joe Harris", "Ben Simmons", "Kevin Durant"]

bostonRoster = [
    "Marcus Smart",
    "Derrick White",
    "Jaylen Brown",
    "Jayson Tatum",
    "Robert Williams",
]

phoenixRoster = [
    "Chris Paul",
    "Devin Booker",
    "Mikal Bridges",
    "Jae Crowder",
    "Deandre Ayton",
]


def strToRoster(str):
    roster = str.split(" ")
    temp = [(roster[i] + " " + roster[i + 1]) for i in range(len(roster)) if i % 3 == 1]
    return temp


rosters = [
    "PG LaMelo Ball SG Terry Rozier SF Miles Bridges PF P. Washington C Mason Plumlee",
    "PG Trae Young SG Kevin Huerter SF DeAndre Hunter PF Danilo Gallinari C Clint Capela",
    "PG Kyle Lowry SG Duncan Robinson SF Jimmy Butler PF P.J. Tucker C Bam Adebayo",
    "PG Lonzo Ball SG Alex Caruso SF Zach LaVine PF DeMar DeRozan C Nikola Vucevic",
    "PG Mike Conley SG Donovan Mitchell SF Bojan Bogdanovic PF Royce O'Neale C Rudy Gobert",
    "PG Stephen Curry SG Klay Thompson SF Andrew Wiggins PF Draymond Green C Kevon Looney",
    "PG Tyrese Maxey SG James Harden SF Matisse Thybulle PF Tobias Harris C Joel Embiid",
    "PG Jrue Holiday SG Grayson Allen SF Khris Middleton PF Giannis Antetokounmpo C Brook Lopez",
]


hornetsRoster = [
    "LaMelo Ball",
    "Terry Rozier",
    "Miles Bridges",
    "P. Washington",
    "Mason Plumlee",
]
hawksRoster = [
    "Trae Young",
    "Kevin Huerter",
    "DeAndre Hunter",
    "Danilo Gallinari",
    "Clint Capela",
]
heatRoster = [
    "Kyle Lowry",
    "Duncan Robinson",
    "Jimmy Butler",
    "P.J. Tucker",
    "Bam Adebayo",
]
bullsRoster = [
    "Lonzo Ball",
    "Alex Caruso",
    "Zach LaVine",
    "DeMar DeRozan",
    "Nikola Vucevic",
]
jazzRoster = [
    "Mike Conley",
    "Donovan Mitchell",
    "Bojan Bogdanovic",
    "Royce O'Neale",
    "Rudy Gobert",
]
warriorsRoster = [
    "Stephen Curry",
    "Klay Thompson",
    "Andrew Wiggins",
    "Draymond Green",
    "Kevon Looney",
]

sixersRoster = [
    "Tyrese Maxey",
    "James Harden",
    "Matisse Thybulle",
    "Tobias Harris",
    "Joel Embiid",
]

bucksRoster = [
    "Jrue Holiday",
    "Grayson Allen",
    "Khris Middleton",
    "Giannis Antetokounmpo",
    "Brook Lopez",
]
