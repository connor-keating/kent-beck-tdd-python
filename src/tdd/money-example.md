# Part 1: The Money Example

## Requirements
As we all know requirements change as soon as they arrive, so as a developer you need to be able to respond to those changes quickly without breaking the existing system. This project follows one such example.

Suppose you have the following report. 

Instrument | Shares | Price | Total
---|---|---|---
IBM | 1000 | 25 | 25000
GE | 400 | 100 | 40000

Total = 65000

A customer comes to you and requests that you be able to to create a  multi-curency report. This is a **story point**. In order to generate value to the customer you'll need to have...
Instrument | Shares | Price | Total
---|---|---|---
IBM | 1000 | 25 USD | 25000 USD
Novartis | 400 | 150 CHF | 60000 CHF

Total = 65000 USD

You'll need to specify exchange rates

From | To | Rate 
---|---|---
CHF | USD | 1.5


## To-Dos
Take the story and create action items for how to solve the customer's problem. 

The To-Do list keeps us focused on the project goals. As you finish items on the list cross them off. Don't be afraid to add more items to your list.

Remember to work in small bite sized chunks and follow the rules of TDD. They'll take awhile to sink in!

- Add two amounts in two different currencies and convert the result given a set of exchange rates.
- Multiply an amount (price per share) by a number (number of shares) and recieve an amount.

- $5 + 10 CHF = $10 if rate is 2:1
- $5 * 2 = $10
- Make "amount" private
- Dollar side effects?
- Money rounding?