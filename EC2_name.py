import random

num_names = int(input("How many instances do you need?"))

department_names = ["Marketing", "Accounting", "FinOps", "Sales" "Purchasing", "Recruiting",]

random_department_names = random.choice(department_names)

for _ in range(num_names):
    random_department_names = random.choice(department_names)
    
    print(random_department_names)
