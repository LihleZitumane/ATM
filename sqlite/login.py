import sqlite3
import datetime as dt


def Transactions(cursor, result):
	print("What do you want to do?" + "\n" + 
				"0 - Quit" + "\n" + 
				"1 - Balances" + "\n" +
				"2 - Withdrawal")
	number = input("Enter the number: ")
	if number == 1:
		balances = ("SELECT AccountNumber, AccountType,sum(tr.Amount) FROM Accounts acc LEFT JOIN Transactions tr ON tr.AccountID = acc.AccountID WHERE acc.ClientId = ? GROUP BY AccountType")
		cursor.execute(balances, [result[0][0]])
		result1 = cursor.fetchall()
		for i in result1:
			print(i)
		Transactions(cursor, result)
	elif number == 2:
		accountnumber = raw_input("Account number: ")
		currentbalance = ("SELECT tr.Amount FROM Accounts ac INNER JOIN Transactions tr ON tr.AccountID = ac.AccountID WHERE AccountNumber =?")
		AccountIDQuery = ("SELECT AccountID FROM Accounts WHERE AccountNumber = ?")
		cursor.execute(currentbalance, [accountnumber])
		result2 = cursor.fetchall()
		cursor.execute(AccountIDQuery, [accountnumber])
		resultAccountID = cursor.fetchall()
		AccountID = resultAccountID[0][0]
		balance = 0
		for i in result2:
			balance += i[0]
		print("Current balance "+ str(balance))
		amount = input("Amount: ")
		if amount > balance:
			print("Invalid amount")
		else:
			cursor.execute(("INSERT INTO Transactions (AccountID, Amount, Date) VALUES (?,?,?)"), [AccountID, -1*amount, dt.datetime.today()])
		Transactions(cursor, result)
	elif number == 0:
		print("bye")
	else:
		print("Invalid option")
		Transactions(cursor, result)



def login():
	while True:
		print("Login details please")
		name = raw_input("Name please: ")
		password = raw_input("PW please: ")
		with sqlite3.connect("mydb") as db:
			cursor = db.cursor()
			user = ("SELECT * FROM Clients WHERE Name = ? AND Password = ?")
			cursor.execute(user,[(name),(password)])
			result = cursor.fetchall()
		if result:
			print("passwords match!!")
			Transactions(cursor, result)
			break
		else:
			print("User not found")
			break
login()


