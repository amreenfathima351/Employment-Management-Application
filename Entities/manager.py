from Entities.employee import Employee


class Manager(Employee):
    def __init__(self, Employee_id, Employee_name, Employee_salary, Employee_designation,projectAllownace,numberOfProjects):
        super().__init__(Employee_id, Employee_name, Employee_salary, Employee_designation)
        self.__projectAllowance=projectAllownace
        self.__numberofProjects=numberOfProjects

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __str__(self):
        return super().__str__()+" Project Allowance: "+str(self.__projectAllowance)+" Number of Projects: "+str(self.__numberofProjects)+"\n"