#import regex

import re 

#creating a regex object using re.compile
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#passing the string you want, this returns a match object
mo = phoneNumRegex.search('My number is 415-555-4242')
#call the match object's group() method to return a string of the actual matched text
print('Phone number found: ' + mo.group())
