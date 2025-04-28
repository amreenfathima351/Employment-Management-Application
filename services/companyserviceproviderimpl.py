from customerrors.employeenotfound import EmployeeNotFoundException
from customerrors.nounallotteddevelopers import NoUnallottedDevelopers
from services.companyserviceprovider import CompanyServiceProvider


class CompanyServiceProviderImpl(CompanyServiceProvider):
    def __init__(self,company_obj):
        self.__company_obj=company_obj

    def AddEmployee(self,employee):
        self.__company_obj.__getattribute__("_Company__employee_list").append(employee)

    def returnSortedList(self):
        sorted_list=sorted(self.__company_obj.__getattribute__("_Company__employee_list"),key=lambda s:s.__getattribute__("_Employee__Employee_salary"),reverse=True)
        return sorted_list

    def searchEmployee(self,id):
        for employeeobj in self.__company_obj.__getattribute__("_Company__employee_list"):
            if id==employeeobj.__getattribute__("_Employee__Employee_id"):
                return employeeobj
        raise EmployeeNotFoundException(f"Employee with ID {id} not found")

    def returnSeleniumTesters(self):
        selenium_testers=[]
        for employeeobj in self.__company_obj.__getattribute__("_Company__employee_list"):
            if hasattr(employeeobj,"_Tester__skilledInSelenium") and employeeobj.__getattribute__("_Tester__skilledInSelenium"):
                selenium_testers.append(employeeobj)
        return selenium_testers


    def returnUFTTesters(self):
        uft_testers=[]
        for utfobj in self.__company_obj.__getattribute__("_Company__employee_list"):
            if hasattr(utfobj,"_Tester__skilledInUFT") and utfobj.__getattribute__("_Tester__skilledInUFT"):
                uft_testers.append(utfobj)
        return uft_testers

    def returnManagersWithHighAllowance(self):
        high_allowance_managers=[]
        for manager in self.__company_obj.__getattribute__("_Company__employee_list"):
            if hasattr(manager,"_Manager__projectAllowance") and manager.__getattribute__("_Manager__projectAllowance")>50000:
                high_allowance_managers.append(manager)
        return high_allowance_managers


    def returnUnAllocatedDevelopers(self):
        UnAllocated_Developer=[]
        for undeveloped in self.__company_obj.__getattribute__("_Company__employee_list"):
            if hasattr(undeveloped,"_Developer__allotted") and getattr(undeveloped,"_Developer__allotted")==False:
                UnAllocated_Developer.append(undeveloped)
            else:
                raise NoUnallottedDevelopers
        return UnAllocated_Developer

    def managerWithMaxProjects(self):
        managers = []
        for emp in self.__company_obj.__getattribute__("_Company__employee_list"):
            if hasattr(emp, "_Manager__numberofProjects") and emp.__class__.__name__ == "Manager":
                managers.append(emp)

        max_manager = managers[0]
        for manager in managers[1:]:
            if getattr(manager, "_Manager__numberofProjects") > getattr(max_manager, "_Manager__numberofProjects"):
                max_manager = manager
        return max_manager

    def returnHighlypaidEmployees(self):
        emp=self.__company_obj.__getattribute__("_Company__employee_list")
        def calculate_payment(emp):
            base_sal=getattr(emp,"_Employee__Employee_salary")
            if emp.__class__.__name__=="Developer":
                allowance=getattr(emp,"_Developer__OTAllowance")+getattr(emp,"_Developer__NightShiftAllowance")
            elif emp.__class__.__name__=="Tester":
                allowance=getattr(emp,"_Tester__testAllowance")
            elif emp.__class__.__name__=="Manager":
                allowance=getattr(emp,"_Manager__projectAllowance")
            else:
                allowance=0
            return base_sal+allowance
        sorted_employees=sorted(emp,key=calculate_payment,reverse=True)
        return sorted_employees[:5]