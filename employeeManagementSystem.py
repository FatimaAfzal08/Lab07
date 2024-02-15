class Employee:
    def __init__(self, name, age, id,department):
        self.name = name
        self.age = int(age)
        self.id = int(id)
        self.department = department
        
class managementSystem: 
    def __init__(self ,initial_employees=None):
        self.employees = []
        if initial_employees:
            self.employees.extend(initial_employees)
        
    def addEmployee(self,name, age,id,department):
        employee = Employee(name, age, id, department)
        self.employees.append(employee)
        print(employee.name)   
           
    def getEmployee(self,id):
        for emp in self.employees:
            print("HEEEEY")
            if emp.id == id:
                print("Employee Information:")
                print("Name:", emp.name)
                print("Age:", emp.age)
                print("Department:", emp.department) 
        else: 
                print("Employee doesnt exist")
                
    def deleteEmployee(self,id):
        for emp in self.employees:
            if emp.id == id:
                self.employees.remove(emp)
                print ("Employee removed successfully")
            else:
                print("Employee not found")

        

def main():
    employeeSystem = managementSystem()
    while True:
        try:
            operation = (input("Do you want to (get , add , delete ) Employee: ")).lower()
            if operation == "add":
                name = input("Enter employee name: ")
                age  =  input("Enter employee age: ")
                emp_id   =  input("Enter employee ID: ")
                department = input("Enter employee department: ")
                employeeSystem.addEmployee(name, age,emp_id,department)
            elif operation == "get":
                id = input("Enter employee id: ") 
                employeeSystem.getEmployee(id)
            elif operation == "delete":
                id = input("Enter employee id: ") 
                employeeSystem.deleteEmployee(id)
            else: 
                print("Invalid operation. Please try again")
                continue
            break
                
            
        except ValueError as e:
            print(e)
            print("Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", e)
            print("Please try again.")    

if __name__ == "__main__":
    main()   