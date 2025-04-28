# Employee Management System

## Overview

The Employee Management System allows the management of employees within a company. It includes functionalities to add employees, search employees by ID, sort employees by salary, and filter them based on specific criteria (e.g., Selenium testers, UFT testers, and more). This system also supports allocation of developers, and managers with the highest allowances or the maximum number of projects.

## Features

- **Employee Creation**: Create different types of employees such as Developers, Testers, and Managers.
- **Adding Employees**: Add new employees dynamically to the company.
- **Sorting**: Retrieve a sorted list of employees based on salary in descending order.
- **Employee Search**: Search for an employee by their unique ID.
- **Employee Filtering**: 
  - Get a list of Selenium testers.
  - Get a list of UFT testers.
  - Get managers with the highest allowances.
  - Get developers who are not allocated to any projects.
  - Find the manager with the maximum number of projects.
- **High Salary Employee Listing**: Display the top 5 highest-paid employees in the company.

## Technologies Used

- **Python**: Main programming language used for development.
- **Custom Classes**: 
  - `Company`
  - `Developer`
  - `Tester`
  - `Manager`
  - `EmployeeNotFoundException`
  - `NoUnallottedDevelopers`
  - `CompanyServiceProviderImpl`
- **Error Handling**: Custom error classes such as `EmployeeNotFoundException` and `NoUnallottedDevelopers`.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Employement-Management-Application.git
   ```

2. Install the necessary dependencies if any are required.

3. Run the main script to test functionalities:
   ```bash
   python main.py
   ```

## Structure

The project is organized into different **Entities** for various employee roles and services:

- **Entities**:
  - `company.py`: Contains the `Company` class that manages all employees.
  - `developer.py`: Contains the `Developer` class with attributes like salary, role, and allocation status.
  - `manager.py`: Contains the `Manager` class, including the manager's allowance and project count.
  - `tester.py`: Contains the `Tester` class, with fields for test tool knowledge and experience.
  
- **Custom Errors**:
  - `employeenotfound.py`: Defines the custom error when an employee is not found by their ID.
  - `nounallotteddevelopers.py`: Defines the custom error when no unallocated developers are available.

- **Services**:
  - `companyserviceproviderimpl.py`: Implements the services for adding employees, searching employees, filtering based on certain conditions, and sorting employees.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
