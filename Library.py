class Library:
    def __init__(self,book_list,name):
        self.book_list=book_list
        self.name=name
        self.lenddict={}

    def display_book(self):
        print(f"we have following book in our library:{self.name}")
        for book in self.book_list:
            print(book)
    def lend_book(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("the book dictonary has been updated");
        else:
            print(f"the book has been taken by { self.lenddict[book]}")  
    def lendbook_display(self):
        for booked in self.lenddict.keys():
            print(booked)          
            
    def add_book(self,book):
        self.book_list.append(book)
        print('the book has been added sucessfully')
    def return_book(self,book):
        self.lenddict.pop(book)

if __name__ == "__main__":
    block=Library(['python','Java','react','dot.net','php'],"booktech") 
    while(True):
        print(f"welcome to the {block.name}library. Enter your choice")
        print("1.display book")
        print("2.lend book")
        print("3.add book")
        print("4.return book")
        print("5.display the lended book")
        userchoice=int(input())
        if userchoice==1:
            block.display_book()
        elif userchoice==2:
            book=input("enter the name of the book you want to lend:")
            user=input("enter your name :")
            block.lend_book(user,book)
        elif userchoice==3:
            book=input("enter the name of the book u want to add")
            block.add_book(book)
        elif userchoice==4:
            book=input("enter the name of the book u want to return")
            block.return_book(book)
        elif userchoice==5:
            block.lendbook_display()    
        else:
            print("invalid keywords")  

        print("Press q to quit or c to continue")
        userchoice2=input()
        while(userchoice2!= "c" and userchoice2!= "q"):
            if userchoice2=="q":
                exit()
            elif userchoice2=="c":
                continue

