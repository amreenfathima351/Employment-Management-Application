class Employee:
    def __init__(self,Employee_id,Employee_name,Employee_salary,Employee_designation):
        self.__Employee_id=Employee_id
        self.__Employee_name=Employee_name
        self.__Employee_salary=Employee_salary
        self.__Employee_designation=Employee_designation

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __str__(self):
        return "[EmployeeID: "+str(self.__Employee_id)+" Name: "+self.__Employee_name+" Salary: "+str(self.__Employee_salary)+" Designation: "+self.__Employee_designation+"]"+"\n"

    def __repr__(self):
        return "[EmployeeID: "+str(self.__Employee_id)+" Name: "+self.__Employee_name+" Salary: "+str(self.__Employee_salary)+" Designation: "+self.__Employee_designation+"]"+"\n"

