'''
Driver file
To do:
  - fix get_id64 bug
  - Improve search for common games--radix/bucket-ish with duplicate checking?
  - Reverse print order more efficiently
  - allow searching of a greater number of common players
  - "vanity search" - highest damage differential:
    - incorporate STEAMID conversion (shouldn't require the API)
Tools:
Couple of urls:
http://logs.tf/profile/76561198055233348
http://logs.tf/profile/76561197993593754
'''
import player

# constants:
ID64_LENGTH = 17
MAX_PLAYERS = 2

def get_id64():
  
  while True:
    url_input = input("Enter player URL: ")
    id_index = url_input.find("/profile/")
    if id_index == -1:
      print("URL not recognized. Please try again.")
      continue
    steam_id_64 = url_input[id_index + 9: id_index + 26]
    if len(steam_id_64) != 17:
      print("URL not recognized. Please try again.")
      continue
    else:
      return steam_id_64
  
def print_common_logs(players):
  if len(players) > MAX_PLAYERS:
    raise RuntimeError("Too many players for now!")
  for i in reversed(players[0].data['logs']):
    for j in reversed(players[1].data['logs']):
      if i['id'] == j['id']:
        print(i['title'])
        print("http://logs.tf/" + str(i['id']))

def main():
  print("Hi! This script finds urls of logs common to two players.")
  print("You'll need to provide their two logs.tf pages:")
  
  players = []

  p1 = player.Player(get_id64())
  players.append(p1)
  p2 = player.Player(get_id64())
  players.append(p2)
    
  print_common_logs(players)

if __name__ == "__main__":
  main()
