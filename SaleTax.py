# Programming Exercise 5-2
#Practice 1 Sales Tax program. 
#Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
# Global constants for the state and county tax rates. #global constant because they won't change.
STATE_TAX_RATE = 0.05
county_tax_RATE = 0.025


#def main
def main():
    # Local variables
    purchase = 0.0
    state_tax = 0.0
    county_tax = 0.0

    # Get the amount of the purchase
    purchase = float(input('Enter the purchase amount: '))

    # Calculate the state tax
    state_tax = purchase * STATE_TAX_RATE

    # Calculate the county tax
    county_tax = purchase * county_tax_RATE

    # Print information about the sale
    show_sale(purchase, state_tax, county_tax)

# The showSale function accepts purchase, state_tax,
# county_tax as arguments and prints the equivalent
# total sale information.
def show_sale(purchase, state_tax, county_tax):
    # local variables
    total_tax = 0.0
    total_sale = 0.0
    total_tax = state_tax + county_tax
    total_sale = purchase + total_tax

    print(f'Purchase amount: {purchase:,.2f}')
    print(f'State tax: {state_tax:,.2f}')
    print(f'County tax: {county_tax:,.2f}')
    print(f'Total tax: {total_tax:,.2f}')
    print(f'Sale total: {total_sale:,.2f}')


# Call the main function.
main()


