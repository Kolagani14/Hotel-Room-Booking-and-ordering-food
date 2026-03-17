#Hotel Room Booking and ordering food
import random,string
import time
print("*********INSTRUCTIONS OF BOOKING ROOMS*********")
print("1:Enter your name with only alphabets")
print("2:Enter your phone number with only 10 digits")
print("3:Select the floor number from 1 to 3")
print("4:Select the room number from the available rooms")
print("5:Enter the time in HH:MM format")
print("6:You can order food items from the menu after booking the room")
print("7:extra hours will be charged 100 per hour after one hour free stay")
print("***********************************************")

count=0
print("Read the instructions carefully before booking the rooms")
for _ in range(3):   
    print(count)
    count+=1
    time.sleep(1)

print("*"*30)
print(" "*7,("Booking Slot"))
print("*"*30)
print("Bookings are open now!!!!")
B_Rooms=[]
items=[]
while True:
    Name=input("enter your name: ")
    if Name.isalpha():
         print("valid")
         break
    else:
         print("not valid")
         
while True:
        Phone = input("Enter your phone number: ")
        if Phone.isdigit() and len(Phone) == 10:
            break
        else:
            print("Enter a valid 10-digit phone number.")
letters=string.ascii_letters
digits=string.digits
OTP="".join(random.choices(letters+digits,k=8))
if OTP:
   print("OTP is successfully entered")
    
print("Books the Floor")
print("1:1st Floor")
print("2:2nd Floor")
print("3:3nd Floor")
while True:
    select_floor=input("Enter the Floor Number: ")
    if select_floor =="1" or select_floor =="2" or select_floor =="3":
        B_Rooms.append(select_floor)
        print("Floor ",select_floor," is selected")
        break
    else:
        print(select_floor," No more is there only limited")
        
while True:     
        print("1st floor rooms: ")
        print("101 :Abu Dhabi Room")
        print("102 :Arabs Room")
        print("2nd floor rooms: ")
        print("201 :Dallas Room")
        print("202 :Adias Room")
        print("3nd floor rooms: ")
        print("301 :Hots Room")
        print("302 :Sweets Room")

        select=input("Enter the Room Numbers:")      
        if select not in ( "101" ,"102" , "201" ,"202" ,"301","302"):
                        print("invalid room numbers" )
                        continue
        members=int(input("Enter the No of family mumbers: "))
        B_Rooms.append(members)
        B_Rooms.append(select)
        print( select,"Room  is seleted " )
        print(select_floor ,": Floor Number",":",select,":Room Number")
        print("Registered by :",Name.upper())
        break
while True:
    time=input("enter time: ")
    if ":" not in time:
        print("Invalid format. Use HH:MM")
        break
    h, m = time.split(":")

    if h.isdigit() and m.isdigit() and 0 <= int(h) < 24 and 0 <= int(m) < 60:
         break
    else:
        print("Invalid time values")
print("Time is successfully entered")


print("*"*30)
print(" "*10,"RECEIPT")
print("*"*30)
print("1.NAME: ",Name)
print("2.PHONE: ",Phone)
print("3.FLOOR NUMBER:",select_floor)
print("4.ROOM NUMBER",select)
print("successfully booked")
print("Have a nice day")
print("*"*30)

#its time to feast
while True:
    print("Food menu")
    print("1.Add items")
    print("2.read items")
    print("3.delete items")
    print("4.Exit the table")
    
    options=input("Enter yours options:")
    if options=="1":
        item=input("enter the item: ")
        items.append(item)
        print("item add succefully")
    
    elif options=="2":
        if item not in items:
            print("items are not availble")
        for i,item in enumerate(items,start=1):
            print(i,".",item)
    elif options=="3":
        if not  items:
            print("no items are not to delete")
        else:
            for i,item in enumerate(items,start=1):
                print(i,".",item)
            if items:
                n=int(input("enter the item number"))
                rem=items.pop(n-1)
                print("item was deleted:",rem)
            else:
                print("not valid")
    elif options == "4":
        print("bill please")
        print("we are off to the table")
    else:
        print("invalid choice")

#how much time spent
# one hour free and extra hours charged 100 per hour
    start_hour=int(input("enter the start hour: "))
    end_hour=int(input("enter the end hour: "))
    total_hours=end_hour - start_hour
    if total_hours <=1:
        print("your total bill is : 0")
    else:
                extra_hours=total_hours -1
                bill=extra_hours * 100
                print("your total bill is :",bill)               
                
                                