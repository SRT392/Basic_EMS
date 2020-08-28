#List to store the employees.
lstEmployee = []
ssnDict = {}
#clear IDLE
def cls():
    print("\n" * 50)

#Displaying employee info format.
def employeeFormatInfo(name,ssn,phone,email,salary):
    print("")
    print("--------------- {0:s} ---------------".format(name))
    print("SSN: {0:s}".format(ssn))
    print("Phone: {0:s}".format(phone))
    print("Email: {0:s}".format(email))
    print("Salary: {0:s}".format(salary))
    print("---------------------------------------------")
    print("")

#Define view all employees
def viewEmployeeInfo():
    cls()
    print("-------------------------------------------------------------")
    print("")
    print("                 View All employees in the system")
    print("")
    print("-------------------------------------------------------------")
    print("")
    if(len(lstEmployee)==0):
        #If list is equal to 0 then display this message.
        print("-------------------------------------------------------------")
        print("                 No Employees in the list.")
        print("-------------------------------------------------------------")
    else:
        #Display all the employees in the system
        for i in range(0, len(lstEmployee)):
            line = lstEmployee[i].split(",")
            employeeFormatInfo(line[0], line[1], line[2], line[3], line[4])
    try:
        option=int(input("Enter 0 to exit or any key to continue:"))
        if option == 0:
            cls()
    except:
        cls()
#Adding a new employee code.
def addEmployee():
    cls()
    print("-------------------------------------------------------------")
    print("")
    print("                 Add Employee Information")
    print("")
    print("-------------------------------------------------------------")
    print("")
    try:
        #Allow users to add the info.
        name=input("Employee Name: ")
        ssn=input("Employee SSN: ")
        phone=input("Employee Phone No.: ")
        email=input("Employee Email: ")
        salary=input("Employee Salary: ")
        line = name+ "," +ssn +"," +phone +"," +email +"," +salary
        index = len(lstEmployee)
        lstEmployee.insert(index, line)
        ssnDict[ssn] = line #Not sure
    except:
        cls()
        addEmployee()
    print("")
    print(" Employee information has been successfully added to the list.")
    print("")
    print("----------------------------------------------------------------------")
    print("")
    try:
        #Allow users to add or return to main menu when they hit 0
        option=int(input("Enter 0 to return to main menu, or any other "))
        if option == 0:
            cls()
        else:
            cls()
            addEmployee()
    except:
        cls()
        addEmployee()

#Code to display the main menu
def printOptions():
    print("------------------------- Employee Management System --------------\n")
    print("There are ( {0:2} ) employees in the system.".format(len(lstEmployee)))
    print("\n-------------------------------------------------------------------")
    print("1. View all employees  \n")
    print("2. Add new employee  \n")
    #validate user selection (?)
    try:
        answer=int(input("Please enter your option number: "))
    except ValueError:
        print("Not a number")
        return 100
    print ("")
    print("-------------------------------------------------------------------")
    print("")
    return answer
while True:
    cls()
    mode = printOptions()
    #View all employees
    if mode == 1:
        cls()
        viewEmployeeInfo()
    if mode == 2:
        cls()
        addEmployee()
#View Employee by SSN
def viewSSN():
    print(" Search Employee by Social Security Number")
    print("--------------------------------------------")
    findSSN = input("Enter employees SSN: ")
    line = ssnDict[findSSN]
