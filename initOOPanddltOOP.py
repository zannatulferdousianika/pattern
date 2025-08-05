class employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
        print(f"[INIT] Employee created: Name = {self.name} , employee_id = {self.employee_id}")
    
    def __del__(self):
        print(f"[DEL] Employee info deleted: Name{self.name}, employee_id= {self.employee_id}")

def deleteMethod():
    print("Creating employee objext....")
    emp = employee("alex", 101)

    print("Employee id created successfully.")

    print("Deleting employee object...")
    del emp

    print("Delete employee id successfully.")

deleteMethod()