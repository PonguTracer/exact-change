# Get total change amount from the user
total_change = int(input("Enter the total change amount: "))

# Check if change is non-positive
if total_change <= 0:
    print("No change")

else:
    # Calculate the number of each coin type
    dollars = total_change // 100
    total_change %= 100

    quarters = total_change // 25
    total_change %= 25

    dimes = total_change // 10
    total_change %= 10

    nickels = total_change // 5
    total_change %= 5

    pennies = total_change

    # Output the fewest coins
    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")

    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")

    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")

    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")

    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")
