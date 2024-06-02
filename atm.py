import time

print("Please Enter Your Pin.")

time.sleep(5)

password=1234
pin=int(input("Your Atm Pin = "))

balance=5000

if pin==password:
    while True:
        print("""
          1 == balance
          2 == withdraw balance
          3 == deposit balance
          4 == exit
          """
          )
        print("============================================================")
        print("============================================================")
        print("============================================================")
        try:
          option=int(input("Please Enter Your Choice = "))
          
        
        except:
          print("Please Enter Valid Option")
        if option==1:
          print(f"Your Current Balance is {balance}.")
          
          print("===========================================================")
          print("===========================================================")
          print("===========================================================")
        
        if option==2:
          withdraw_amount=int(input("Please Enter withdraw_amount = "))
        
          balance=balance-withdraw_amount  
          print("===========================================================")
          print("===========================================================")
        
          print(f"{withdraw_amount} is Debited from Your account.")  
        
          print(f"Your Current Balance is {balance}.")
          
          print("===========================================================")
          print("===========================================================")
          
        
        if option==3:
          deposit_amount=int(input("Please Enter deposit_amount = "))
        
          balance=balance+deposit_amount  
          print("===========================================================")
          print("===========================================================")
        
          print(f"{deposit_amount} is Credited from Your account.")  
        
          print(f"Your Updated Balance is {balance}")
          
          print("===========================================================")
          print("===========================================================")
        
    
        if option==4:
          break
    
    
else:
    print("Wrong Pin Please try Again")