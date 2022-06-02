#Importing DateTime 
import DateTime
#Importing os for absolute path
import os
""" A library class is created to keep record of books present in library.
It has total three functions: 'display_books', 'Borrow_book' and 'return_books'
"""
class library():
    #__init__ method called when an object is created from the class
    def __init__(self,Librarybook,Libraryname):
           self.Librarybook = Librarybook
           self.Libraryname = Libraryname
           #dictionaries
           self.dictionarylender={}
           self.dictionary = {}
           #lists
           self.list = []
           self.listlender=[]
    #display_book method is defined for displaying books present in library.       
    def display_books(self):
        s=open(self.Librarybook, "r")
        for line in s:
            #strip() removes spaces
            a=line.strip()
            #split() returns a list of the words in the line
            b=a.split("\t")
            self.list.append(b)
        s.close()
        for i in range(len(self.list)):
            #update() method inserts the specified items to the dictionary
            self.dictionary.update({int(self.list[i][0]):[self.list[i][1],self.list[i][2],int(self.list[i][3]),(self.list[i][4])]})
        x=open(self.Librarybook)
        #readlines reads the line 
        p=x.readlines()
        for i in p:
            print(i)
        x.close()
        
    #Borrow_books method is defined for borrowing the books present in library  
    def Borrow_books(self):
        a="YES"
        ct=0
        Total=0
        while(a.upper()== 'YES'):
            #Infinite loop used
            while True:
                #try and except used to handel exception caused by program.
                try:
                    BookID = int(input("Enter the Book ID you want to borrow from the Library: "))
                    break
                except:
                    print("Please enter a no.")
            #Counter used to check the program is running or not
            if(ct==0):
                yourname = input("Enter your name: ").upper()
            

            list1=[]
            s=open(self.Librarybook, "r")
            for line in s:
                a=line.strip()
                b=a.split("\t")
                #append() method adds a single item to the existing list
                self.list.append(b)
            s.close()
            BookName = self.list[BookID-1][1]
            Price = self.list[BookID-1][3]
            for i in range(len(self.list)):
                #update() method inserts the specified items to the dictionary
                self.dictionary.update({int(self.list[i][0]):[self.list[i][1],self.list[i][2],self.list[i][3], int(self.list[i][4])]})
            if BookID in self.dictionary.keys():
                if self.dictionary[BookID][3]>=1:
                    #functions from DateTime file is used 
                    borrowDate = DateTime.getDate()
                    borrowTime = DateTime.getTime()
                    #absolute path is given
                    lender=os.path.abspath("LendersName/lender-("+yourname+")"+".txt")
                    with open (lender,"a") as x:
                        if (ct==0):
                            #writelines used for writing provided lines in txt file
                            x.writelines(f"\tLibrary Management System\n\n")
                            x.writelines(f"Date:{borrowDate}\t\t\tTime:{borrowTime}\n\n")
                            x.writelines(f"Borrower Name:{yourname}\n\n")
                            x.writelines("-------------------------------------------------------------------------------------\n")
                            x.writelines(f"BookID\t|\tBookName\t|\tPrice\n")
                            x.writelines("-------------------------------------------------------------------------------------\n")
                        x.writelines(f"{BookID}\t|\t{BookName}\t|\tRs.{Price}\n")
                        x.writelines("-------------------------------------------------------------------------------------\n")
                        
                        Total+=int(Price)
                    #append() method adds a single item to the existing list    
                    self.listlender.append([BookID,yourname,borrowDate])
                    list1=self.dictionary.get(BookID)
                    list1[3] -= 1
                    self.dictionary[BookID]=list1
                    #open and close Librarybook.txt file
                    f = open(self.Librarybook, "w")
                    f.close()
                    with open(self.Librarybook,"w") as y:
                        for key,value in self.dictionary.items():
                            y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
                    print("---------------------------------------------------------------------------------")
                    print(f"{yourname} you have sucessfully borrowed the Book with Book ID : {BookID} ")
                    print(f"So, {yourname} you have to pay Rs.{Price} for Book: {BookName}")
                    print("---------------------------------------------------------------------------------")
                else:
                    print("----------------------------------------------------------------")
                    print("Sorry! The book you are searching is currently out of stock.")
                    print("----------------------------------------------------------------")
            else:
                print("The ID doesnot match with Books.")
                
            a=input("Do you want to borrow more books?(Yes or No)")
            ct += 1
        lender=os.path.abspath("LendersName/lender-("+yourname+")"+".txt")
        with open (lender,"a") as x:
                x.write("Total Price: " + str(Total))
        a="NO"        
        while (a.upper() == 'NO'):
            print("----------------------------------")
            print("Thankyou for borrowing books.")
            print("----------------------------------")
            break

    #return_books method used for returning books that has been borrowed from library    
    def return_books(self,BookID,yourname):
        #absolute path determined
        lender=os.path.abspath("LendersName/lender-("+yourname+")"+".txt")
        #try except used for handeling exception caused in the program 
        try:
            with open(lender,"r") as f:
                lines=f.readlines()
                lines=[lender.strip() for lender in lines]
            """with open(lender,"r") as f:
                data=f.read()"""
        except:
            print("--------------------------------------------")
            print("The book has not been issued by this name!!")
            print("--------------------------------------------")
        #functions called from DateTime file
        CurrentDate = DateTime.getDate()
        CurrentTime = DateTime.getTime()                                
        list1=[]
        for i in range(len(self.listlender)):
            ##update() method inserts the specified items to the dictionary
            self.dictionarylender.update({(int(self.listlender[i][0]),self.listlender[i][1]):self.listlender[i][2]})
            BookName = self.list[BookID-1][1]
        if (BookID,yourname) in self.dictionarylender.keys():
            returner=os.path.abspath("ReturnersName/Returned By -("+yourname+")"+".txt")
            with open (returner,"a") as x:
                #writes provided lines in txt file
                x.writelines(f"\tLibrary Management System\n\n")
                x.writelines(f"Date:{CurrentDate}\t\t\tTime:{CurrentTime}\n\n")
                x.writelines(f"Returner Name:{yourname}\n")
                x.writelines("------------------------------------------------------------------\n")
                x.writelines(f"BookID\t|\tBook Name\n")
                x.writelines("------------------------------------------------------------------\n")
                x.writelines(f"{BookID}\t|\t{BookName}\n")
                x.writelines("------------------------------------------------------------------\n")
            #opens Librarybook.txt file
            s=open(self.Librarybook, "r")
            for line in s:
                a=line.strip()
                b=a.split("\t")
                self.list.append(b)
            #close Librarybook.txt file
            s.close()
            for i in range(len(self.list)):
                #update() method inserts the specified items to the dictionary
                self.dictionary.update({int(self.list[i][0]):[self.list[i][1],self.list[i][2],int(self.list[i][3]),(self.list[i][4])]})
            list1=self.dictionary.get(BookID)
            list1[3]=int(list1[3])
            list1[3] += 1
            self.dictionary[BookID]=list1
            #open and close Librarybook.txt file
            f = open(self.Librarybook, "w")
            f.close()
            with open(self.Librarybook,"w") as y:
                for key,value in self.dictionary.items():
                    y.write(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}\n")
            print("Is the book return date expired?")
            print("Press Y for Yes and N for No")
            #codes for charging fine after delaying the book while returning
            YN=input()
            if(YN.upper()=="Y"):
                print("By how many days was the book returned late?")
                day=int(input())
                fine=2*day
                with open("ReturnersName/Returned By -("+yourname+")"+".txt","a")as f:
                    f.write("Fine: Rs."+ str(fine)+"\n\n")
                print("------------------------------------------------------------------------------------")
                print(f"{yourname} you have sucessfully returned the Book: {BookName}")
                print(f"You have returned the book {day} days late so, Pay Fine Rs.{fine}")
                print("------------------------------------------------------------------------------------")
            elif (YN.upper()=='N'):
                print("------------------------------------------------------------------------------------")
                print(f"{yourname} you have sucessfully returned the Book: {BookName}")
                print("------------------------------------------------------------------------------------")
            else:
                print("--------------------------------------")
                print("Invalid input! Please check")
                print("--------------------------------------")
            

l=library("Librarybook.txt","Islington Library")


        

