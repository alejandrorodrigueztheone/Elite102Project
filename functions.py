import mysql.connector


logged_in = False
mistake_counter = 0
def menu():
  print("Hello! Welcome to Ace Banking! ")
  if logged_in == False:
    account_num = input("Please enter your account number: ")
    account_password = input("Please enter your account password: ")
    bank_balance = input("Please enter you starting bank balance")
    sql = (f"""" INSERT INTO 'ace_banking'. 'account_info' ('Account_Number', 'Account_password', 'Balance') VALUES ('{account_num}', '{account_password}', '{bank_balance}');""")
    x = mydb.cursor()
    x.execute(sql)
    mydb.commit()
    print("We have successively created a new account for you!")
    logged_in = True
    menu()
  elif logged_in == True:
    action_ = input("Please choose what you want to do")
    if action_ == 1:
      deposit()
    elif action_ == 2:
      withdraw()




def deposit():
  if logged_in == True:
    account_ = input("Please enter the account number you want to use: ")
    amount_ = input('How much do you wish to deposit?: ')
    a = f"""" UPDATE account_info SET Balance = Balance+{amount_} WHERE Account_Number={account_} ; """}
    if account_ != account_num :
      if mistake_counter < 3:
        print("Oppsie, wrong number! Please try again! ")
        mistake_counter = mistake_counter +1
        deposit()
      elif mistake_counter == 3:
       print("You have made two many mistakes. The program will terminate and log you out")
        logged_in = False
        exit()

def withdrawal():
  if logged_in == True:
    account_ = input("Please enter the account number you want to use: ")
    amount_ = input('How much do you wish to withdraw?: ')
    a = f"""" UPDATE account_info SET Balance = Balance-{amount_ WHERE Account_Number={account_} ; """}
    if account_ != account_num :
      if mistake_counter < 3:
        print("Oppsie, wrong number! Please try again! ")
        mistake_counter = mistake_counter +1
        withdrawal()
      elif mistake_counter == 3:
        print("You have made two many mistakes. The program will terminate and log you out")
        logged_in = False
        exit()



menu()