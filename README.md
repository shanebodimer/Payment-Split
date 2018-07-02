# PaymentSplit
Splitting of group expenses with Python.

## How to format your input.txt file
The first line should be the first names of all involved, seperated by a space.
~~~~
shane maneesh cliff angelo
~~~~

The following lines are for expenses. This is the format:
~~~~
[item] [amount] [who paid] [who owes for purchase]
~~~~

So if Shane paid $25 for an Uber and Angelo, Maneesh, and Cliff all rode, it would look like this:
~~~~
uber 25 shane shane angelo maneesh cliff
~~~~

If Cliff paid $260 for dinner that Maneesh and Shane also enjoyed, it would look like this:
~~~~
dinner 260 cliff cliff maneesh shane
~~~~

If Cliff paid $100 for something Shane, it would look like this:
~~~~
thing 100 cliff shane
~~~~

You can also comment lines using the tilde character
~~~~
~ This is a comment!
~~~~

The file should be a .txt file. Look at `input.txt` for a complete input file example.


## How to run
~~~~
python3 calculate.py input.txt
~~~~

If you would like to round the values, pass it the following paramaters:
- Nothing does not round
- `r` to round normally
- `ru` to round up
- `rd` to round down

To round up would look like this:
~~~~
python3 calculate.py input.txt ru
~~~~

## Example input.txt
~~~~
shane maneesh cliff angelo
ponce 60 shane shane maneesh cliff angelo
dinner 260 cliff cliff maneesh shane 
~ This is a comment!
uber 25 shane shane maneesh angelo cliff 
other 60 cliff cliff shane
thing 100 cliff shane
~~~~

## Example output
~~~~
Transactions:
ponce, $60.0
dinner, $260.0
uber, $25.0
other, $60.0
thing, $100.0
total: $505.0

Who owes who:
shane owes cliff: $195.42
angelo owes shane: $21.25
maneesh owes shane: $21.25
maneesh owes cliff: $86.67

Result:
shane pays cliff: $152.92
maneesh pays cliff: $107.92
angelo pays cliff: $21.25
~~~~