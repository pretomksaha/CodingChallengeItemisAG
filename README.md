# CodingChallengeItemisAG
It's a coding challenge given by  itemis Ag. Three problems  
1: SALES TAXES .  
2: CONFERENCE TRACK MANAGEMENT.  
3: MERCHANT'S GUIDE TO THE GALAXY

## Problem 1: SALES TAXES
Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical
products that are exempt. Import duty is an additional sales tax
applicable on all imported goods at a rate of 5%, with no exemptions. When I purchase items
I receive a receipt which lists the name of all the items and their price (including tax),
finishing with the total cost of the items,
and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax
rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of
sales tax.

## Problem 2: CONFERENCE TRACK MANAGEMENT
You are planning a big programming conference and have received many proposals which
have passed the initial screen process but you're having trouble fitting them into the time
constraints of the day -- there are so many possibilities! So you write a program to do it for
you.

## Problem 3: MERCHANT'S GUIDE TO THE GALAXY
You decided to give up on earth after the latest financial collapse left 99.99% of the earth's
population with 0.01% of the wealth. Luckily, with the scant sum of money that is left in your
account, you are able to afford to rent a spaceship, leave earth, and fly all over the galaxy to
sell common metals and dirt (which apparently is worth a lot).
Buying and selling over the galaxy requires you to convert numbers and units, and you
decided to write a program to help you.
The numbers used for intergalactic transactions follows similar convention to the roman
numerals and you have painstakingly collected the appropriate translation between them.

Problem description in details on the following pdf:  https://github.com/pretomksaha/CodingChallengeItemisAG/blob/master/Coding%20challenge%20itemis.pdf

# Solutions for the problems \
main() method call all of the other methods to solve the three problem. \
## option to choose \
\
Select the problem you want to solve: \
	<li>Problem 1: SALES TAXES </li>
	<li>Problem 2: CONFERENCE TRACK MANAGEMENT </li> 
	<li>Problem 3: MERCHANT'S GUIDE TO THE GALAXY </li>
	<li>4.exit</li>
Put a input number according to your choose:\
\
inpurList() methods have two fuction.\
takeInput(): Function take input values in list.\
findInput():Function to take file location and convert input as list.\
selcet the way want to give inputs for problems:\
\
Do you want manual input?\
Type yes or no:\
\
Problem 1: SALES TAXES\
salesTaxes() has three funcions.\
initialize(): Function to Initialize the solution for sales taxes problem.\
itemize():categories item in food, book, medicine and others product section.\
taxes(): Funtion to split every item and price then calculate the sales taxes and total price.\
\
Problem 2: CONFERENCE TRACK MANAGEMENT \
conferenceTrack() has three function.\
initialize(): function to Initialize the solution for conference track management problem.\
progarmSchedule(): Function that spite the time from every line and call the function to creat schedule.\
timeSchedle(): Function that assign every program in time and print a copy.\
\
Problem 3: MERCHANT'S GUIDE TO THE GALAXY\
merchantGuide() has five functions.\
initialize(): Function that initialize the mercants guide problem.\
separateConditions(): Function to separate condition according their structure.\
valueAssassin(): Function to assign credit to the metal according Roman Letter.\
calculateCredit(): Function to calculate the credits for the questions in the input list.\
searchValue(): Function to search credit for non assign metal.
