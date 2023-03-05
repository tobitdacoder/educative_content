#PRACTICE TO REMEMBER!!!

employee_file=open("employees.txt","r")

print(employee_file.readable())
print(employee_file.readlines())
for employee in employee_file.readlines():
   print(employee)
   
   

employee_file.close()