import re

matching = re.search(r"P.n", "Do you have a Ball Pen?")
matching1 = re.search(r"B..k", "Please, give the Book.")

# note : matching is case-sensitive.

print(matching)
print(matching1)

# output1 : <re.Match object; span=(19,22), match='Pen'>
# output2 : <re.Match object; span=(17,21), match='Book'>