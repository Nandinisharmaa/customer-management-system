id_list=[]
name_list=[]
age_list=[]
mob_list=[]
#Business Logic Layer
def add_cust(id,name,age,mob):
    id_list.append(id)
    name_list.append(name)
    age_list.append(age)
    if len(mob)==12:
        mob_list.append(mob)
    else:
        print("Please enter a valid mobile number.")
        mob=input("Enter 10 digit mobile number")
        mob_list.append(mob)
def search_cust(id):
    ind=id_list.index(id)
    print(f"""        
Cust Name: {name_list[ind]}, Cust Age: {age_list[ind]}

""")
def delete_cust(id):#delete customer
    i=id_list.index(id)
    id_list.pop(i)
    name_list.pop(i)
    age_list.pop(i)
def modify_cust(id,name,age):#modify customer
    i=id_list.index(id)
    name_list[i]=name
    age_list[i]=age
def display_cust():
    for i in range(len(age_list)):
        print(f"""cust id :{id_list[i]}, cust name: {name_list[i]}, cust age :{age_list[i]}, Cust mob:{mob_list[i]}
""")
#Presentation Layer
while (1):
    choice=input("""Add : 1, Search : 2, Delete : 3, Modify: 4, Display All :5, Exit ?: Y/N
""")
    if (choice=="1"):
        id=input("Enter Id :")
        name=input("Enter name :")
        age=input("Enter Age :")
        mob=input("Enter mobile number: ")
        add_cust(id,name,age,mob)
    elif(choice=="2"):
        id=input("Enter Id to search: ")
        if id in id_list:
            print("You searched for .......")
            search_cust(id)
        else:
            print("Id not found")
    elif(choice=="3"):
        confirm=input("Are you sure you want to delete ?(Y/N)")
        if confirm.capitalize()=="Y":
            id=input("ENter Id to delete Cust: ")
            if id in id_list:
                delete_cust(id)
                print("Id deleted successfully.")
            else:
                print("Id does'nt exist.")
        else:
            continue
    elif(choice=="4"):
        id=input("Enter Id you want to modify :")
        if id in id_list:
            name=input("Enter updated name ")
            age=input("Enter updated age: ")
            modify_cust(id,name,age)
        else:
            print("Please enter a Valid ID...")
    elif(choice=="5"):
        display_cust()
    elif(choice.capitalize()=="Y"):
        print("Thanks for using Nandini's management system")
        print("You are terminating the program")
        break
    elif(choice.capitalize()=="N"):
        print("Couinting")
        continue
    else:
        print("Incorrect Choice!!!!")