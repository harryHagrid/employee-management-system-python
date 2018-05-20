from entity.employee import Employee
from entity.department import Department
from service.employee_service import EmployeeService
from service.department_service import DepartmentService
import time
import sys
from util.dbutil import DbUtil
from util.fileutil import FileUtil

# class EmployeeManagementSystem :

service = EmployeeService()
dept_service = DepartmentService()


def employee_file_operations():
    employee_file = FileUtil("employee.txt")
    employee_file.objects = service.fetch_all_employees()
    employee_file.construct_file_headers("\tID", "\tDOB", "\tDepartment", "\tName")
    employee_file.construct_employee_file()


def department_file_operations():
    department_file = FileUtil("department.txt")
    department_file.objects = dept_service.fetch_all_department()
    department_file.construct_file_headers("ID", "Name")
    department_file.construct_department_file()


def main():


    employee_file_operations()
    department_file_operations()


    value: int
    print("""
       Welcome to Employee Management System
       ******************************************************************
       1. Fetch All Employees
       2. Fetch Employee by ID
       3. Save Employee Details
       4. Save Department Details
       5. Fetch All Departments
       6. Fetch Department by ID
       7. Delete Employee by ID
       8. Delete Department by ID
       9. Update Employee by ID
       10. Update Department by ID.
       
       --- Designed by - Abhishek Pattanaik (Mindtree)
       """)
    while True:
        try:
            value = int(input("Enter the input operation--"))
            if value ==1 :
                service.fetch_all_employees()
            if value == 2 :
                input_id =  input("Enter Employee ID - ")
                service.fetch_employee_by_id(input_id)
            if value == 3:
                emp = Employee()
                service.fetch_all_employees()
                emp.emp_id = input("Enter Employee id - ")
                emp.fname= input("Enter Employee first name - ")
                emp.lname= input("Enter Employee last name - ")
                emp.dob= input("Enter Employee Date of Birth - ")
                print("Choose department id from the existing department - \n ************************************")
                dept_service.fetch_all_department()
                did = input("Enter the department id - ")
                emp.dept = dept_service.fetch_department_by_id(did)
                if validate_employee_input(emp):
                    service.save_employee(emp)
                    fileUtil = FileUtil("employee.txt")
                    fileUtil.objects = service.fetch_all_employees()
                    fileUtil.construct_file_headers("ID", "First Name", "Last Name", "DOB", "Department")
                    fileUtil.construct_file()

                    service.fetch_all_employees()
                    employee_file_operations()

                else:
                    print("Please enter correct inputs.")

            if value == 4:
                dept = Department()
                dept_service.fetch_all_department()
                dept.dept_id = input ("Enter the department id - ")
                dept.dept_name = input ("Enter the department name - ")

                dept_service.save_department(dept)
                department_file_operations()


            if value == 5:
                dept_service.fetch_all_department()

            if value == 6:
                did = input("Enter the Department ID to be fetched - ")
                try :

                    d = dept_service.fetch_department_by_id(did)
                    print("Department Detail \n")
                    print(
                        "******************************************\n")

                    print("#Id" + "\t" + "name" + "\n")
                    print(
                        "******************************************\n")
                    print(d.dept_id + "\t" + d.dept_name + "\n")
                except:
                    print("Unable to fetch Department Id - " + str(did) + " \n")
                    print(sys.exc_info()[1])
                    print("\n")
            if value ==7:
                    service.fetch_all_employees()
                    eid = input("Enter the employee id to be deleted - ")
                    service.delete_employee(eid)
                    employee_file_operations()
            if value ==8:
                    dept_service.fetch_all_department()
                    did=input("Enter the department id to be deleted - ")
                    dept_service.delete_department(did)
                    department_file_operations()

            if value ==9:
                    emp_update = Employee()
                    service.fetch_all_employees()
                    print("Employee Update service \n *************************************************")
                    emp_update.emp_id = input("Enter the employee Id -- ")
                    if len(emp_update.emp_id) != 0:
                        emp = service.fetch_employee_by_id(emp_update.emp_id)
                        # emp_update.emp_id = input("Enter the employee Id")
                        emp_update.fname = input("Enter the first name -- ")
                        emp_update.lname = input("Enter the last name -- ")
                        emp_update.dob = input("Enter the Date of Birth. DOB should be in yyyy-mm-dd -- ")
                        dept_service.fetch_all_department()
                        d = Department()
                        d.did = input("Enter the department id -- ")

                        if len(d.did) == 0:
                            d.did = emp.emp_id



                        if validate_employee_input(emp_update):
                            emp_update.dept = dept_service.fetch_department_by_id(d.did)
                            service.update_employee(emp_update)
                            service.fetch_all_employees()
                            employee_file_operations()
                        else:
                            emp_update = emp
                            emp_update.dept = dept_service.fetch_department_by_id(d.did)
                            service.update_employee(emp_update)
                            service.fetch_all_employees()
                            employee_file_operations()
                    else:

                        print("Enter correct inputs.Please Try Again !!")



                    # if validate_employee_input(emp_update):
                    #     service.update_employee(emp_update)
                    #     service.fetch_all_employees()
                    # else:
                    #     print("Please enter correct inputs.")
            if value == 10:
                d = Department()
                dept_service.fetch_all_department()
                did= input("Enter Department Id to be updated: - ")
                if len(did) != 0:
                    d = dept_service.fetch_department_by_id(did)

                    print("Department Detail \n")
                    print(
                        "******************************************\n")

                    print("#Id" + "\t" + "name" + "\n")
                    print(
                        "******************************************\n")
                    print(d.dept_id + "\t" + d.dept_name + "\n")
                    dname = input("Enter department name - ")
                    if dname.isalpha() == False:
                        print("Department name should have alphabets. Retry Again !!")
                    else:
                        if len(dname) == 0:
                            dname = d.dept_name

                        d.dept_name = dname
                        dept_service.update_department(d)
                        dept_service.fetch_all_department()
                        department_file_operations()
                else:

                    print("Enter correct inputs.Please Try Again !!")



        except ValueError:
            print("Wrong input operation. Kindly enter the input displayed above :- ")

    print("----------------------------")



    # employees = db.fetch_all()

    # employees = service.fetch_all_employees()
    #
    # fileUtil = FileUtil("employee.txt")
    #
    # fileUtil.objects = employees
    # fileUtil.construct_file_headers("ID", "First Name","Last Name")
    # fileUtil.construct_file()

    dept_service.db_dept.close_connection()
    service.db.close_connection()

def validate_employee_input(uemp:Employee):
    validated: bool = True
    if str(uemp.fname).isalpha() == False:
        validated = False
        print("First Name should have alphabets")
    if str(uemp.lname).isalpha() == False:
        validated = False
        print("Last Name should have alphabets")

    try:
        time.strptime(uemp.dob,'%Y-%m-%d')
        validated = True
    except ValueError:
        validated = False
        print("""The date of birth should be in "yyyy-mm-dd""""")

    return validated

def user_input():
    value: int
    print("""
    Welcome to Employee Management System
    ******************************************************************
    1. Fetch All Employees
    2. Fetch Employee by ID
    3. Save Employee Details
    4. Save Department Details
    5. Fetch All Departments
    6. Fetch Department by ID
    7. Delete Employee by ID
    8. Delete Department by ID
    9. Update Employee by ID
    10. Update Department by ID.
    """)
    while True:
        try:
            value = int(input("Enter the input operation--"))
            return value
        except ValueError:
            print("Wrong input operation. Kindly enter the input displayed above :- ")


    #
    #     print("Wrong input operation. Kindly enter the input displayed above :- ")
    #     user_input()
    # else:
    #     return value



if __name__ == '__main__':
    main()
