class Employee:
    def __init__(self,emp_id,name,hourly_rate):
        self.emp_id = emp_id
        self.name = name 
        self.hourly_rate = hourly_rate
        self.work_hour = 0

    def set_work_hours(self, hours):
        self.work_hour = hours

    def calculate_salary(self):
      return self.work_hour * self,hourly_rate

    def display_info(self):
        print(f"Employee ID     : {self.emp_id}")
        print(f"Employee name   : {self.name}")
        print(f"Type            : {self.get_employee_type()}")
        print(f"Work hours      : {self.work_hour}")
        print(f"Hourly rate     : {self.calculate_salary()} Taka\n")

    def get_employee_type(self):
        return "Genaral Employee"



class RegularEmployee(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        if self.work_hour > 160:
            bonus = 0.10*base_salary
            return base_salary + salary
        return base_salary
        
    def overtime_work_bonus(self):
        if self.work_hour > 160:
            bonus = 0.10 * (self.work_hour * self.hourly_rate)
            print(f"Overtime bonus  : {bonus:.2f} Taka")
        else:
            print(f"No Overtime bonus Taka")

    def get_employee_type(self):
        return "Regular Employee"


class TemporaryEmployee(Employee):
    if check_max_hours() > 120:
        print("Warning you cannot work overtime as a temporary employee")
        print()
    else:
        print(f"You have completed with limited time")
    
    def get_employee_type(self):
        return "Temporary Employee"


if __name__ == "__main__":
    emp1 = RegularEmployee(emp_id = 301 , name = "Alex Jordan ", hourly_rate = 300 )
    emp2 = TemporaryEmployee(emp_id = 302 , name = "Max Fernandez ", hourly_rate = 200 )
    emp3 = RegularEmployee(emp_id = 303 , name = "Ikbal isobar ", hourly_rate = 320 )

    emp1.set_work_hours(170)
    emp2.set_work_hours(130)
    emp3.set_work_hours(150)

    employees = [emp1 ,emp2 ,emp3]

    for emp in employees:
        emp.display_info()
        if isinstance(emp , RegularEmployee):
            emp.calculate_overtime_bonus()
            print()
        elif isinstance(emp , TemporaryEmployee):
            emp.check_max_hours()






                


