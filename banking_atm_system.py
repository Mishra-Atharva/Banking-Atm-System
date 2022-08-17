#-------------------------------------------------------------------------------
# Name:        assignmentU3A1(part4).py
# Purpose:     Banking ATM
#
# Author:      Atharva Mishra
#
# Created:     11/11/2021
# Copyright:   (c) Atharva Mishra 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Loop for checking user entered password, if password is right they can continue with their banking if incorrect the program will stop.
def password():

	global user, login #added global becuase without this you can't check if user inputted the correct password in menu section. Also to update login value.
	for i in range(1, 4):
		user = input("Enter password: ")
		if user == "ABC123":
			print("")
			print("| Welcome to ABCB Banking! |")
			login = True #To allow user to skip login later when going back to menu.
			break
		elif user != "ABC123" and i < 3:
			print("Incorrect Password Entered: " + str(i) + ", " + "Re-enter the password!")
		elif user != "ABC123" and i == 3:
			print("Incorrect Password Entered: 3.")
			print("Your Account is temporarily suspended!")

#Deposite function is there to ask the user in what currency do they want to make a deposite and once they select the currency of their choice (HKD or USD) they choose which account do they want to make their deposite in.
#After picking the account they want to make a deposite in (savings or Chequing) they are asked the amount of moeny they want to deposite, after they have inputted their deposite account the function shows the updated balance of their account.
#After they have made the deposite they are asked wether they want to make another deposite or they don't (press 1 for yes and press 2 for No) if they pick 1 they are sent back to the currency selection menu, if they pick 2 the function displays a goodbye message and then quits.
#The while statements in the function is so when the user inputs an incorrect number (for example function asks press 1 for yes and 2 for no and user press 3) it will keep on asking the user the same prompt untill they input correct number.
def deposite():

	global savings, chequing
	print("")
	print("| Currency Select |")
	print("[1] HKD")	
	print("[2] USD")
	user_currency_deposite = int(input("Please enter a number: "))
	
	while user_currency_deposite != 1 and user_currency_deposite != 2:
		print("")
		print("| Currency Select |")
		print("[1] HKD")
		print("[2] USD")
		user_currency_deposite = int(input("Please enter a number: "))
	
	if user_currency_deposite == 1:
		print("")
		print("[1] Savings")
		print("[2] Chequing")
		user_deposite = int(input("Enter options: "))
		while user_deposite != 1 and user_deposite != 2:
			print("")
			print("[1] Savings")
			print("[2] Chequing")
			user_deposite = int(input("Enter options: "))
		
		if user_deposite == 1:
			user_savings_deposite = float(input("Enter the amount you want to deposite: "))
			savings += user_savings_deposite
			print("$"+ str(user_savings_deposite) + "HKD")
			print("Current Balance: $" + str(savings) + "HKD")
			user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				deposite()
			elif user_stay == 2:
				menu()
				return savings
		
		elif user_deposite == 2:
			user_chequing_deposite = float(input("Enter the amount you want to deposite: "))
			chequing += user_chequing_deposite
			print("$"+ str(user_chequing_deposite) + "HKD")
			print("Current Balance: $" + str(chequing) + "HKD")
			user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				deposite()
			elif user_stay == 2:
				menu()
				return chequing
	
	elif user_currency_deposite == 2:
		print("")
		print("[1] Savings")
		print("[2] Chequing")
		user_deposite = int(input("Enter options: "))
		while user_deposite != 1 and user_deposite != 2:
			print("")
			print("[1] Savings")
			print("[2] Chequing")
			user_deposite = int(input("Enter options: "))
		
		if user_deposite == 1:
			user_savings_deposite = float(input("Enter the amount you want to deposite: "))
			savings += (user_savings_deposite*7.8)
			print("$" + str(user_savings_deposite) + "USD")
			print("Current Balance: $" + str(savings) + "HKD")
			user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				deposite()
			elif user_stay == 2:
				menu()
				return savings
		
		elif user_deposite == 2:
			user_chequing_deposite = float(input("Enter the amount you want to deposite: "))
			chequing += (user_chequing_deposite*7.8)
			print("$" + str(user_chequing_deposite) + "USD")
			print("Current Balance: $" + str(chequing) + "HKD")
			user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another deposite? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				deposite()
			elif user_stay == 2:
				menu()
				return chequing

#Withdraw function is there to ask the user which account do they want to withdraw money from and if the user picks 1 they will withdraw the money from savings and if the user picks 2 they will withdraw the money from chequing.
#If the user exceeds the value that is in the account it isn't going to let them withdraw only if the user withdraw less than or the equal value that is in the account only then they will be able to withdraw.
#The while loops are to make sure if the correct value isn't inputted it keeps on asking the same prompt.
#After they have withdraw money they are asked wether they want to withdraw again or they don't (press 1 for yes and press 2 for No) if they pick 1 they are sent back to the savings and chequing selection menu, if they pick 2 the function displays a goodbye message and then quits.
def withdraw():

	global savings, chequing
	print("")
	print("| Withdraw Account Selection |")
	print("[1] Savings")
	print("[2] Chequing")
	user_withdraw = int(input("Enter options: "))

	while user_withdraw != 1 and user_withdraw != 2:
		print("")
		print("[1] Savings")
		print("[2] Chequing")
		user_withdraw = int(input("Enter options: "))

	if user_withdraw == 1:
		user_savings_withdraw = float(input("Enter the amount you want to withdraw: "))
		while user_savings_withdraw > savings:
			print("Withdraw amount excceds savings!")
			user_savings_withdraw = float(input("Enter the amount you want to withdraw: "))
		if user_savings_withdraw <= savings:
			savings -= user_savings_withdraw
			print("$"+ str(user_savings_withdraw) + "HKD")
			print("Current Balance: $" + str(savings) + "HKD")
			user_stay = int(input("Do you want to withdraw again? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to withdraw again? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				withdraw()
			elif user_stay == 2:
				menu()
				return savings

	elif user_withdraw == 2:
		user_chequing_withdraw = float(input("Enter the amount you want to withdraw: "))
		while user_chequing_withdraw > chequing:
			print("Withdraw amount excceds chequing!")
			user_chequing_withdraw = float(input("Enter the amount you want to withdraw: "))
		if user_chequing_withdraw <= chequing: 
			chequing -= user_chequing_withdraw
			print("$"+ str(user_chequing_withdraw) + "HKD")
			print("Current Balance: $" + str(chequing) + "HKD")
			user_stay = int(input("Do you want to withdraw again? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to withdraw again? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				withdraw()
			elif user_stay == 2:
				menu()
				return chequing

#Transfer function is for the user to be able to transfer their money from one account to another.
#If they press 1 its chequing to savings, if they press 2 its savings to chequing.
#When entering the transfer amount if it exceeds the amount stored in that account the computer displays a message saying Transfer amount excceed chequing amount! and then prompts them with how much do they want to transfer.
#The while loops are to make sure if the correct value isn't inputted it keeps on asking the same prompt.
#After they have transfered money they are asked wether they want to make another transfer or they don't (press 1 for yes and press 2 for No) if they pick 1 they are sent back to the savings and chequing selection menu, if they pick 2 then the function quits.
def transfer():

	global savings, chequing
	print("")
	print("| Transfer |")
	print("[1] Savings")
	print("[2] Chequing")
	user_transfer = int(input("Enter options: "))

	while user_transfer != 1 and user_transfer != 2:
		print("")
		print("[1] Savings")
		print("[2] Chequing")
		user_transfer = int(input("Enter options: "))
	if user_transfer == 1:
		user_savings_transfer = float(input("Enter the amount you want to transfer from chequing: "))
		while user_savings_transfer > chequing:
			print("Transfer amount excceds chequing amount!")
			user_savings_transfer = float(input("Enter the amount you want to transfer from chequing: "))
		if user_savings_transfer <= chequing:
			savings += user_savings_transfer
			chequing -= user_savings_transfer
			print("$"+ str(user_savings_transfer) + "HKD")
			print("Current Balance for savings: $" + str(savings) + "HKD")
			print("Current Balance for chequing: $" + str(chequing) + "HKD")
			user_stay = int(input("Do you want to make another transfer? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another transfer? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				transfer()
			elif user_stay == 2:
				menu()
				return chequing, savings
	elif user_transfer == 2:
		user_chequing_transfer = float(input("Enter the amount you want to transfer from chequing: "))
		while user_chequing_transfer > savings:
			print("Transfer amount excceds chequing value!")
			user_chequing_transfer = float(input("Enter the amount you want to transfer from chequing: "))
		if user_chequing_transfer <= savings:
			chequing += user_chequing_transfer
			savings -= user_chequing_transfer
			print("$"+ str(user_chequing_transfer) + "HKD")
			print("Current Balance for chequing: $" + str(chequing) + "HKD")
			print("Current Balance for savings: $" + str(savings) + "HKD")
			user_stay = int(input("Do you want to make another transfer? Press 1 - Yes, Press 2 - No: "))
			while user_stay != 1 and user_stay != 2:
				user_stay = int(input("Do you want to make another transfer? Press 1 - Yes, Press 2 - No: "))
			if user_stay == 1:
				transfer()
			elif user_stay == 2:
				menu()
				return chequing, savings

#The display procedure shows the current balance of both accounts. Once it display's the current balance in both account it takes the user back to the menu.
def display():

	global savings, chequing
	print("")
	print("| Current Bank Balance |")
	print("Savings: HKD $" + str(savings))
	print("Chequing: HKD $" + str(chequing))
	menu()

#The menu procedure is there to call different functions.
#First it calls the password procedure to check if the user enters the correct password, then it shows a menu which allows use to pick what they want to do.
#1. allows them to make a deposite by calling the deposite function.
#2. allows them to make a withdraw by calling the withdraw function.
#3. allows them to transfer their money from one account to another.
#4. allows them to see their current balance in both their account savings and chequing.
#5. allows for them to exit the program and the program prints Thank you for using ABCB banking services!.
def menu():

	global savings, chequing
	if login == False:
		password()
	if user == "ABC123":
		print("")
		print("| ABCB Banking |")
		print("[1] Deposite")
		print("[2] Withdraw")
		print("[3] Transfer")
		print("[4] Display current balnace")
		print("[5] Exit")
		user_menu = int(input("Enter optioin: "))
		while user_menu != 1 and user_menu != 2 and user_menu != 3 and user_menu != 4 and user_menu != 5:
			print("")
			print("| ABCB Banking |")
			print("[1] Deposite")
			print("[2] Withdraw")
			print("[3] Transfer")
			print("[4] Display current balnace")
			user_menu = int(input("Enter optioin: "))
		if user_menu == 1:
			deposite()
		elif user_menu == 2:
			withdraw()
		elif user_menu == 3:
			transfer()
		elif user_menu == 4:
			display()
		elif user_menu == 5:
			print("Thank you for using ABCB banking services!")

#Declaration of variables password, savings and chequing. 
set_password = "ABC123" # this was changed due to it conflicting with the password procedure. It made it so password procedure wasn't able to be called.
savings = 10000
chequing = 10000
login = False #added to help the user later on so once the user has entered the correct password they don't need to enter password again when going back to the menu.
menu()