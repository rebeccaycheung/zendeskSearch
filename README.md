# Zendesk Coding Challenge

Requirements
------
Python version 3.3+.

How to run the program:
------
    $ ./main.py

This search program lets you search by users, organisations and/or tickets. Start off by selecting which category you want to search by, i.e:
- Type 1 for users
- Type 2 for organisations
- Type 3 for tickets

Then once a category has been selected, choose a term and value that you want to search by.

If you do not know what terms you can search by for each category then type 'terms' when prompted for a term to view a list of terms.

Type 'quit' to exit the program at any time.

How to run tests
------
    $ ./setup.sh
    $ pytest
    or if above command does not work
    $ python3 -m pytest

Example output: see exampleOutput.txt
