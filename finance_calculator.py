"""Simple Employee Financial Summary Program."""


def get_float(prompt, min_value=0, max_value=None):
    """Get a valid float input within a range."""
    while True:
        try:
            value = float(input(prompt))
            if value <= min_value:
                print(f"Value must be greater than {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be between {min_value} and {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Collect data, calculate values, and print report."""

    # Inputs
    employee_name = input("Enter employee name: ")

    annual_salary = get_float("Enter annual salary: ", 0)
    tax_percent = get_float("Enter tax percentage (0-50): ", -1, 50)
    monthly_rent = get_float("Enter monthly rent: ", 0)
    savings_percent = get_float("Enter savings percentage (0-100): ", -1, 100)

    # Calculations
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * tax_percent / 100
    net_salary = monthly_salary - monthly_tax

    savings_amount = net_salary * savings_percent / 100
    disposable_income = net_salary - monthly_rent - savings_amount
    rent_ratio = (monthly_rent / net_salary) * 100

    annual_tax = monthly_tax * 12
    annual_savings = savings_amount * 12
    annual_rent = monthly_rent * 12

    # Report
    print("\n════════════════════════════════════════════")
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("════════════════════════════════════════════")
    print(f"Employee : {employee_name}")
    print(f"Annual Salary : ₹{annual_salary:,.2f}")
    print("────────────────────────────────────────────")
    print("Monthly Breakdown:")
    print(f"Gross Salary : ₹ {monthly_salary:,.2f}")
    print(f"Tax ({tax_percent:.1f}%) : ₹ {monthly_tax:,.2f}")
    print(f"Net Salary : ₹ {net_salary:,.2f}")
    print(
        f"Rent : ₹ {monthly_rent:,.2f} "
        f"({rent_ratio:.1f}% of net)"
    )
    print(
        f"Savings ({savings_percent:.1f}%) : "
        f"₹ {savings_amount:,.2f}"
    )
    print(f"Disposable : ₹ {disposable_income:,.2f}")
    print("────────────────────────────────────────────")
    print("Annual Projection:")
    print(f"Total Tax : ₹ {annual_tax:,.2f}")
    print(f"Total Savings : ₹ {annual_savings:,.2f}")
    print(f"Total Rent : ₹ {annual_rent:,.2f}")
    print("════════════════════════════════════════════")


if __name__ == "__main__":
    main()
    