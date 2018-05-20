import sys
import sqlite3
import datetime
from datetime import date
from util.dbutil import DbUtil
from entity.employee import Employee
from entity.department import Department

class DepartmentService:
    dept = Department()
    db_dept = DbUtil("department.db")

    def create_department_table(self):
        create_dept_query = """
            CREATE table department (
            dept_id varchar(10) primary key,
            name varchar(50) not null         
            );
            """
        try:
            self.db_dept.execute_query(create_dept_query)
        except:
            print("Unable to create department table \n")
            print(sys.exc_info())
            print("\n")

    def save_department(self, dept: Department):
        try:
            self.db_dept.execute_dynamic_query("insert into department (dept_id,name) values (?,?)",dept.dept_id,dept.dept_name)
            self.db_dept.connection.commit()
            print("Congrats : Department - " + dept.dept_name + " details saved \n")
        except:
            print("Sorry- Unable to save department details. Invalid Values entered \n")
            print(sys.exc_info()[1])

    def fetch_department_by_id(self, did):



        try:
            self.dept = Department()
            self.db_dept.execute_dynamic_query("select * from department where dept_id = ?", did)
            query_result = self.db_dept.fetch_one()


            self.dept.dept_id = query_result[0]
            self.dept.dept_name = query_result[1]
            return self.dept

        except:
            print("Unable to fetch Department Id - " + str(did) + " \n")
            print(sys.exc_info()[1])
            print("\n")



    def fetch_all_department(self):

        departments = []

        try:
            self.db_dept.execute_query("select * from department")
            query_result = self.db_dept.fetch_all()

            for d in query_result:
                self.dept = Department()
                self.dept.dept_id = d[0]
                self.dept.dept_name = d[1]
                departments.append(self.dept)
            print("Department Details \n")
            print(
                "******************************************\n")

            print("#Id" + "\t" + "name" + "\n")
            print(
                "******************************************\n")
            for d in departments:
                print(d.dept_id+"\t"+d.dept_name + "\n")
            return departments

        except:
            print("Unable to fetch all departments \n")
            print(sys.exc_info()[1])
            print("\n")


    def update_department(self, department : Department):


        try:
            self.fetch_department_by_id(department.dept_id)
            self.db_dept.execute_dynamic_query("update department set name = ? where dept_id=?", department.dept_name,department.dept_id)
            print("Successfully Updated - "+department.dept_name+"\n")
        except AttributeError:

            if "dept_name" in str(sys.exc_info()[1]):
                print("Department Name cannot be null")
        except ValueError:
            print("value")
        except:
            print("Unable to update Department Id - " + str(department.dept_id) + ". Check department Id.\n")
            print(sys.exc_info()[1])
            print("\n")


    def delete_department(self, did):
        try:
            dept_to_be_deleted = self.fetch_department_by_id(did)
            self.db_dept.execute_dynamic_query("delete from department where dept_id=?", did)
            print("Successfully Deleted Department- " + dept_to_be_deleted.dept_name + "\n")
            self.fetch_all_department()
        except:
            print("Unable to delete Department Id - " + did + ". Check department Id.\n")
            print(sys.exc_info()[1])
            print("\n")
