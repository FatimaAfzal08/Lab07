import unittest
from employeeManagementSystem import managementSystem
from employeeManagementSystem import Employee

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.emp_sys = managementSystem([
            Employee("John Doe", 30, 101, "HR"),
            Employee("Jane Smith", 25, 102, "Engineering")
        ])

    def test_getEmployee(self):
        self.assertEqual(self.emp_sys.getEmployee(102))

    def test_deleteEmployee(self):
        self.assertTrue(self.emp_sys.deleteEmployee(102))
        self.assertIsNone(self.emp_sys.getEmployee(102))
        
    def test_delete_non_existing_employee(self):
        self.assertFalse(self.emp_sys.delete_employee(103))



if __name__ == '__main__':
    unittest.main()
