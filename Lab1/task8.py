employees = [
    {"name":"Noor", "dept":"CS", "salary":80000},
    {"name":"Shabab", "dept":"Finance", "salary":70000},
    {"name":"Suhana", "dept":"CS", "salary":85000}
]

max_salary = 0
idx = -1

for i in range(0, len(employees)):
    if employees[i]["salary"] > max_salary:
        max_salary = employees[i]["salary"]
        idx = i

print(employees[idx])