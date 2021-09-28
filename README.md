
## RTI CDS Backend Developer Exercise 01

This is the implementation of this backend developer exercise by Jose Quinones.
Each of the following sections go through what files are what, along with how to run them.

### SQL

The sql query used to combine the different tables in the database can be found in the file 'combine_tables.sql'
The table is named 'combined' in the sqlite database.
The combined table has also been output as a csv file to 'combined_data.csv'.


### Analysis
The base python script used for analysis on this data is 'analysis.py'. Make sure to create a new venv, activate it, and install requirements.txt via pip before running the analysis.py script. You may also have to install tkinter to view the chart during the script run, but it will be output to the file regardless (command would be something like this: 'sudo apt-get install python3-tk')

The different things analyzed include the following:
* Data count (number of rows)
* Rows with zero vs non-zero capital loss
* Missing data count for each column
* Percent distribution of countries
* A chart of marital status vs capital gain.

The output of this analysis will be primarily in console, with one bar graph being displayed and also saved as 'marital_status_vs_capital_gain.png'.


### Django App
A Django web app has also been created to display the same information as the 'analysis.py' script, which can be found in the exerciseDjangoProject folder. This has been Dockerized, and (assuming docker and docker-compose are both installed) can be run with 'docker-compose up' from the exerciseDjangoProject folder. Once the docker container is running, the app can be accessed at 'http://localhost:8000/'.

All the information is displayed in unstylized plain html for the sake of simplicity.
