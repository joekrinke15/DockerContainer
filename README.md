# Loan Payment Calculator
I made this program for the purpose of trying out Docker. This program calculates monthly loan payments, total amount paid, and interest paid given a loan's term length, interest rate, and amount.

# Usage
Let's say, for example, you want to calculate payments on a 10 year 30k loan with 6% interest. You can run the following command:

```
docker run -it joekrinke15/app python app.py  --amount 30000 --term 10 --interest .06

Output:
Your estimated monthly payment is: $333.06. You will pay $9967.38 in interest and $39967.38 total.
```
