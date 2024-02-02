import re

# as we know that python is case-sensitive.
matching = re.search(r"shiv", "Shiv", re.IGNORECASE)

print(matching)

# output : <re.Match object; span=(0,4), match='Shiv'>