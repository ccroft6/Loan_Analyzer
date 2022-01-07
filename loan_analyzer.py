# Initial imports.
import csv
from pathlib import Path

"""Part 1: Automate the Calculations """

#Loan cost list.
loan_costs = [500, 600, 200, 1000, 450]

# Print the number of loans from the list.
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans in the list.")

# Print the total value of the loans.
total_value_of_loans = sum(loan_costs)
print(f"The total value of all the loans is: ${total_value_of_loans}.")

# Print the average loan amount.
average_loan_price = (total_value_of_loans)/(number_of_loans)
print(f"The average loan price is: ${average_loan_price}.")

"""Part 2: Analyze Loan Data"""

# Dictionary with loan data. I will use this information to calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract the future value and remaining months on the loan from the loan dictionary.
# Print each variable.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value of the loan is: ${future_value}.")
print(f"The remaining months on the loan are: {remaining_months}.")

# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
# Use the **monthly** version of the present value formula.
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = future_value / (1 + 0.20/12) ** remaining_months
print(f"The present value of the loan is ${present_value:.2f}.")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if present_value >= loan["loan_price"]:
    print("The loan is worth at least the cost to buy it.")

elif present_value < loan["loan_price"]:
    print("The loan is too expensive and not worth the price.")


"""Part 3: Perform financial calculations"""

# New loan data in dictionary. Given the following loan data, I will calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return present_value

# Use the function to calculate the present value of the new loan.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
present_value = calculate_present_value(
        new_loan["future_value"],
        new_loan["remaining_months"],
        annual_discount_rate)
print(f"The present value of the new loan is: ${present_value:.2f}.")


"""Part 4: Conditionally filter lists of loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print(f"The inexpensive loans include {inexpensive_loans}.")
               

"""Part 5: Save the results. Output this list of inexpensive loans to a csv file."""

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")
with open(output_path, "w", newline = "") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
       csvwriter.writerow(loan.values())

    





