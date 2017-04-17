# Zachary Tobin's Tournament Results Database
### by Zachary Tobin

## Description
A database system that runs a Swiss Pairing-sytle tournament.
It has the following features:
* Players can be added to the database.
* Players' standings can be polled.
* Player count can be checked.
* Players can be paired based on the Swiss Pairing style.
* Match outcomes can be recorded.
* Tournament data can be cleared.

## Installation and running
1. The database can be run in a Vagrant an environment. You can find installation instructions for Vagrant and Virtual Box on [Udacity's website.](https://classroom.udacity.com/nanodegrees/nd004/parts/af045689-1d81-46e7-8a3b-ad05de1142ce/modules/353202897075460/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0). 
2. Instead of using the Vagrant Configuration provided by Udacity, download and use this repository.
3. To create the tournament database and its associated relations, first open your command line console (as suggested in the Udacity example) in this repository's folder (TobinTourney).
4. Enter the following commands:
    1. $ vagrant up
    2. $ vagrant ssh  
         *(Command Line will change to Vagrant)*
    3. $ cd /vagrant/tournament
    4. $ psql -c "create database tournament;"
    5. $ psql tournament  
         *(Command Line will change to PostreSQL command line)*
    6. => \i tournament.sql 
    7. => \q  
         *(Command line will change back to Vagrant)*
5. You may then access the database files through Python by importing the *tournament.py* file. 
    An example file is included, python tournament_test.py.


## License
This code released under the [MIT License](https://choosealicense.com/licenses/mit)
