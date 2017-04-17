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
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")	
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")	
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) AS num FROM players;")
    numPlayers = 0
    if c.rowcount > 0:
        numPlayers= c.fetchall()[0][0]
    DB.close()
    return numPlayers


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players "
              "(name) VALUES (%s);" , (name,) )	
    DB.commit()
    DB.close()


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
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT scores.player, players.name, scores.wins, scores.tot_matches "
              "FROM scores FULL OUTER JOIN players ON scores.player = players.id "
              "ORDER BY scores.wins DESC;")	
    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT tot_matches "
              "FROM scores "
              "WHERE player =(%s) or player=(%s) "
              "ORDER BY tot_matches DESC;", (winner, loser))
    previous_round = int( c.fetchall()[0][0] )
    next_round = previous_round + 1
    
    c.execute("INSERT INTO matches "
              "(round_num, winner, loser) "
              "VALUES ( %s, (%s), (%s) );" , (next_round, winner, loser))
    DB.commit()
    DB.close()
 
 
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
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT players.id, players.name "
              "FROM players FULL OUTER JOIN scores "
              "ON players.id = scores.player "
              "ORDER BY scores.wins DESC;")
    players = [(row[0], row[1]) for row in c.fetchall()]
    DB.close()
    numPlayers = countPlayers()
    pairings = []
    for i in range(numPlayers/2):
        pairings.append((players[2*i][0], players[2*i][1],
                         players[2*i+1][0], players[2*i+1][1]))
    return pairings