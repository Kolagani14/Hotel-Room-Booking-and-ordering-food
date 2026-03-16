#Role Of The Seller In Grocery Shop
import datetime
import time
while True:      
   Total=0

   while True:
      shopping = input("🗣 : Have you completed the shopping Sir(👱‍♂️)/Madam(👱‍♀️)(yes/no): ")
      if shopping == "yes" or shopping == "YES" and shopping == "no":
         print("🗣 : Give me your items")

         print("customer 👨 : ")
         
         customer= "Taking out our items....."
         for _ in range(5):
            print(customer)
            time.sleep(1)


         print("🗣 : please wait a mintue Sir(👱‍♂️)/Madam(👱‍♀️)")
         

         print("🗣 : your name please Sir(👱‍♂️)/Madam(👱‍♀️)")
      else:
         print("🗣 : okay please continue the shopping Sir(👱‍♂️)/Madam(👱‍♀️)")
         print("🗣 : Next customer please")
         print("🗣 : your name please Sir(👱‍♂️)/Madam(👱‍♀️)")


      print("-"*50)
      print("Description : Enter The Details")
      print("-"*50)
      
      Name     = input("💻 : enter the customer name : ")
      Quantity = int(input("💻 : Enter the no. of quantities : "))
      Amount   = int(input("💻 : Enter the total amount : "))
      
      Total += Quantity*Amount

      print("-"*50)
      print("Total amount of you purchased items : ", Total)
      print("-"*50)

      Enquiry = input("🗣 : Do you need to continue the shopping yes/no : ")
      
      if Enquiry == "yes" or Enquiry == "yes" and Enquiry == "no" or Enquiry == "NO":
         print("🗣 : please continue the shopping")
         break
      else:
         print("-"*5,"Take Your Receipt","-"*5)
         print("customer name : ", Name)
         print("Total amount : ", Total)
         x = datetime.datetime.now()
         print(x,x.strftime("%A"))

         print("-"*5,"Thank You ","-"*5)

         print("*"*5,"Have a nice day","*"*5)

         print("🗣 : Next Customer please")

   

      Seller_Decision = input("👨💭 : can you go for the next customer yes/no : ")
      if Seller_Decision == "no"  or Seller_Decision == "no" and Seller_Decision=="yes" :
          print("This counter is closed for some time")
          print("Go for next counter, Thank you")
      
      else:
         print(" Yes go for next customer..💭👨 ")
         print("Next customer Please....")
         
       



      
      
      


    