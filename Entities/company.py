class Company:
    def __init__(self,company_name,location,employee_list):
        self.__company_name=company_name
        self.__location=location
        self.__employee_list=employee_list

    def __getattribute__(self, __name):
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)

    def __str__(self):
        return "Company [Company Name: "+self.__company_name+" Location: "+self.__location+" Company List: "+str(self.__employee_list)+"]"+"\n"
