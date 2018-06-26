# ATM
This is a python written project. Console application that mimics an atm, using sqlite3 as a database engine

This is the process when you run the application:

1. Ask user for name and password to log on using the password in the database.
2. Ask the user what he wants to do: 
  a. See balances for all his accounts
  b. Withdraw money, ask which' account  and amount. Add the withdrawal entry into the transaction table so that when he asks for his balance it is updated correctly after the withdrawal.
  c. Quit the application
  
  The database that I created has 3 tables, Clients, Accounts and Transactions. Hence you can find login details in those tables. To see the data that is in those tables you can look at the csv files that I have uploaded in this repository.

