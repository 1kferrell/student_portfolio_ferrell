##Kyler Ferrell##
##Last Revised 12/09/2023##
##loan_payoff_portfolio_assignment##
##This program uses a function to calculate a vehicle the montly payments on a car loan with the prospective interest rate and loan term ##

#This function sets the monthly payments variable to be an equatio that adds the car loan to the interest and divides it by the loan term#
def calculate_interest():
  monthly_payments = (car_loan + interest) / loan_term
  return monthly_payments

#The variables are initialized based on your loan terms
car_loan = 8500
interest = car_loan // (float(8.74))
loan_term = (float(36.0))

#The monthly gets set to the calculate_interest function#
monthly_payments = calculate_interest()

#The print statement calls the function and your montly payments are displayed#
print(monthly_payments)
