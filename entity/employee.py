from entity.department import Department
from datetime import date
from util.dateutil import DateUtil
class Employee:
    """Employee entity"""

    'emp_id,emp_name,dept'
    emp_id: str
    fname: str
    lname: str
    emp_name: str
    dob: date
    dept: Department


    def __init__(self):
        self.emp_name=""


    def displayEmployeeDetail(self):

        print("Employee Details : \n")
        print("Emp ID : \t", self.emp_id, " Name : \t", self.emp_name)
        print(Department.displayDepartmentDetail(self.dept))

    def __eq__(self, other):
        dateUtil = DateUtil()
        return ((self.fname == other.fname) and (self.lname == other.lname) and (self.dept.dept_id == other.dept.dept_id) and (dateUtil.check_no_of_days(self.dob,other.dob) == 0))


