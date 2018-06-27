# PaymentSplit
Splitting of group expenses with Python.

## How to format your input.txt file.
The first line should be the first names of all involved, seperated by a space.
~~~~
shane maneesh cliff angelo
~~~~

The following lines are for expenses. This is the format:
~~~~
[item] [amount] [who paid] [who needs to pay]
~~~~

So if Shane paid $25 for an Uber and Angelo, Maneesh, and Cliff all rode, it would look like this:
~~~~
uber 25 shane angelo maneesh cliff
~~~~

If Cliff paid $260 for dinner that Maneesh and Shane also enjoyed, it would look like this:
~~~~
dinner 260 cliff maneesh shane
~~~~

The file should be a .txt file. Look at `input.txt` for a complete input file example.


## How to run
~~~~
python3 calculate.py input.txt
~~~~


## Example input.txt
~~~~
shane maneesh cliff angelo
ponce 60 shane maneesh cliff angelo
dinner 260 cliff maneesh shane 
uber 25 shane maneesh angelo cliff 
other 60 cliff shane
~~~~

## Example output
~~~~
Transactions:
ponce, $60.0
dinner, $260.0
uber, $25.0
other, $60.0
total: $405.0

Who owes who:
maneesh owes shane: $21.25
shane owes cliff: $95.42
angelo owes shane: $21.25
maneesh owes cliff: $86.67

Result:
shane pays cliff: $52.92
angelo pays cliff: $21.25
maneesh pays cliff: $107.92
~~~~