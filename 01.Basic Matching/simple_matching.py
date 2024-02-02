import re
matching = re.search(r"Hello", "Hello, How are you?")
print(matching)

# here re.search() is method
# r - is raw string used along with string which is going to find.
""" 
    note : matching is case-sensitive. 
    if we are matching small letter with capital then output will be "None".
"""

# output : <re.Match object; span=(0,5), match='Hello'>