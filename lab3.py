def check_loan_eligibility():
    # Get user inputs
    salary = float(input("Enter monthly salary: "))
    loan_amount = float(input("Enter the loan amount you are want: "))

    # Check eligibility
    if salary >= 30000 and loan_amount <= 10 * salary:
        print("You are eligible for the loan")
        months = int(input("In how many months do you want to repay the loan? "))
        
        # Apply 10% interest
        interest_rate = 0.10
        total_amount_with_interest = loan_amount * (1 + interest_rate)
        monthly_payment = total_amount_with_interest / months
        
        # Display results
        print(f"With a 10% interest, the total loan amount to repay is: {total_amount_with_interest:.2f}")
        print(f"Your monthly payment will be: {monthly_payment:.2f} for {months} months.")
    else:
        if salary < 30000:
            print("You are not eligible for the loan because your salary is below 30,000.")
        if loan_amount > 10 * salary:
            print(f"You are not eligible for the loan because the loan amount requested is more than 10 times your salary ({salary * 10:.2f}).")

# Run the function
check_loan_eligibility()