import re


grades="ACAAAABCBCBAA"

print("find B: ",re.findall("B",grades))

print("find A and B : ",re.findall("[AB]",grades))

print("find where an A followed by a B or a C: ",re.findall("[A][B-C]",grades))

print("you can write previous pattern by using the pipe operator, which means OR: ",re.findall("AB|AC",grades))
print("grades which were not A's ",re.findall("[^A]",grades))
print("^[^A]: ",re.findall("^[^A]",grades))
print("back-to-back A's streak: ",re.findall("A{2,10}",grades))
print(" re.findall(\"A\{1,1\}A\{1,1\}\",grades)  : ",re.findall("A{1,1}A{1,1}",grades))
print(" re.findall(\"A\{2, 2\}\",grades)  : ",re.findall("A{2, 2}",grades))
print(" re.findall(\"A\{2\}\",grades)  : ",re.findall("A{2}",grades))
print(" find a decreasing trend: ",re.findall("A{1,10}B{1,10}C{1,10}",grades))


print("####################")
print("####################")
print("####################")
print("####################")
print("####################")

with open("datascience.txt","r") as file:
    wiki=file.read()

print(wiki)

print("find [edit], [a-zA-Z]{1,100}\[edit\]: ",re.findall("[a-zA-Z]{1,100}\[edit\]",wiki))
print("find [edit], [\w]{1,100}\[edit\] : ",re.findall("[\w]{1,100}\[edit\]",wiki))
print("find [edit], [\w ]*\[edit\] : ",re.findall("[\w ]*\[edit\]",wiki))

for title in re.findall("[\w]*\[edit\]",wiki):
    print(re.split("[\[]",title)[0])