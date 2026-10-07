class EmployeeFile:

    def write_employee(self, name, salary):

        with open("employees.txt", "w") as file:
            file.write("Name: " + name + "\n")
            file.write("Salary: " + str(salary))

    def read_employee(self):

        with open("employees.txt", "r") as file:
            data = file.read()

        return data