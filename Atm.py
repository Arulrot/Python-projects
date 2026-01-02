# import datetime
# import time
# card_pass_num=0000
# acc_bal=6500
# print("Arul Atm ")
# print("Insert the card")
# card_ins=int(input("press 1 to Insert card :"))
# if card_ins==1:
#         print("Please Wait Your transaction is under process !")
#         time.sleep(2)
#         card_pass=int(input("Enter your pssword :"))
#         time.sleep(0.5)
#         if card_pass==card_pass_num:
#             print("Password Accepeted ")
                
#             print('''
#                 1 - Balance 
#                 2 - withdrawal 
#                 3 - exit ''')
#             menuopt=int(input("Enter your option "))
#             if menuopt==1:
#                 print(acc_bal)
#             elif menuopt== 2:
#                 with_amt=int(input("Enter your Withdrawal amount :"))
#                 if with_amt>acc_bal:
                    
#                     print("insufficient Balance")
                   
#                 time.sleep(1)
#                 print("please Wait ...")
#                 time.sleep(2)
#                 print("Please collect your cash ")
#                 acc_bal=acc_bal-with_amt
#                 rec_menu=input("Do you want recipt ? y / n ")
#                 if rec_menu== 'y' :
#                     print("\n--- RECEIPT ---")
#                     print(datetime.datetime.now())
#                     print("Amount With drawn =",with_amt)
#                     print("remaining Balance =",acc_bal)
#                     time.sleep(2)   
#             elif menuopt==3:
#                 print("exit initiated ")
#             else:
#                 print("Wrong input ")
                
#             time.sleep(0.5)
#             print("Thank you for Banking With US ..")
#             time.sleep(1)
          
#         else:
#             print("Wrong Password ")
# else:
#     print("Card not inserted")
                
                
                
import time
import datetime

def withdraw(acc_bal):
    wdth_amt=int(input("Enter Withdrawal Amount :"))
    if wdth_amt>acc_bal:
        print("Insufficient Balance :")
    else :
        print("please wait ..")
        print("please collect your cash")
        acc_bal-=wdth_amt
        return acc_bal
        
def balance_check(acc_bal):
    print("Account balance is =",acc_bal)
    
    
def deposit(acc_bal):
    dep_amt=int(input("Enter the deposit Amount:"))
    print("Please Wait the amount is Being Deposited..")
    acc_bal+=dep_amt
    print("deposit Sucessfull")
    return acc_bal
    
def exit_init(session):
    print("Thank you for banking with Us .. ")
    session=False
    return session
    
    

def mechine_menu(acc_bal,session):
    print('''
          1-Cash Withdrawal 
          2-balance Enquiry
          3-deposit
          4-exit''')
    mechine_menu_int=int(input("Enter The Choice :"))
    if mechine_menu_int==1:
        acc_bal=withdraw(acc_bal)
       
    elif mechine_menu_int==2:
        balance_check(acc_bal)
        
    elif mechine_menu_int==3:
        acc_bal=deposit(acc_bal)
        
    elif mechine_menu_int==4:
        session=exit_init(session)
    return acc_bal, session 
        
    
    
def main():
    session=True
    try_counter=0
    card_pass=1234
    acc_bal=15000
    while session :
        
        print("Arul Atm ")
        print("insert your card ")
        print("Please with Your transcation in Processing")
        card_pass_check=int(input("Enter your card Password :"))
        if card_pass==card_pass_check:
            print("password Accepted")
            acc_bal,session=mechine_menu(acc_bal,session)
            
        else:
            print("incorrect password ")
            try_counter+=1
            if try_counter>=3:
                print("tries exceeded ..")
                print("card blocked ..")
                session=False
        

if __name__=="__main__":
    main()