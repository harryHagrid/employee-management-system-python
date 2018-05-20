import os
import sys
from entity.employee import  Employee
from entity.department import Department


class FileUtil:
    fileName = ""


    objects = []

    def __int__(self):
        print("Default :- File Utility \n")

    def __init__(self,filename):
        self.fileName = filename
        self.newFile = open(os.getcwd() + '\\' + self.fileName, "w")

    def construct_file(self):

        self.write_objects_into_file(self.objects)

    def construct_employee_file(self):
        self.write_employee_into_file(self.objects)

    def construct_department_file(self):
        self.write_department_into_file(self.objects)


    def write_department_into_file(self,objects):
        try:
            for obj in objects:
                entry = ""
                entry = obj.dept_id + "\t\t"+obj.dept_name
                # entry = obj[0]+ '\t' + obj [1]
                self.newFile.write(entry + "\n")
            print("Department details is written into file. Check department.txt file.")
        except:
            print("Unable to add department entry into file \n")
            print(sys.exc_info()[1])
        finally:
            self.newFile.close()



    def write_employee_into_file(self,objects):
        try:
            for obj in objects:
                entry = ""
                entry = obj.emp_id + "\t\t"+obj.dob+"\t\t"+obj.dept.dept_name+"\t\t"+obj.fname+"\t"+obj.lname
                # entry = obj[0]+ '\t' + obj [1]
                self.newFile.write(entry + "\n")
            print("Employee details is written into file. Check employee.txt file.")
        except:
            print("Unable to add employee entry into file \n")
            print(sys.exc_info()[1])
        finally:
            self.newFile.close()



    def write_objects_into_file(self, objects):
        print(objects.__len__())
        try:
            for obj in objects:
                entry = ""

                for i in obj:
                    entry = entry + i + "\t"
                # entry = obj[0]+ '\t' + obj [1]
                self.newFile.write(entry + "\n")
            print("object is written into file")
        except:
            print("Unable to add entry into file \n")
            print(sys.exc_info())

    def construct_file_headers(self, *headers):

        construct_header=""

        for header in headers:
            construct_header = construct_header + header + "\t \t"
        construct_header = construct_header + "\n *****************************************************"
        try:
            self.newFile.write(construct_header + "\n")
        except:
            print("Unable to construct file headers \n")
            print(sys.exc_info()[1])





