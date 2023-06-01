class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_name(self):
        return self.name

    def get_employee_id(self):
        return self.employee_id


class SalaryCalculator:
    def calculate_salary(self, employee):
        # perform salary calculation logic based on employee attributes
        return salary_amount
