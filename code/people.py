# importing libraries
import re


class Employee:
    """_summary_ : This class represents an employee
       _attributes_ : This class has 4 attributes representing employee first and last names, address and the email
    """
    def __init__(self, line:str):
        self.first_name = parse_name(line)[0]
        self.last_name = parse_name(line)[1]
        self.address = parse_address(line)
        self.email = parse_email(line)

class Address:
    """_summary_ : This class represents an address
    """
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
        
def parse_name(text):
    """_summary_ : This will parse the name out of a given string

    Args:
        text (str): This is a single line of the input file

    Returns:
        tuple: returns a tuple which includes first and last names
    """
    
    # this regex will extract two names at the beginning of the string
    compiled = re.compile("^([A-Z][a-z]+) ([A-Z][a-z]+)")
    # find first and last names and return them in a tuple
    return re.findall(compiled, text)[0]

def parse_address(text):
    """Following function will parse an address into a Address object

    Args:
        text (str): This is a single line of the input file

    Returns:
        Address: returns an Address object
    """
    # following is the regex which extract street, city and state out of the line
    compiled = re.compile("([0-9]+ ([A-Za-z_]+ )+)([A-Za-z_]+) ([A-Z][A-Z])")
    # finds all the occuracnces in the line and return in a tuple list
    extract = re.findall(compiled, text)
    # Initiate an Address object by carefully getting data from the returned list of tuples
    address = Address(extract[0][0].strip(), extract[0][2].strip(), extract[0][3].strip())
    # return Address object
    return address 

def parse_email(text):
    """This function parses an email address

    Args:
        text (str): This is a single line of the input file

    Returns:
        Tuple: returns an Address object representing the address of an employee
    """
    # following is the regex pattern to extract the email address
    compiled = re.compile("[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+")
    # finds all the occurrences of the email addresses
    email = re.findall(compiled, text)[0]
    # return email address
    return email

def main(path):
    """This function is the main function which executes the employee object data gathering

    Args:
        path (str): The path name of the relevant file containing employee data

    Returns:
        list(Employee): a lost of Employee objects
    """
    # list containing all the Employee objects
    employee_list = []
    # open the file to read
    FILE = open(path, 'r')
    # read all the lines into a list of lines
    lines = FILE.readlines()
    # iterate over the lines and add completely initiated Employee objects to the list of employees
    for line in lines:
        employee_list.append(Employee(line.strip()))
    # return the list of employees
    return employee_list

if __name__ == '__main__':
    # set the path of the data file
    path = "people.txt"
    # call main function to initialize list of Employee objects
    listOfEmployees = main(path)
    # print the data
    print("======================= List of Employees =====================\n")
    for employee in listOfEmployees:
        print(f"First Name: {employee.first_name}")
        print(f"Last Name: {employee.last_name}")
        print(f"Address: {employee.address.street} / {employee.address.city} / {employee.address.state}")
        print(f"Email: {employee.email}")
        print()