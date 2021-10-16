import re

with open("datascience.txt","r") as file:
    wiki=file.read()

print(" ([\w ]*)(\[edit\]): )  : ",re.findall("([\w ]*)(\[edit\])",wiki))

print("####################")

for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))
print("last dict kept for the last match: ",item.group())
print("####################")

for item in re.finditer("(?P<title>[\w]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict()['title'])

print("last dict kept for the last match: ",item.groupdict())

print("####################")
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    # What this regex says is match two groups, the first will be named and called title, will have any amount
    # of whitespace or regular word characters, the second will be the characters [edit] but we don't actually
    # want this edit put in our output match objects
    print(item)
