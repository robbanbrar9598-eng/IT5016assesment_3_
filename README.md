# IT5016assesment_3_
Assessment 
Name: Robbandeep Singh Brar
Student ID: 20251168

Overview
This assignment shows how a simple requisition system for purchasing, which allows the staff member to input details like name, ID, date, price, and a unique ID generator for those who input the credentials, also a calculator, which calculates the total at the end, and displays whether the request is approved or pending. there are four functions staff_info(), requisitions_total(), requisition_approval(), and display_requisitions()
function details
In staff_info(), staff member input their data, like name, ID, date, and a requisition increments by 1 if details are entered. There is a while loop so that if another customer needs to add, then they can type yes, if not, then break, say no
requisitions_total().   After entering all the details, the system will prompt you to enter the item name, followed by the price. If the customer has more than one item, only the system will sum the cost of one cylinder. If there are different or multiple options, then it will sum all of them.
requisition_approval(). This function tells us the status, like approved or pending. if the total price is above 500, it will show pending if it is less than, approved will print the total and status. String and slicing methods are used in this function, and an if statement is also used.
display_requisitions(). This function collects all the data from the above functions and reports them as a summary.
There are some software design principles applied, like K.I.S.S, D.R.Y, 

Principle Implementation



