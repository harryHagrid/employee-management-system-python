import sys
import sqlite3
import datetime
from datetime import date
from util.dbutil import DbUtil
from util.dateutil import DateUtil
from util.fileutil import FileUtil
from entity.employee import Employee
from entity.department import Department
from service.department_service import DepartmentService


class EmployeeService:


    dept =Department()
    employee = Employee()
    dept_service = DepartmentService()
    fileUtil = FileUtil("employee.txt")
    #
    # fileUtil.objects = employees
    # fileUtil.construct_file_headers("ID", "First Name","Last Name")
    # fileUtil.construct_file()

    db = DbUtil("employee.db")


    def __int__(self):
        print("Default: Employee Service")

    def check_date_of_birth(self, dob):
        date_format = "%Y-%m-%d"
        try:
            yy,mm,dd = str(dob).split("-")

            dob_entered = date(int(yy), int(mm), int(dd))
            age = self.calculate_age(dob_entered)

            if age < 24:
                return False
            else:
                return True
        except ValueError:
            print(sys.exc_info()[1])


        # dob_entered = datetime.datetime.strptime(dob, date_format)


    def calculate_age(self,dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def create_employee_table(self):
        create_table_query = """
            CREATE table employee(
            emp_id varchar(10) primary key,
            fname varchar(50) not null,
            lname varchar(50) not null,
            dob date,
            dept_id varchar(10),
            FOREIGN KEY (dept_id) REFERENCES department(dept_id)            
            );
            """
        try:
            self.db.execute_query(create_table_query)
        except:
            print("Unable to create employee table \n")
            print(sys.exc_info()[1])
            print("\n")



    def save_employee(self, emp: Employee):

        dob = emp.dob
        if self.check_date_of_birth(dob):
            try:
                self.db.execute_dynamic_query("insert into employee (emp_id,fname,lname,dob,dept_id) values (?,?,?,?,?)",
                                              emp.emp_id, emp.fname, emp.lname, emp.dob, emp.dept.dept_id)
                self.db.connection.commit()

                print("Congrats : Employee - " + emp.fname + " details saved \n")
            except sqlite3.IntegrityError:
                print("Sorry- Unable to save employee details. ID already exists \n")
            except:
                print("Sorry- Unable to save employee details. Invalid Values entered \n")
                print(sys.exc_info())

        else:
            print(
                "Oops !! - Employee - " + emp.fname + " too young to get registered. To register, you must be older than 24 years. \n")

    def fetch_all_employees(self):

        employees = []
        query = "select * from employee"
        try:
            self.db.execute_query(query)

            query_result= self.db.fetch_all()

            for emp in query_result:
                self.employee = Employee()
                self.employee.emp_id = emp[0]
                self.employee.fname = emp[1]
                self.employee.lname = emp[2]
                self.employee.dob = emp[3]
                self.employee.dept = self.dept_service.fetch_department_by_id(emp[4])
                employees.append(self.employee)
            print("Employee Details \n")
            print(
                "******************************************\n")

            print("#Id" + "\t \t \t" + "DOB" + "\t\t\t" + "Department" + "\t\t\t" + "fname" + "\t\t\t\t" + "lname" + "\n")
            print("**************************************************************************************************** \n")
            for emp in employees:
                print(emp.emp_id + "\t" + emp.dob + "\t" + emp.dept.dept_name + "\t\t\t\t\t" + emp.fname + " " + emp.lname + "\n")

        except:
            print("Unable to fetch all employees \n")
            print(sys.exc_info()[1])
            print("\n")


        return employees

    def fetch_employee_by_id(self, eid: str):

        self.employee = Employee()
        try:
            self.db.execute_dynamic_query("select * from employee where emp_id = ?", eid)
            query_result = self.db.fetch_one()
            self.employee.emp_id = query_result[0]
            self.employee.fname = query_result[1]
            self.employee.lname = query_result[2]
            self.employee.dob = query_result[3]
            self.employee.dept = self.dept_service.fetch_department_by_id(query_result[4])

            print(
                "#Id" + "\t \t \t" + "DOB" + "\t\t\t" + "Department" + "\t\t\t" + "fname" + "\t\t\t\t" + "lname" + "\n")
            print(
                "**************************************************************************************************** \n")
            print(
                self.employee.emp_id + "\t" + self.employee.dob + "\t" + self.employee.dept.dept_name + "\t\t\t\t\t" + self.employee.fname + " " + self.employee.lname + "\n")
            return self.employee

        except:
            print("Unable to fetch Employee Id - " + eid + " . Please enter correct employee ID.\n")
            print(sys.exc_info()[1])
            print("\n")

    def delete_employee(self, eid):
        try:
            emp_to_be_deleted = self.fetch_employee_by_id(eid)
            self.db.execute_dynamic_query("delete from employee where emp_id=?", eid)
            print("Successfully Deleted Employee - " + emp_to_be_deleted.fname + "\n")
            self.fetch_all_employees()
        except:
            print("Unable to delete Employee Id - " + eid + ". Check employee Id.\n")
            print(sys.exc_info()[1])
            print("\n")

    def update_employee(self, emp : Employee):

        try:
            emp_result = self.fetch_employee_by_id(emp.emp_id)
            try:
                if emp.__eq__(emp_result):
                    #
                    print("Successfully Updated Employee- " + emp.emp_id + "\n")
                else:
                    date_util = DateUtil()
                    if date_util.check_date_of_birth(emp.dob):
                        self.db.execute_dynamic_query(
                            "update employee set fname = ?, lname =?, dob = ? , dept_id = ? where emp_id=?", emp.fname,
                            emp.lname, emp.dob, emp.dept.dept_id, emp.emp_id)
                        self.db.connection.commit()
                        print("Successfully Updated Employee- " + emp.emp_id + "\n")
                    else:
                        print("Sorry!! Unable to update Employee- " + emp.emp_id + "\n")


            except AttributeError:

                if "fname" in str(sys.exc_info()[1]):
                    print("First Name cannot be null")
                elif "lname" in str(sys.exc_info()[1]):
                    print("Last Name cannot be null")
                elif "dob" in str(sys.exc_info()[1]):
                    print("Date of birth is not in correct format")
            except ValueError:
                print(sys.exc_info()[1])
        except:
            print("Unable to update employee Id - " + str(emp.emp_id) + ". Check employee Id.\n")
            print(sys.exc_info())
            print("\n")
