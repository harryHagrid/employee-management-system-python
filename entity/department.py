class Department:

    """department entity"""
    dept_id :str
    dept_name:str
    def __int__(self):
        self.dept_id=""
        self.dept_name=""

    # def __init__(self, dept_id, dept_name):
    #     self.dept_id = dept_id
    #     self.dept_name = dept_name

    def displayDepartmentDetail(self):
        print("Department Details \n")
        print("Id : ", self.dept_id, "\t Name : ", self.dept_name)


