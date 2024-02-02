# Import the necessary library
import re

text = "I have no special talents. I am only passionately curious."

# Use search function to search for the literal word "curious"
match = re.search(r"curious", text)

# Printing match
print(match)