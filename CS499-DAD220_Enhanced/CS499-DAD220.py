# Tobias O'Brien
# CS499-DAD220
# Nov/ Dec 2021

# Goal of the program is to provide a user interface to the work completed in DAD-220
# View Employees that were hired within a specific time period
# Search for Employee by First and Last Name
# Search for Employee by Employee Number
# Search for and View and Employees Salary by Employee Number
# Search for a Dept and list users
# Tell me the story of a user

import datetime
import mysql.connector

# User menu layout
menu_options = {
    1: 'View Employees that were hired within a specific time period',
    2: 'Search for Employee by First and Last Name',
    3: 'Search for Employee by Employee Number',
    4: 'Search for and View and Employees Salary by Employee Number',
    5: 'List employees by Department Number',
    6: 'Tell me the users story',
    7: 'Exit',
}


# Define the user menu
def print_menu():
    print()
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print()


# Define option 1 - Search for Employee by hire date
def option1():
    #  Get hire date range.  Must be in format DDMMYYYY
    hire_start_date = input("Please enter the hire date in the format DDMMYYYY: ")
    hire_end_date = input("Please enter the end date in the format DDMMYYYY: ")

    #  Convert user input in datetime format
    hire_start = datetime.datetime.strptime(hire_start_date, "%d%m%Y").date()
    hire_end = datetime.datetime.strptime(hire_end_date, "%d%m%Y").date()

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123', database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable
    query = ("SELECT first_name, last_name, hire_date FROM employees "
             "WHERE hire_date BETWEEN %s AND %s")

    # Execute query
    cursor.execute(query, (hire_start, hire_end))

    # Loop through and display the results
    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%b %d %Y.}".format(
            last_name, first_name, hire_date))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


# Define option 2 - Search for Employee by first and last name
def option2():
    #  Get first and last name
    f_name = input("Please enter the employees first name: ")
    l_name = input("Please enter the employees last name: ")

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123', database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable
    query = ("SELECT first_name, last_name, emp_no, birth_date, gender, hire_date FROM employees "
             "WHERE first_name = %s AND last_name = %s")

    # Execute query
    cursor.execute(query, (f_name, l_name))

    # Loop through and display the results
    for (first_name, last_name, emp_no, birth_date, gender, hire_date) in cursor:
        print()
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Emp No: {}".format(emp_no))
        print("Birthdate: {}".format(birth_date))
        print("Gender: {}".format(gender))
        print("Hire Date: {}".format(hire_date))
        print("{}, {}, {}, {}, {}, {}".format(last_name, first_name, emp_no, birth_date, gender, hire_date))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


# Define option 3 - Search for Employee Number
def option3():
    #  Get Employee Number
    e_num = input("Please enter the employees emp_no: ")

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123', database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable
    query = ("SELECT first_name, last_name, emp_no, birth_date, gender, hire_date FROM employees "
             "WHERE emp_no = %s")

    # Execute query
    cursor.execute(query, (e_num,))

    # Loop through and display the results
    for (first_name, last_name, emp_no, birth_date, gender, hire_date) in cursor:
        print()
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Emp No: {}".format(emp_no))
        print("Birthdate: {}".format(birth_date))
        print("Gender: {}".format(gender))
        print("Hire Date: {}".format(hire_date))
        print("{}, {}, {}, {}, {}, {}".format(last_name, first_name, emp_no, birth_date, gender, hire_date))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


# Define option 4 - Show Employee Salary Information
def option4():
    #  Get Employee Number
    e_num = input("Please enter the employees emp_no to show their salary: ")

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123', database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable - Multiple tables are present with and INNER JOIN
    query = ("SELECT employees.first_name, employees.last_name, employees.emp_no, "
             "employees.birth_date, employees.gender, employees.hire_date, salaries.salary "
             "FROM employees "
             "INNER JOIN salaries "
             "ON employees.emp_no = salaries.emp_no "
             "WHERE employees.emp_no = %s")

    # Execute query
    cursor.execute(query, (e_num,))

    # Loop through and display the results
    for (first_name, last_name, emp_no, birth_date, gender, hire_date, salary) in cursor:
        print()
        print("First Name: {}".format(first_name))
        print("Last Name: {}".format(last_name))
        print("Emp No: {}".format(emp_no))
        print("Salary: ${}".format(salary))
        print("{}, {}, {}, {}, {}, {}, {}".format(last_name, first_name, emp_no, birth_date, gender, hire_date, salary))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


# Define option 5 - List users by Department
def option5():
    #  Get Employee Number
    d_num = input("Please enter the dept_no to show the users: ")

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123', database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable - Multiple tables are present with and INNER JOIN
    query = ("SELECT employees.first_name, employees.last_name, employees.emp_no, "
             "dept_emp.dept_no "
             "FROM employees "
             "INNER JOIN dept_emp "
             "ON employees.emp_no = dept_emp.emp_no "
             "WHERE dept_emp.dept_no = %s")

    # Execute query
    cursor.execute(query, (d_num,))

    # Loop through and display the results
    for (first_name, last_name, emp_no, dept_no) in cursor:
        print("{}, {}, employee number: {} is a member of department {}".format(
            last_name, first_name, emp_no, dept_no))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


# Define option 6 - Tell me the Users Story
def option6():
    #  Get Employee Number
    e_num = input("Please enter the employees emp_no to show their story: ")

    # Connect to MySQL instance
    cnx = mysql.connector.connect(user='root', password='Password123' , database='employees')

    # Create cursor object
    cursor = cnx.cursor()

    # Define query with variable - Multiple tables are present with JOINS
    query = ("SELECT employees.emp_no, employees.birth_date, employees.first_name, employees.last_name, "
             "employees.gender, employees.hire_date, sal.salary, sal.salary_from_date, titl.title, "
             "titl.title_from_date, dept.dept_no, dept.dept_from_date, depts.dept_name "
             "FROM employees "
             "JOIN (SELECT emp_no, MAX(salary) as salary, MAX(from_date) as salary_from_date "
             "FROM salaries GROUP BY emp_no) sal ON employees.emp_no = sal.emp_no "
             "JOIN (SELECT emp_no, title, MAX(from_date) as title_from_date "
             "FROM titles GROUP BY emp_no) titl ON employees.emp_no = titl.emp_no "
             "JOIN (SELECT emp_no, dept_no, MAX(from_date) as dept_from_date "
             "FROM dept_emp GROUP BY emp_no) dept ON employees.emp_no = dept.emp_no "
             "JOIN (SELECT dept_no, dept_name "
             "FROM departments GROUP by dept_no) depts "
             "ON dept.dept_no = depts.dept_no "
             "AND employees.emp_no = %s")

    # Execute query
    cursor.execute(query, (e_num,))

    # Loop through and display the results
    for (emp_no, birth_date, first_name, last_name, gender, hire_date, salary,
         salary_from_date, title, title_from_date, dept_no, dept_from_date,
         dept_name) in cursor:
        print("This is the story of {} {}.  {} was hired on {} with an employee number of {}.  "
              "{} works in the {} organization and has the title of {} that was obtained on {}.  "
              "{} has a current salary of ${} which was obtained on {}.  {} was born on {}.".
              format(first_name, last_name, first_name, hire_date, emp_no, first_name,
                     dept_name, title, title_from_date, first_name, salary,
                     salary_from_date, first_name, birth_date))

    # Clean up the objects
    cursor.close()
    cnx.close()
    print()


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 7:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')
