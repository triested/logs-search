# logs-search
Search logs.tf for games common to two players

## Usage:
To run, enter the following in a terminal:

	$ python3 main.py
You'll need the [logs.tf](logs.tf) profiles of the players in question. When prompted, enter their urls. The script will print titles and links for games in which they appear together.

Note: the resulting list of logs is currently limited to the most recent 1000 games of __both__ players.

## Future Plans
    * web interface
    * searches using any reasonable number of users
    * search using multiple types of steam identifiers
