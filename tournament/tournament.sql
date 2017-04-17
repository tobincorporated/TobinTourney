
CREATE TABLE players (id serial PRIMARY KEY, name text);


CREATE TABLE matches (round_num INTEGER, winner INTEGER REFERENCES players(id), 
                      loser INTEGER REFERENCES players(id));
                          
CREATE VIEW wins AS
    SELECT COUNT(matches.winner) AS num, players.id AS player FROM
    matches FULL OUTER JOIN players
    ON  matches.winner = players.id
    GROUP BY players.id
    ORDER BY num DESC;

CREATE VIEW losses AS
    SELECT COUNT(matches.loser) AS num, players.id AS player FROM
    matches FULL OUTER join players
    ON  matches.loser = players.id
    GROUP BY players.id
    ORDER BY num DESC;

CREATE VIEW scores AS 
    SELECT wins.player AS player, wins.num AS wins, losses.num AS losses, wins.num+losses.num AS tot_matches
    FROM wins FULL OUTER JOIN losses ON wins.player = losses.player 
    ORDER BY wins DESC;