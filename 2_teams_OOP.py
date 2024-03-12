"""
Object Oriented Programming

"It randomly divides 22 players into two teams, with each team having 11 players."


Author: Mojtaba Hassanzadeh
Date: March 11, 2024

"""

import random

# Parent class
class People: 
    def __init__(self, name):
        self.name = name

# This child class inherits "name" from the parent and has an extra attitude "team"
class Player(People): 
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team
    def assign_team(self, team):
        self.team = team

player_names = ['Hossein', 'Maziar', 'Akbar', 'Nima', 'Mahdi', 'Farhad', 'Mohammad', 'Khashayar', 'Milad', 'Mostafa', 'Amin', 'Saeid', 'Pouya', 'Poria', 'Reza', 'Ali', 'Behzad', 'Soheil', 'Behrooz', 'Shahrooz', 'Saman', 'Mohsen']
 
 # Create Objects
player_objects = [Player(name, None) for name in player_names] 

# Create teams        
random.shuffle(player_objects) 

# for player in player_objects[:11]:
#     player.assign_team('team_A')
[player.assign_team('team_A') for player in player_objects[:11]]

# for player in player_objects[11:]:
#     player.assign_team('team_B')
[player.assign_team('team_B') for player in player_objects[11:]]

# Display the teams
print("TEAM A:")
# for player in player_objects:
#     if player.team == 'team_A':
#         print('    ', player.name)
print([player.name for player in player_objects if player.team == 'team_A'])
print(*[player.name for player in player_objects if player.team == 'team_A'])

print("\nTEAM B:")
# for player in player_objects:
#     if player.team == 'team_B':
#         print('    ', player.name)
print([player.name for player in player_objects if player.team == 'team_B'], sep = '\n')
print(*['    ' + player.name for player in player_objects if player.team == 'team_B'], sep = '\n')
