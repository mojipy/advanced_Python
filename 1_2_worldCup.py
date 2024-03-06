"""
This script get the group stage results as:

2-2
2-1
1-2
2-2
3-1
2-1

 and gives:

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3

In the group stage, teams are ranked based on the following criteria: 
points earned, number of victories, and alphabetical order. 
The team with more points is placed higher, followed by the count of wins, 
and if necessary, the alphabetical order is considered.

Author: Mojtaba Hassanzadeh
Date: March 6, 2024
"""
teams = ['Iran', 'Spain', 'Portugal', 'Morocco']
table = {team:{'wins': 0, 'losses': 0, 'draws': 0, 'goal difference': 0, 'points': 0 } for team in teams}
matches = [['Iran','Spain'],
           ['Iran','Portugal'],
           ['Iran','Morocco'],
           ['Spain','Portugal'],
           ['Spain','Morocco'],
           ['Portugal','Morocco'],
]

def update_table(team1, team2, res):
    winner, loser = (team1, team2) if int(res[0]) > int(res[-1]) else (team2, team1) if int(res[0]) < int(res[-1]) else (None, None)
    draw = winner is None

    if not draw:
        table[winner]['wins'] += 1
        table[loser]['losses'] += 1
        goal_diff = int(res[0]) - int(res[-1])
        table[winner]['goal difference'] += goal_diff
        table[loser]['goal difference'] -= goal_diff
    else:
        table[team1]['draws'] += 1
        table[team2]['draws'] += 1

for i, match in enumerate(matches):
    result = input(f"Result for match {i + 1}: ")
    update_table(match[0], match[1], result)

for team in teams:
    table[team]['points'] = 3 * table[team]['wins'] + table[team]['draws']

print('table:', table)

sorted_table = dict(sorted(table.items(), key=lambda x: (-x[1]['points'], -x[1]['wins'], x[0])))

print('sorted table:', sorted_table)

for team, data in sorted_table.items():
    print(f"{team}  wins:{data['wins']} , loses:{data['losses']} , draws:{data['draws']} , goal difference:{data['goal difference']} , points:{data['points']}")


### optimized version

# class FootballTournament:
#     def __init__(self, teams):
#         self.teams = {team: {'wins': 0, 'losses': 0, 'draws': 0, 'goal difference': 0, 'points': 0} for team in teams}
#         self.matches = []

#     def add_match(self, team1, team2):
#         self.matches.append((team1, team2))

#     def update_table(self, team1, team2, result):
#         winner, loser = (team1, team2) if result[0] > result[-1] else (team2, team1) if result[0] < result[-1] else (None, None)
#         draw = winner is None

#         if not draw:
#             self.teams[winner]['wins'] += 1
#             self.teams[loser]['losses'] += 1
#             goal_diff = result[0] - result[-1]
#             self.teams[winner]['goal difference'] += goal_diff
#             self.teams[loser]['goal difference'] -= goal_diff
#         else:
#             self.teams[team1]['draws'] += 1
#             self.teams[team2]['draws'] += 1

#     def calculate_points(self):
#         for team in self.teams:
#             self.teams[team]['points'] = 3 * self.teams[team]['wins'] + self.teams[team]['draws']

#     def get_standings(self):
#         self.calculate_points()
#         sorted_table = dict(sorted(self.teams.items(), key=lambda x: (-x[1]['points'], -x[1]['wins'], x[0])))
#         for team, data in sorted_table.items():
#             print(f"{team}  wins:{data['wins']} , loses:{data['losses']} , draws:{data['draws']} , goal difference:{data['goal difference']} , points:{data['points']}")