import re

def example_word_count():
    example_string = "Amy is 5 years old"
    

    result = example_string.split(" ")
    return len(result)



print(example_word_count()) 


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

  
    result=re.findall("[A-Z][\w]*",simple_string)
    return result
   


print(names())

assert len(names()) == 4, "There are four names in the simple_string"

def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
    result=re.findall("[A-Z]\w*\s[A-Z]\w*(?=[:]\s[B])",grades)
    return result

print(grades())
print(len(grades()))

assert len(grades()) == 16, "should len be 16"

def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
    

        pattern=""" (?P<host>\d{0,9}[.]\d{0,9}[.]\d{0,9}[.]\d{0,9})
                    (\s[-]\s)
                    (?P<user_name>(\w*|[-]))
                    (\s[\[])
                    (?P<time>\d{0,2}[\/][a-zA-Z]*[\/]\d{0,4}[:]\d{0,2}[:]\d{0,2}[:]\d{0,2}\s[-]\d{0,9})
                    ([\]]\s["])
                    (?P<request>\w*\s\S*\s\w*[\/]\d{0,5}[.]\d{0,5})
                    """
 
    logsList = list()

    for item in re.finditer(pattern,logdata,re.VERBOSE):
        logsList.append(item.groupdict())
    return logsList

# print(logs())
print(len(logs()))
assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
