# PaymentSplit
Splitting of group expenses.

# Why
[https://kittysplit.com/excel/hwwrkvMXC04K9Oo9QU1WK8JlA30dpnhR-2](https://kittysplit.com/excel/hwwrkvMXC04K9Oo9QU1WK8JlA30dpnhR-2)

[billzer.com/my/e23cafacdfc5adcb3f1e084c2bccbfbc](billzer.com/my/e23cafacdfc5adcb3f1e084c2bccbfbc)


## How to format input.txt
The first line should be the first names of all involved, seperated by a space.
~~~~
shane maneesh cliff angelo
~~~~

The following lines are for expenses. This is the format:
~~~~
[item] [who paid] [who needs to pay] [amount]
~~~~

So if Shane paid $25 for an Uber and Angelo, Maneesh, and Cliff all rode, it would look like this:
~~~~
uber shane angelo maneesh cliff 25
~~~~

If Cliff paid $260 for dinner that Maneesh and Shane also enjoyed, it would look like this:
~~~~
dinner cliff maneesh shane 260
~~~~

Look at `input.txt` for a complete input file.


## How to run
~~~~
python3 calculate.py
~~~~


## Example input
~~~~
shane maneesh cliff angelo
ponce shane maneesh cliff angelo 60
dinner cliff maneesh shane 260
uber shane maneesh angelo cliff 25
other cliff shane 60
~~~~

## Example output
~~~~
---Transactions:
ponce, $60
dinner, $260
uber, $25
other, $60

---Pre-optimized:
maneesh pays shane: $21.25
shane pays cliff: $95.42
angelo pays shane: $21.25
maneesh pays cliff: $86.67

---Optimized:
shane pays cliff: $53
angelo pays cliff: $21
maneesh pays cliff: $108
~~~~