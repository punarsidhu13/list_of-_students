print("1. List of Students:- ")
print("2. Search a Student:- ")
print("3. Update a Student:- ")
print("4. Delete a Student:- ")
print("5. Add a Student:- ")
print("6. Exit")



stud_dict=[{"Roll_num":1 , "Name":"Arsh" , "Subjects":["Punjabi","Hindi","English"] , "class":"Ten" } , { "Roll_num":2 , "Name":"Bani" , "Subjects":["Punjabi","Hindi","English"], "class":"five" } ,
{"Roll_num":3 , "Name":"Punar" , "Subjects":["Punjabi","Hindi","English"], "class":"five" } , {  "Roll_num":4 , "Name":"upneet" , "Subjects":["Punjabi","Hindi","English"], "class":"Ten"}
]

#list of students

# if option == 1:
#     for i in range(len(stud_dict)):
#         print(stud_dict[i]['Name'])

def list_of_students():
        name_lst = []
        for i in stud_dict:
            name_lst.append(i['Name'])
        return name_lst

#search a student
# if option == 2:
#     inp = input("Search a Student \n ")
#     for i in range(len(stud_dict)):
#         if stud_dict[i]['Name'] == inp:                                                           
#             print("Found in the list") 
        # else:
        #     print("Name Not Found!")

def search_student():
    inp_search = input("Enter name:- \n")
    for i in stud_dict:
        if i['Name'] == inp_search:
            print("Element found at index:- ", i)
            return i                

 #delete a student 
def delete_student():
    id = int(input("Enter the roll number: \n "))
    for i in stud_dict:
        if i['Roll_num'] == id:
            print("Element found at index:- ", i)
            inp_del = input("Are you sure you want to delete it y/n? \n")
            if inp_del == 'y':
                del i
                print("Record Deleted \n")
                print(stud_dict)
            else:
                pass
            # stud_dict.remove(i)



#update a student

def update_student():
    inp_search = input("Enter name:- \n")
    for i in stud_dict:
        if i['Name'] == inp_search:
            print("Element found at index:- \n", i)
            print("What you want to update:- \n")
            print("1. Update Name:- \n")
            print("2. Update Subjects \n")
            print("3. Update Class:- \n")
            a = int(input("Choose option:- \n"))
            if a == 1:
                inp_new_name = input("Enter updated name \n")
                i.update({'name':inp_new_name})
                print("Updated name is: ",i['Name'])

            elif a == 3:
                inp_new_class = input("Enter Updated class name \n")
                i.update({'class':inp_new_class})
                print("Updated class is: ",i['class'])


#ADD A STUDENT

def add_new_student():
    temp = {
            "roll_no": 0,
            'name':'',
            'subjects': [],
            'class':'',
            }

    inp_roll_no = int(input("Enter roll number:- \n"))
    inp_name = input("Enter name:- \n")
    inp_class = input("Enter class:- \n")
    for i in range(3):
        inp_subject = input("Enter subject name:- \n")
        temp["subjects"].append(inp_subject)
    temp.update({"roll_no":inp_roll_no, 'name':inp_name, 'class':inp_class})
    stud_dict.append(temp)
    print(stud_dict)       

            
option = int(input("Choose an option from above \n  "))

if option == 1:
    a = list_of_students()
    print(a)
    
elif option == 2:
    a = search_student()
    print(a)

elif option == 3:
    update_student()

elif option == 4:
    delete_student()

elif option == 5:
    add_new_student()
    
elif option == 6:
    exit()