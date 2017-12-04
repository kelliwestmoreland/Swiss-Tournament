# Swiss-Tournament
## Project Submission

Developed a database schema to store the game matches between players. 
Used code to query this data and determine the winners of various games.

## Files: 
* `tournament.py` - defines functions necessary to run Swiss style tournament
* `tournament.sql` - SQL database structure necessary to for the tournament.
* `tournament_test.py` - Tests to evalute functions contained in tournament.py

## Systems:
* Github
* Virtual Box
* Vagrant
* Python
* psql 

## Procedure:
1. Login to vagrant using `vagrant up`
2. Login to VM using "vagrant ssh" (I had to modify it as a Windows 10 user with "winpty vagrant ssh")
3. Access vagrant folder using `cd/vagrant/tournament`
4. Access psql database using `psql -f tournament.sql`
5. Access python and import tournament using "python" and "import tournament"
6. Created database (also included `DROP` method to remove database if the same one was previously created, preventing errors)
7. Run `tournament_test.py` to test the tournament_test.py script to run the python script.

Additional comments within tournament.py and tournament.sql explains how the procedures and queries are run.
