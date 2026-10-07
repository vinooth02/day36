import unittest
from employee import EmployeeFile


class EmployeeFileTest(unittest.TestCase):

    def setUp(self):
        self.employee_file = EmployeeFile()

    def test_write_employee(self):

        self.employee_file.write_employee("Karan", 40000)

        data = self.employee_file.read_employee()

        self.assertIn("Karan", data)
        self.assertIn("40000", data)

    def test_read_employee(self):

        self.employee_file.write_employee("Riya", 50000)

        data = self.employee_file.read_employee()

        self.assertEqual(data, "Name: Riya\nSalary: 50000")


if __name__ == "__main__":
    unittest.main()