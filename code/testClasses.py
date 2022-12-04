import re

class Employee:
    def __init__(self, line:str):
        self.first_name = parse_name(line)[0][0]
        self.last_name = parse_name(line)[0][1]
        self.address = parse_address(line)
        self.email = parse_email(line)

class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
        
def parse_name(text):
    compiled = re.compile("^([A-Z][a-z]+) ([A-Z][a-z]+)")
    return re.findall(compiled, text)

def parse_address(text):
    compiled = re.compile("([0-9]+ ([A-Za-z_]+ )+)([A-Za-z_]+) ([A-Z][A-Z])")
    extract = re.findall(compiled, text)
    address = Address(extract[0][0].strip(), extract[0][2].strip(), extract[0][3].strip())
    return address 

def parse_email(text):
    compiled = re.compile("[A-Za-z0-9\.\-+_]+@[A-Za-z0-9\.\-+_]+\.[a-z]+")
    email = re.findall(compiled, text)[0]
    return email

def main(path):
    employee_list = []
    FILE = open(path, 'r')
    lines = FILE.readlines()
    
    for line in lines:
        employee_list.append(Employee(line.strip()))
    
    return employee_list

if __name__ == '__main__':
    path = "people.txt"
    listOfEmployees = main(path)
    print("======================= List of Employees =====================\n")
    for employee in listOfEmployees:
        print(f"First Name: {employee.first_name}")
        print(f"Last Name: {employee.last_name}")
        print(f"Address: {employee.address.street} / {employee.address.city} / {employee.address.state}")
        print(f"Email: {employee.email}")
        print()