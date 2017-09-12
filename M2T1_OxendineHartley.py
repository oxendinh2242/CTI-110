# CTI-110 
# M2T1 - Sales Prediction 
# Hartley Oxendine
# September 08, 2017
# This program calculates a profit from a percentage of total sales

# Get the projected sales.
total_sales=float(input('Enter the projected sales: '))

#Calculate the profit as 15 percent of total sales.
profit = total_sales * 0.15

#Display the profit
print('The profit is $', format(profit, ',.2f'))
