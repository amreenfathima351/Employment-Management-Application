from abc import ABC, abstractmethod


class CompanyServiceProvider(ABC):
    @abstractmethod
    def AddEmployee(self,employee):
        pass

    @abstractmethod
    def returnSortedList(self):
        pass

    @abstractmethod
    def searchEmployee(self,Employee_id):
        pass

    @abstractmethod
    def returnSeleniumTesters(self):
        pass

    @abstractmethod
    def returnUFTTesters(self):
        pass

    @abstractmethod
    def returnManagersWithHighAllowance(self):
        pass

    @abstractmethod
    def returnUnAllocatedDevelopers(self):
        pass

    @abstractmethod
    def managerWithMaxProjects(self):
        pass

    @abstractmethod
    def returnHighlypaidEmployees(self):
        pass
