#/usr/bin/env python
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
    db = connect() #connect to database
    db_cursor = db.cursor()
    query = "DELETE FROM players;"
    db_cursor.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect() #connect to database
    db_cursor = db.cursor() #added in to connect to database and execute cursor
    query = "SELECT COUNT(*) FROM players;" #using id as way to count players
    db_cursor.execute(query) #added in to execute query
    results = db_cursor.fetchone() #returns players by one line
    db.close() 
    if results:
    	return results[0] #returns count of players registered
    else:
    	return '0' #returns zero if no players are registered
#   query = SELECT COUNT(*) FROM players; #added in to test
#"SELECT COUNT(id) AS num from players";
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect() #connect to database
    db_cursor = db.cursor() #using cursor object to execute next command
    query = "INSERT INTO players(name) VALUES('%s');" % name #we want to pass name in % name as a string %s
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
#    standings = []
    db = connect()
    db_cursor = db.cursor()
    query = """SELECT players.id, players.name, count(m.winner) as wins, 
                    count(l.loser)+count(m.winner) as matches
                FROM players
                    LEFT JOIN matches as m
                        ON players.id = m.winner
                    LEFT JOIN matches as l
                        ON players.id = l.loser
                GROUP BY players.id
                ORDER BY wins;"""
    db_cursor.execute
    db.commit()
    
    #result = db_cursor.fetchall()
   
    #db = connect()
    #db_cursor = db.cursor()
    #query = "SELECT * FROM win_total";
    #db_cursor.execute(query)
    #win_total = db.cursor.fetchall()
    #db.close()
    #return win_total


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
#win_total = playerStandings()
db = connect()
db_cursor = db.cursor()
query = """SELECT players.id as id1, players.name as name1  
            FROM players, 
            matches WHERE players.id=matches.winner
              LEFT JOIN matches as n1
                 ON players.id = n.winner
              LEFT JOIN matches as i2
                 ON players.id = i.winner
            GROUP by players.id;"""
db.commit()

db.close()


#WHILE EXISTS('SELECT * FROM players WHERE id NOT IN'('SELECT player.winner FROM matches') AND id NOT IN ('SELECT player.loser FROM matches')); 
#i = 0 
#result = [] 
#other_player = None
#for player in win_total:
#	if (i % 2) == 0:
#		other_player = player
#	else:
#		pairs = (other_player[0], other_player[1], player[0], player[1])
#		result.append(pairs)
#	i += 1
#return standings
#OR for review
#    pairs = []
 #   while len(ranks) > 1:
 #       validMatch = checkPairs(tid,ranks,0,1)
 #       player1 = ranks.pop(0)
 #       player2 = ranks.pop(validMatch - 1)
 #       pairs.append((player1[0],player1[1],player2[0],player2[1]))

 #   return pairs
