-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament; -- removes old database (if applicable)
CREATE DATABASE tournament; -- adds new tournament database

\c tournament -- connects to tournament database

CREATE TABLE players (id SERIAL primary key, 
					name TEXT);
); /*id for the match, which will also be a primary key, and the name in text form*/

CREATE TABLE matches (id SERIAL primary key, 
					winner INTEGER REFERENCES players (id), 
					loser INTEGER REFERENCES players (id));
); /*id for players as a primary key, the winner, then loser in integer form and references the players table and id*/

-- views practice
/*example... CREATE VIEW v_americanLeague as
	select * from team 
	where league = 'National League';
	Then can say: select * from v_americanLeague
	
	where league = 'National League';
	Then can say: select * from v_americanLeague

/*example... 
	CREATE VIEW v_number_wins 
	AS
		SELECT players.id, COUNT(matches.winner) AS wins 
		FROM players left join matches
		ON players.id = matches.winner
		GROUP by players.id;

	CREATE VIEW v_number_played --- getting syntax error at CREATE VIEW???
	AS
		SELECT players.id, COUNT(matches.id) AS total from players
		FROM players left join matches 
			ON players.id
		GROUP by players.id;
	

*/
