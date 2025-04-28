from Entities.employee import Employee


class Tester(Employee):
    def __init__(self, Employee_id, Employee_name, Employee_salary, Employee_designation,skilledInSelenium, skilledInUFT,skilledINJemeter,testAllowance):
        super().__init__(Employee_id, Employee_name, Employee_salary, Employee_designation)
        self.__skilledInSelenium=skilledInSelenium
        self.__skilledInUFT = skilledInUFT
        self.__skilledInJemeter = skilledINJemeter
        self.__testAllowance=testAllowance

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __str__(self):
        return super().__str__()+"Skilled in Selenium: "+str(self.__skilledInSelenium)+" Skilled in UFT: "+str(self.__skilledInUFT)+" Skilled in Jemeter: "+str(self.__skilledInJemeter)+" Test Allowance: "+str(self.__testAllowance)+"\n"