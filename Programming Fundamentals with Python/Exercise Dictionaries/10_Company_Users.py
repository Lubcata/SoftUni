companies = {}
while True:
    info = input()
    if info == "End":
        break
    company_name = info.split(" -> ")[0]
    employer_id = info.split(" -> ")[1]
    if company_name not in companies:
        companies[company_name] = []
    if employer_id not in companies[company_name]:
        companies[company_name].append(employer_id)

for company in companies:
    print(company)
    for employer in companies[company]:
        print(f"-- {employer}")
