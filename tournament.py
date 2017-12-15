#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect() #connect to database
    db_cursor = db.cursor() #create a cursor to execute the command
    query = "DELETE FROM matches;" #SQL query with what the action will be, this one is deleting
    db_cursor.execute(query)#the line to execute the query
    db.commit() #must commit to execute the delete action
    db.close() #close the connection

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect #connect to database
    db_cursor = db.cursor()
    query = "DELETE FROM players;"
    db_cursor.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect() #connect to database
    db_cursor = db.cursor() #added in to connect to database and execute cursor
    query = "SELECT COUNT(id) AS num from players"; #using id as way to count players
    db_cursor.execute(query) #added in to execute query
    results = db_cursor.fetchone() #returns players by one line
    db.close() 
    if results:
    	return results[0] #returns count of players registered
    else:
    	return '0' #returns zero if no players are registered
#   query = SELECT COUNT(*) FROM players; #added in to test
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect() #connect to database
    db_cursor = db.cursor() #using cursor object to execute next command
    query = "INSERT INTO players(name) VALUES('%s');" % name
    db_cursor.execute#("INSERT INTO players(name) VALUES(%s)", (name,))
    db.commit() #commit to execut the insert function
    db.close() #close database connection

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    standings = []
    db = connect()
    db_cursor = db.cursor()
    query = ("""SELECT players.id, name, count(matches.id) AS num 
                FROM players LEFT JOIN matches \
                ON players.id = matches.winner
                ORDER BY players.id""");
    db_cursor.execute
    db.commit()
    result = db_cursor.fetchall()

#    query = "SELECT * FROM players;"
 #   db_cursor.execute(query)
#    player_id = db_cursor.fetchall()
    #for row in db_cursor.fetchall():
#    for i in range(len(players.id)):
 #   	standings.append((row[0], str(row[1]), row[2], row[3])) #returns tuples of id, name, wins, matches
    db.close()
    return standings
    #OR
    #standings = db.cursor.fetchall()
    #db.close()
    #return standings



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    db_cursor = db.cursor()
    db_cursor.execute("INSERT into games VALUES (%s,%s);" (winner, loser)) #executes outcome of single match between two players
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
standings = playerStandings()

i = 0 
result = [] 
other_player = None
for player in standings:
	if (i % 2) == 0:
		other_player = player
	else:
		pairs = (other_player[0], other_player[1], player[0], player[1])
		result.append(pairs)
	i += 1
#OR for review
#    pairs = []
 #   while len(ranks) > 1:
 #       validMatch = checkPairs(tid,ranks,0,1)
 #       player1 = ranks.pop(0)
 #       player2 = ranks.pop(validMatch - 1)
 #       pairs.append((player1[0],player1[1],player2[0],player2[1]))

 #   return pairs
