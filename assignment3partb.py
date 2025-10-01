"""My Name :- Robbandeep Singh Brar
   Srudent Id:- 20251168"""
"""                          Get HUb                                                                   """


# evey function is reusable so reuseability principle is also used 
# Reability and commenting principlr as it is easy to read and added comments to deails
1
def staff_info():  
    """this function Collect staff members details and to create a unique id 
    
    Principles implemented
    K.I.S.S: Simple loop to collect input.
    Single Responsibility: Only collects staff info.
    Separation of Concerns: Input is separated from calculations."""


    requisition_id= 10000              
    while True:
        
        date=input("enter the date : ")                          #enter date by staff
        staff_id=input("enter the staff id please : ")            #enter the id by staff
        staff_name=input("what is your name please enter it : ")      #enter the name 
        
        # generates unique requisition  id and each time increments when new staff member is added 
        requisition_id +=1        


                    # this  display collected data   

        print(f"Date = {date} ")            
        print(f" Staff ID = {staff_id}")   
        print(f"Your Name = {staff_name}")
        print(f"unique id = {requisition_id}")

                    # askin the staff member want to add another staff member 
        choice = input("Do you want to add another staff? (yes/no): ").lower() 



        if choice == "yes"  or choice == "no":           #K.I.S.S is used here in simple statement yes/no    
                            
                            # break helps to stop the loop from repeatind if staff says no
                            break
        




    return date,staff_id,staff_name,requisition_id

# 2


"""Collect items and their prices, calculate total requisition value.
    
    Principles implementes
    D.R.Y Use total variable to sum multiple items.
    Single Responsibility Only calculates total.
    
"""
def requisitions_total():                 
    date,staff_id,staff_name,requisition_id = staff_info()
    total = 0                                                         #D.R.Y principle as i have used used total to calculte all items at once
    while True:
        item = input("Enter item name (or 'done' to finish): ")   
        if item.lower() == "done":

            # stop the loop when type done

            break                
        
        """ Break statement is used there to break the 
        while loop even if it is true """

        price = int(input(f"Enter price of {item}: $"))   

        


        total += price  
        """total variable will represet the sum of particular staff member's all items price sum  as user as
            they had put price of their requireed items in price variable """
    
    print("\nTotal requisition value is: $", total)

    
    
    
    return date,staff_id,staff_name,requisition_id,total




# 3

"""this function determine approval for requisition status based on total.
    
    Principles implements
    K.I.S.S: used if condition total<500 if greater than it will be pending if below than approved which is simple logic 
    """
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




"""THIS function display the compelete summary of collected data.
    
    Principles implementated:
    
     Separation of Concerns: Only responsible for display"""


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



