#!/usr/bin/env python
import click
import math

@click.command()
@click.option('--amount', type = float)
@click.option('--term', type = float)
@click.option('--interest', type = float)
def calculate(amount, term, interest):
    """
    Calculate the montly payment, interest, and total amount paid on a loan.
    
    Inputs:
    Amount: Total loan amount.
    Term: The length of the loan term in years.
    Interest: The interest rate of the loan in decimal form. 
    
    Outputs:
    monthlyPayment: The estimated monthly payment for the loan.
    totalPaid: The total amount paid on the loan.
    """
    
    nPayments= term * 12
    rInterest = interest / 12
    interestPow = math.pow((1 + rInterest), nPayments)
    discountFactor = (interestPow - 1)/(interestPow*rInterest)
    monthlyPayment = amount/discountFactor
    totalPaid = monthlyPayment * nPayments
    
    click.echo(f'Your estimated monthly payment is: {monthlyPayment}. You will pay {totalPaid-amount} in interest and {totalPaid} total.')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calculate()
