import re

with open("buddhist.txt","r") as file:
    wiki = file.read()

print(wiki)

pattern="""
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in"""

for item in re.finditer(pattern,wiki,re.VERBOSE):
    print(item.groupdict())


print("####################")

print("####################")

print("####################")

text = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'

pattern="(?<=[https]:\/\/)([A-Za-z0-9.]*)"

print(re.findall(pattern,text))

print("####################")

print("####################")

print("####################")

with open("phoneNumbers.txt") as file:
    phones=file.read()
print(phones)

pattern="[(]\d{3}[)]\s\d{3}[-]\d{4}"
print(re.findall(pattern,phones))