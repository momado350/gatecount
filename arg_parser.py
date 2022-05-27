# An Example of how to parse command line arguments in streamlit. 
# This is free and unencumbered software released into the public domain.
import os
import sys
import random
import argparse
import streamlit as st

parser = argparse.ArgumentParser(description='This app lists animals')

parser.add_argument('--animal', action='append', default=[],
                    help="Add one or more animals of your choice")
sort_order_choices = ('up', 'down', 'random')
parser.add_argument('--sort', choices=sort_order_choices, default='up',
                    help='Animal sort order (default: %(default)s)')
parser.add_argument('--uppercase', action='store_true',
                    help='Make the animals bigger!')
try:
    args = parser.parse_args()
except SystemExit as e:
    # This exception will be raised if --help or invalid command line arguments
    # are used. Currently streamlit prevents the program from exiting normally
    # so we have to do a hard exit.
    os._exit(e.code)

st.title("Command line example app")
st.markdown("""
Your current command line is:
```
{}
```
A double dash (`--`) is used to separate streamlit arguments from app arguments.
As a result
```
streamlit run command_line.py --help
```
will show the help for streamlit and
```
streamlit run command_line.py -- --help
```
will show the help for this app. Try
```
streamlit run command_line.py -- --animal dog --animal cat --sort down
```
to see it in action.
""".format(sys.argv))

# Built in animals
animals = ['Albatross', 'Bison', 'Dragonfly', 'Shark', 'Zebra']

# Add one or more animals supplied on command line
animals += args.animal

# Set default sort order from command line option
sort_order = st.selectbox("Sort order", sort_order_choices,
                          sort_order_choices.index(args.sort))
if sort_order == 'up':
    animals.sort()
elif sort_order == 'down':
    animals.sort(reverse=True)
elif sort_order == 'random':
    random.shuffle(animals)
else:
    # This can't happen unless you add more values to sort_order_choices
    raise ValueError("Invalid sort order")

# Set checkbox default from command line
uppercase_animals = st.checkbox("Uppercase", args.uppercase)
if uppercase_animals:
    animals = [animal.upper() for animal in animals]

# Show the results
st.header("You list of animals")
st.dataframe(animals)