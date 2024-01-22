#lIST
#Amisha Anand 
#Cora Baker(part 1)
#Shopping list

print("Hello, Welcome to the Shopping list")
mylist = ["apples"]
def shoppinglist():
    Answer = input("1.Add a task \n2.View List \n3.Mark task complete  \n4.Remove task \n5.exit \n6.Remove all tasks from list \n7.Sort list alphabetically \n8.Print the number of Items on the To-do List ")
    if (Answer== "1"):
        item = str(input("What would you like to add: "))
        mylist.append(item)
        shoppinglist()
        
    elif (Answer == "2"):
        print(mylist)
        shoppinglist()
    
    elif (Answer == "3"):
        change = input("What is the item you would like to mark as complete?: ")
        i = mylist.index(change)
        mylist[i] = change + "X"
        shoppinglist()
    elif(Answer == "4"):
        rem = input("What would you like to remove?: ")
        mylist.remove(rem)
        shoppinglist()
    elif(Answer == "5"):
        print("Thank You for using the list")
    elif(Answer == "6"):
        mylist.clear() 
        shoppinglist()
    elif(Answer == "7"):
        mylist.sort()        
        shoppinglist()
    elif(Answer=="8"):
        print(len(mylist))
        shoppinglist()


shoppinglist()