#!/usr/bin/env python
import click
import math

@click.command()
@click.option('--amount','--term', '--interest')
def calculate(amount, term, interest):
    """
    Calculate the montly payment, interest, and total amount paid on a loan.
    """
    nPayments= term * 12
    rInterest = interest / 12
    interestPow = math.pow(1 + rInterest)
    discountFactor = (rInterest - 1)/(interestPow*rInterest)
    monthlyPayment = amount/discountFactor
    totalPaid = monthlyPayment * nPayments
    
    click.echo(f'Your estimated monthly payment is: {monthlyPayment}. You will pay {totalPaid-amount} in interest and {totalPaid} total.')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calculate()
