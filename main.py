from Entities.company import Company
from Entities.developer import Developer
from Entities.manager import Manager
from Entities.tester import Tester
from customerrors.employeenotfound import EmployeeNotFoundException
from customerrors.nounallotteddevelopers import NoUnallottedDevelopers
from services.companyserviceproviderimpl import CompanyServiceProviderImpl

"""Developer Object Creation"""
developerobj1=Developer(123,"Kavi",600000,"Software Developer",4500.00,9000.90,True)
developerobj2=Developer(934,"Fathima",900000,"Product Developer",7800,5600,False)

"""Developer List Creation"""
developer_list=[developerobj1,developerobj2]

"""Tester Object Creation"""
testerobj1=Tester(456,"Dharshini",80000,"Tester",True,False,True,8900)
testerobj2=Tester(146,"Abi",50000,"Tester",False,True,True,8400)

"""Tester List Creation"""
tester_list=[testerobj1,testerobj2]

"""Manager Object Creation"""
managerobj1=Manager(789,"Amreen",700000,"HR Manager",56000,5)
managerobj2=Manager(489,"Arasan",800000,"Manager",25000,2)

"""Manager List Creation"""
manager_list=[managerobj1,managerobj2]

"""Employee List Creation"""
employee_list=developer_list+tester_list+manager_list

"""Company Object Creation"""
company_obj=Company("Hexaware","Siruseri",employee_list)
print(company_obj)

"""ServiceImpl Object Creation"""
serviceobj1=CompanyServiceProviderImpl(company_obj)

"""Adding a new developer to the company"""
new_developer=Developer(999,"Amreenzx",75000,"Full Stack Developer",5000,7000,True)

"""Add employees in company"""
serviceobj1.AddEmployee(new_developer)
"""Printing After adding employee in company"""
print("After Adding New Employee\n",company_obj)

"""Getting Sorted Employees in descending order in terms of salaries"""
sorted_emp=serviceobj1.returnSortedList()
print("Employees list in descending order of salaries\n")
"""printing sorted employees"""
for emp in sorted_emp:
    print(emp)

"""Searching employee based on id"""
print("Searching Employee:")
try:
    print(serviceobj1.searchEmployee(935))
except EmployeeNotFoundException as err:
    print(err,"\n")

print("Selenium Testers")
selenium_testers=serviceobj1.returnSeleniumTesters()
"""Printing Selenium Testers"""
for tester in selenium_testers:
    print(tester)

print("UFT Testers")
"""Printing UTF Tester"""
utf_tester=serviceobj1.returnUFTTesters()
for tester in utf_tester:
    print(tester)

print("High Allowance Manager")
"""Printing High Allowance Manager"""
high_allowance_manager=serviceobj1.returnManagersWithHighAllowance()
for manager in high_allowance_manager:
    print(manager)

print("Un Allocated Developers")
"""Printing Developers who are not allocated to any projects"""
try:
    un_allocated_developer=serviceobj1.returnUnAllocatedDevelopers()
    for undeveloper in un_allocated_developer:
        print(undeveloper)
except NoUnallottedDevelopers as err:
    print(err)

"""Printing managers who are with maximum projects"""
max_manager = serviceobj1.managerWithMaxProjects()
print("Manager with Maximum Projects:\n", max_manager)

print("Top 5 Payment Employees")
"""Printing top 5 payment employees"""
highly_paid_employees=serviceobj1.returnHighlypaidEmployees()
for emp in highly_paid_employees:
    print(emp)
