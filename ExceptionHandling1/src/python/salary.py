salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    net_bonus = 0.05 * salary
    print("Net bonus amount: $", net_bonus)
else:
    print("No bonus eligible.")
