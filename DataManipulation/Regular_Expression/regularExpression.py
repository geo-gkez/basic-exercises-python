import re

text = "This is good programming"
print(text)

if re.search(" good",text):
    print("Wonderful!")

else:
    print("Alias :(")

print("####################")

text = "Sonja works diligently. Sonja gets good grades. Our student Sonja is succesful."

print(text)

print("re.split(Sonja,text): ",re.split("Sonja",text))

print("re.findall(Sonja,text): ",re.findall("Sonja",text))

print("re.search(\"^Sonja\",text): ",re.search("^Sonja",text))