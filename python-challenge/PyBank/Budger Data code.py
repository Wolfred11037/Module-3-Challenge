import csv

# loation of the csv file Budget_ Data
filename = r"C:\Users\Wolfred\Documents\Data Analysis Boot Camp\Week 3\python-challenge\PyBank\Resources\budget_data.csv"
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    data = list(csv_reader)

# delaring tne variables
total_months = len(data)
net_total = 0
changes = []
max_increase = 0
max_decrease = 0

for i in range(total_months):
    date = data[i][0]
    profit_loss = int(data[i][1])

    # Calculaig the total
    net_total += profit_loss

    # Calculating changes in profits and losses
    if i > 0:
        change = profit_loss - int(data[i - 1][1])
        changes.append(change)

        # Checking for the greatest increase and decrease
        if change > max_increase:
            max_increase = change
            max_increase_date = date
        elif change < max_decrease:
            max_decrease = change
            max_decrease_date = date

# Calculating the average changes
average_change = sum(changes) / len(changes)

# displaying the results as shown in the challenge
output = f"Financial Analysis\n----------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${net_total}\n"
output += f"Average Change: ${average_change:.2f}\n"
output += f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
output += f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})"

print(output)
