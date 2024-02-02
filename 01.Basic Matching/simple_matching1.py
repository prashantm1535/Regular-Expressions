import re
matching = re.search(r"World", "Hello, World!")

# note : matching is case-sensitive.

print(matching)

# output : <re.Match object; span=(7,12), match='World'>