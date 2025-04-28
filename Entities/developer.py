from Entities.employee import Employee


class Developer(Employee):
    def __init__(self, Employee_id, Employee_name, Employee_salary, Employee_designation, OTAllowance, NightShiftAllowance,allotted):
        super().__init__(Employee_id, Employee_name, Employee_salary, Employee_designation)
        self.__OTAllowance=OTAllowance
        self.__NightShiftAllowance=NightShiftAllowance
        self.__allotted=allotted

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __str__(self):
        return super().__str__()+"Over Time Allowance: "+str(self.__OTAllowance)+" Night Shift Allowance: "+str(self.__NightShiftAllowance)+" Alloted: "+str(self.__allotted)+"\n"