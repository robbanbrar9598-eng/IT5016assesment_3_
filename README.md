---------------------------------------------------------# IT5016assesment_3_------------------------------------------------------------------------


                                                              Assessment 


                                                          Name: Robbandeep Singh Brar


                                                            Student ID: 20251168

-------------------------------------------------------------------Overview------------------------------------------------------------------------


This assignment shows how a simple requisition system for purchasing, which allows the staff member to input details like name, ID, date, price, and make unique ID g for those who input the credentials, and there is  also a calculator, which calculates the total at the end, and displays whether the request is approved or pending. there are four functions staff_info(), requisitions_total(), requisition_approval(), and display_requisitions()


---------------------------------------------------------------------------function details----------------------------------------------------------


**In staff_info(), staff member input their data, like name, ID, date, and a requisition increments by 1 if details are entered. There is a while loop so that if another customer needs to add, then they can type yes, if not, then break, say no.


**requisitions_total().   After entering all the details, the system will prompt you to enter the item name, followed by the price. If the customer has more than one item, only the system will sum the cost of one cylinder. If there are different or multiple options, then it will sum all of them.


**requisition_approval(). This function tells us the status, like approved or pending. if the total price is above 500, it will show pending if it is less than, approved will print the total and status. String and slicing methods are used in this function, and an if statement is also used.


**display_requisitions(). This function collects all the data from the above functions and reports them as a summary.
There are some software design principles applied, like K.I.S.S, Single Responsibility, Separation of Concerns, Clean Code, Open/Closed, Single Responsibility, and D.R.Y


----------------------------------------------------------------Principle Implementation-----------------------------------------------------------------


1.K.I.S.S (Keep It Simple, Stupid): Simple loops and conditions for clarity

2.D.R.Y (Don’t Repeat Yourself): Reused variables for total calculation

3.Single Responsibility: Each function performs one specific task

4.Separation of Concerns: Input, calculation, and display are handled separately




--------------------------------------------------------------------All Principles--------------------------------------------------------------------------


1. K.I.S.S:- In this principle, codes are simple to understand and straightforward. Through this principle, we can stop avoiding unnecessary complexity. If the  code is simple, we understand it more.
   there are 2 function in which K.I.S.S is implement. line 23 of caltex, papaura, where the program simply manages  the loop, which avoids other work, for example,
   in these codes:-
  #  choice = input("Do you want to add another staff? (yes/no): ").lower()
  
        if choice == "yes"  or choice == "no":           #K.I.S.S is used here in a simple statement yes/no    
                            
                            # break helps to stop the loop from repeating if staff says no
                            break
   

In requisition_total()from 64  lines,  i had simply applied a true statement to keep it simple and break the loop by typing done.

 if item.lower() == "done":

            # stop the loop when type done

            break                
        
        The break statement is used there to break the 
        while loop even if it is true """
This is simple because if the customer types done, they exit the loops.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

2. D.R.Y:- To avoid the repeating logic and make it into a single position. this will help when a person need to make a change, if D.R.Y principle is applied, they would only need to change it from one place only.
In requisition_total(), the total variable accumulates all the prices of items repeatedly entered by the staff. This helps to avoid rewriting additional code multiple times



    total = 0                                                        
    while True:
        item = input("Enter item name (or 'done' to finish): ")   
        if item.lower() == "done":
            break                
        price = int(input(f"Enter price of {item}: $"))   
                   total += price


      
-----------------------------------------------------------------------------------------------------------------------------------------------------------------          
3. Single Responsibility:- This principle tells that a class or module should only have 1 responsibility, meaning it performs only one function. This helps to avoid the different concerns and makes it more effective. 

Single Responsibility is implemented in multiple functions, like:-
staff_info()
requisitions_total()
display_requisitions()
These function has their own purposes.

staff_info() collects only data from staff members.
requisitions_total() only sums up all the items staff enter.
display_requisitions() only displays the summary or report.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Separation of Concerns:- In this principle, the program is divided into different sections, which makes it easy to handle and secure from overlapping responsibilities. This helps to make the code more readable.

for instance:-
 staff_info:- only handels input from staff.
 requisition _total:- only performs calculations 
 display_requisition:- print out the output

 ---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------Conclusion---------------------------------------------------------------------


In conclusion, there is a requisition system which is developed by using software principles such as K.I.S.S., D.R.Y., Single Responsibility, and Separation of Concerns, to make the code simpler, more modular. These principles had not only made code better but also increased its reusability and made it more effective.  Every function has its unique quality, and software principles help to embrace them



