#Importing files 
import DateTime
from DRBcodes import library
    
l=library("Librarybook.txt","Islington Libary")
#Dictionary
press_key_list = {"D": "Displays the Book","B": "Borrows the Book","R": "Returns the Book","E": "Exits"}
#Booolean data type used
key_press = False
print("             A warm Welcome to the Library Management System       ")
print("-----------------------------------------------------------------------")
print("D: Displays the Book")
print("B: Borrows the Book")
print("R: Returns the Book")
print("E: Exits")
while not(key_press == "E"):
    for key,value in press_key_list.items():
        print("Press",key,"To",value)
    key_press = input("Press Key: ").upper()
    
    if key_press =="B":
        print("-----------------------------------------------------------------------------------")
        print(f"\t List of Books that you can borrow from the Library")
        print("-----------------------------------------------------------------------------------")
        print("Book ID   Book Name       Author    Price(Rs.)  Quantity")
        print("--------------------------------------------------------------")
        #display_book method called from class library
        l.display_books()
        print("Current Selection: Borrow Books")
        print("-------------------------------")
        #Borrow_books method called from class library
        l.Borrow_books()
        
    elif key_press == "D":
        print("Current Selection: Display Books")
        print("-------------------------------------------------------------")
        print("\t\tList of Books")
        print("-------------------------------------------------------------")
        print("Book ID   Book Name       Author    Price(Rs.)  Quantity")
        print("-------------------------------------------------------------")
        #display_book method called from class library
        l.display_books()
        
    elif key_press == "R":
        print("Current Selection: Return Books")
        print("-------------------------------")
        BookID=int(input("Enter the Book ID you want to return: "))
        yourname =input("Enter your name: ").upper()
        #return_books method called from class library
        l.return_books(BookID,yourname)
        
    elif key_press == "E":
        print("--------------------------------------------------------------")
        print("Thankyou for visiting! Hope you enjoyed our services")
        print("--------------------------------------------------------------")
        break
    
    else:
        print("-------------------------------")
        print("Invalid! Please check")
        print("-------------------------------")

