'''
Driver file
To do:
    - allow searching of a greater number of common players
    - "vanity search" - highest damage differential:
    - incorporate STEAMID conversion (shouldn't require the API)
    - impose order on results
    - start to store player aliases, associated with IDs
    - write test
Tools:
Couple of urls:
http://logs.tf/profile/76561198055233348
http://logs.tf/profile/76561197993593754
'''
import player

# constants:
ID64_LENGTH = 17
MAX_PLAYERS = 12

# print title and link for logs common to players
def print_common_logs(players):
    num_of_players = len(players)
    if num_of_players > MAX_PLAYERS:
        raise RuntimeError("Too many players for now!")
    elif num_of_players == 0:
        print("No players, no logs.")
    else:
        for key in players[0].data['logs']:
            players_with_key = 1
            for i in range(1, num_of_players):
                if key in players[i].data['logs']:
                    players_with_key += 1
            if players_with_key == num_of_players:
                print(players[i].data['logs'][key]['title'])
                print("http://logs.tf/" + str(players[i].data['logs'][key]['id']))

def main():
    print("Hi! This script finds urls of logs common to up to 12 players.")
    print("Enter their logs.tf profiles, then enter 's' to search.")

    players = []
    steam_id_64 = 0

    # get and validate user input for ID
    while True:
        url_input = input("Enter player URL: ")
        if url_input == 's' or url_input == 'S':
            break
        # id64 will follow this signature:
        id_index = url_input.find("/profile/")
        if id_index == -1:
            print("Input not recognized. Please try again.")
            continue
        # get 17 digits following "/profile/"
        steam_id_64 = url_input[id_index + 9: id_index + 26]
        if len(steam_id_64) != 17:
            print("Input not recognized. Please try again.")
            continue
        else:
            p = player.Player(steam_id_64)
            players.append(p)

    print_common_logs(players)

if __name__ == "__main__":
    main()
