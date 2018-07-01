# Get file name from first argument
import sys
fileName = sys.argv[1]

# Colors for printing
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'
    BOLD = '\033[1m'

# Get data from file and store in transactions array
allTransactions = []
with open(fileName,'r') as f:
		for line in f:								# For each line in file
			if "~" != line[0]:						# If not a comment
				transaction = []					# Array to store transaction
				for word in line.split():			# Break down by word
					transaction.append(word)		# Append to array
				allTransactions.append(transaction)	# Append to all transactions

# Get names from first row in file, remove from list
names = allTransactions.pop(0)

# Create list of items with [ pays, to, amount ] for every combination
payments = []
for n1 in names:
	for n2 in names:
		if n1 != n2:				# Exclude self
			group = [n1, n2, 0]		# [Pays, To, Amount]
			payments.append(group)

# Analyze each transaction
total = 0
print(colors.PURPLE + "\nTransactions:" + colors.END)
for transaction in allTransactions:
	item = transaction.pop(0)			# Get item from start of line
	cost = float(transaction.pop(0))	# Get total cost from end of line
	people = len(transaction) 			# Get number of people involved
	costPer = round(cost / people, 2)	# Get cost per person
	owner = transaction.pop(0) 			# Get who paid

	print(item + ", " + colors.GREEN +"$"+ str(cost) + colors.END)
	total += cost

	# Loop through payments and add to cost
	for name in transaction:
		for group in payments:
				# Find [Pays, To, Amount] that matches
				if group[0] == name and group[1] == owner:
					group[2] += costPer	# Add cost

# Print total
print(colors.GREEN + colors.BOLD + "total: $"+str(total) + colors.END)

# Settle between eachother
# If X owes Y and Y owes X, settle
for g1 in payments:
	for i, g2 in enumerate(payments):
		if g1[0] == g2[1] and g1[1] == g2[0]:	# If owe eachother
			g1[2] -= g2[2]						# Subtract second from first 
			
			# If negative, switch name order and payment
			if g1[2] < 0:
				tempName = g1[1]
				g1[1] = g1[0]
				g1[0] = tempName
				g1[2] = -g1[2]

			# Remove empty duplicate
			del payments[i]

# Print who owes who (before optimizations)
print(colors.PURPLE + "\nWho owes who:" + colors.END)
for group in payments:
	if group[2] != 0: # If not blank
		print(group[0] + " owes " + group[1] + ": " + colors.GREEN + "$" + str(round(group[2],2)) + colors.END)

# Optimize for tri-relationships
# Where: X owes Y, Y owes Z, X owes Z
for g1 in payments:
	for g2 in payments:
		for g3 in payments:
			# If X owes Y, Y owes Z, X owes Z
			if g1[0] == g3[0] and g1[1] == g2[0] and g2[1] == g3[1]:
				# If first costs less than second
				if g1[2] <= g2[2]:
					g2[2] -= g1[2]		# Decrease payment
					g3[2] += g1[2]		# Increase payment
					g1[2] = 0			# Set to 0
				
				# If first cost more than second
				if g1[2] >= g2[2]:
					g1[2] -= g2[2]	# Decrease payment
					g3[2] += g2[2]	# Increase payment
					g2[2] = 0 		# Set to 0

# Optimize for bi-relationships
# Where: X owes Y and Z owes X: Make Z pay Y
for g1 in payments:
	for g2 in payments:
		if g1[0] == g2[1]:		# If payer in g1 is payee of g2
			if g1[2] > g2[2]:
				g1[2] -= g2[2] 	# Subtract
				g2[1] = g1[1]	# Switch pay-to

print(colors.PURPLE + "\nResult:" + colors.END)
for group in payments:
	if group[2] != 0: # If not blank
		print(colors.BLUE + group[0] + colors.END +" pays " + colors.BLUE + group[1] + colors.END + ": " + colors.GREEN + "$" + str(round(group[2],2)) + colors.END)

print("") # Add space