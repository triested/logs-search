# logs-search
Search logs.tf for games common to up to 12 players

## Usage:
To run, enter the following in a terminal:

	$ python3 main.py
You'll need the [logs.tf](logs.tf) profiles of the players in question. When prompted, enter their urls, then enter "s" to search. The script will print titles and links for games in which they appear together.

Note: the resulting list of logs is currently limited to the most recent 1000 games of __all__ players.

## Future Plans
    * web interface
    * remove 1000 game limit
    * search using multiple types of steam identifiers
