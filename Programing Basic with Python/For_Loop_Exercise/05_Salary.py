facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

opened_tabs = int(input())
salary = float(input())

for _ in range(opened_tabs):
    current_tab = input()
    if current_tab == "Facebook":
        salary -= facebook_fine
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_tab == "Instagram":
        salary -= instagram_fine
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif current_tab == "Reddit":
        salary -= reddit_fine
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(f"{int(salary)}")

