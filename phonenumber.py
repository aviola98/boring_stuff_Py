def isPhoneNumber(text):
    #checking that the string is exactly 12 characters
    if len(text)!=12:
        return False
    #checking if the area code consists of only numeric characters
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        #checking if it has hyphen after the area code
        if text[3] != '-':
            return False
        #checking three more numeric characters
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
            #checking another hyphen
            if text[7] != '-':
                return False
            #three more numeric characters
            for i in range(8,12):
                if not text[i].isdecimal():
                    return False
            return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))

print('Moshi moshi is a phone number: ')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
















#import regex

import re 

#creating a regex object using re.compile
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#passing the string you want, this returns a match object
mo = phoneNumRegex.search('My number is 415-555-4242')
#call the match object's group() method to return a string of the actual matched text
print('Phone number found: ' + mo.group())
