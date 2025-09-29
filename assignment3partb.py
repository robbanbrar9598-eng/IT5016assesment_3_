"""My Name :- Robbandeep Singh Brar
   Srudent Id:- 20251168"""
"""                          Get HUb                                                                   """


# evey function is reusable so reuseability principle is also used 
# Reability and commenting principlr as it is easy to read and added comments to deails

def staff_info():  
    requisition_id= 10000              
    while True:
        
        date=input("enter the date : ")                          
        staff_id=input("enter the staff id please : ")            
        staff_name=input("what is your name please enter it : ")
        
        requisition_id +=1                       

        print(f"Date = {date} ")            
        print(f" Staff ID = {staff_id}")   
        print(f"Your Name = {staff_name}")
        print(f"unique id = {requisition_id}")

                    
        choice = input("Do you want to add another staff? (yes/no): ").lower() 



        if choice == "yes"  or choice == "no":           #K.I.S.S is used here as exicting loop is very simple     
                            break
        




    return date,staff_id,staff_name,requisition_id
#staff_info()
from task1 import*
def requisitions_total():                 
    date,staff_id,staff_name,requisition_id = staff_info()
    total = 0                                                         #D.R.Y principle as i have used used total to calculte all items at once
    while True:
        item = input("Enter item name (or 'done' to finish): ")   
        if item.lower() == "done":
            break
        
        """ Break statement is used there to break the 
        while loop even if it is true """

        price = int(input(f"Enter price of {item}: $"))   

        


        total += price  
        """total variable will represet the sum of particular staff members all items price sum  as user as
            they had put price of their requireed items in price variable """
    
    print("\nTotal requisition value is: $", total)

    
    
    
    return date,staff_id,staff_name,requisition_id,total
requisitions_total()
from task2 import*
def requisition_approval():                
    date,staff_id,staff_name,requisition_id,total = requisitions_total() 
    
    
    status = "Pending"     
    approval_ref = None

    if total < 500:     #K.I.S.S principle is used

        """here we have make a condition that total is less than 500 than mark the status approved 
            and also use a < operator which help the computer to know grater or less than """        
        
        status = "Approved"
        last_three = str(requisition_id)[-3:]  
        approval_ref = staff_id + last_three
    
    
    print("\nRequisition Summary")
    print("Total: $", total)
    print("Status:", status)
    if approval_ref:
        print("Approval Reference Number:", approval_ref)
    
    return date,staff_id,staff_name,requisition_id,total,status,approval_ref
requisition_approval()
from task3 import*
def display_requisitions():

    date,staff_id,staff_name,requisition_id,total,status,approval_ref = requisition_approval()
    
    print("\nPrinting Requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $", total)
    print("Status:", status)
    if approval_ref:
        print("Approval Reference Number:", approval_ref)
display_requisitions()

