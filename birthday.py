"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
today = datetime.today()

MN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

Name = input("What is your name? ")
MOB = input("What month were you born in? ")
DOB = input("What day were you born on? ")
YOB = input("What year were you born in? ")

if MOB == list(month_name)[10] and DOB == "31":
    print("You were born on Halloween!")
    
if today.month == MN.index(MOB)+1 and today.day == int(DOB):
    print("Happy birthday!")
    
if MN.index(MOB)+1 in [1, 2, 12]:
    print(Name, ", you are a winter baby")