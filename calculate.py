import sys
import math

# Colors for terminal printing
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'
    BOLD = '\033[1m'

# Parse arguments
round_by = False				# No round by preference set
if len(sys.argv) >= 2:			# Get file name from arguments
	file_name = sys.argv[1]
if len(sys.argv) >= 3:			# Get rounding preference
	round_by = sys.argv[2]
# if len(sys.argv) == 4:			# Get report
# 	generate_report == sys.argv[3]

# Get data from file and store in transactions array
all_transactions = []
with open(file_name,'r') as f:
		for line in f:								# For each line in file
			if "~" != line[0]:						# If not a comment
				transaction = []					# Array to store transaction
				for word in line.split():			# Break down by word
					transaction.append(word)		# Append to array
				all_transactions.append(transaction)# Append to all transactions

# Get names from first row in file, remove from list
names = all_transactions.pop(0)

# Print names
all_names = ""
print(colors.PURPLE + "\nParticipants:" + colors.END)
for name in names:									# Build list of names
	all_names += name + ", "
all_names = all_names[:-2]							# Trim last trailing comma
print(all_names)

# Create list of items with [ pays, to, amount ] for every combination
payments = []
for n1 in names:
	for n2 in names:
		#if n1 != n2:				# Exclude self
			group = [n1, n2, 0]		# [Pays, To, Amount]
			payments.append(group)

total = 0
print(colors.PURPLE + "\nTransactions:" + colors.END)
for transaction in all_transactions:	# Analyze each transaction
	item = transaction.pop(0)			# Get item from start of line
	cost = float(transaction.pop(0))	# Get total cost from end of line
	owner = transaction.pop(0) 			# Get who paid
	people = len(transaction) 			# Get number of people involved
	costPer = round(cost / people, 2)	# Get cost per person

	print(item + ", " + colors.GREEN +"$"+ str(cost) + colors.END + " (" + str(people) + ")")
	total += cost

	# Loop through payments and add to cost
	for name in transaction:
		for group in payments:
			# Find [Pays, To, Amount] that matches and not itself
			if group[0] == name and group[1] == owner and group[0] != group[1]:
				group[2] += costPer		# Add cost

# Print total
print(colors.GREEN + colors.BOLD + "total: $"+str(round(total,2)) + colors.END)
print(colors.GREEN + colors.BOLD + "avg per person: $"+str(round(total/people,2)) + colors.END)
print(str(len(all_transactions)) + " total expenses")

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
# print(colors.PURPLE + "\nWho owes who:" + colors.END)
# for group in payments:
# 	if group[2] != 0: # If not blank
# 		print(group[0] + " owes " + group[1] + ": " + colors.GREEN + "$" + str(round(group[2],2)) + colors.END)

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

		# Round
		amount = group[2]					# Get amount
		if round_by == "r":					# Round regular
			amount = round(group[2])
		elif round_by == "ru":				# Round up
			amount =  math.ceil(group[2])
		elif round_by == "rd":				# Round down
			amount = math.floor(group[2])
		else:								# No round
			amount = round(group[2],2)

		print(colors.BLUE + group[0] + colors.END +" pays " + colors.BLUE + group[1] + colors.END + ": " + colors.GREEN + "$" + str(amount) + colors.END)

print("") # Add space