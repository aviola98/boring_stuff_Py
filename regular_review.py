import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4242')
print('phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

mo.groups()

areaCode, mainNumber=mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

heroRegex.findall('Batman and Tina Fey')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
mo2 == None

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyRegex.search('HaHaHaHaHa')
print(mo2.group())

#findall() Method
#using search it will only return the first match
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

#findall() will return a list of strings (as long as there are no groups in the regular expression)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#if there are any groups in the regular expression, findall() will return a list of tuples

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#summarizing 
#when called on a Regex with no groups it will return a list of string matches 
#when called on a Regex that has groups it will return a list of tuples of strings

#matching text that has one or more numeric digits (\d+)
#followed by a whitespace character (\s)
#followed by one or more letter (\w+)
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers,9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 bens, 2 doves, 1 partridge')

#defining my own character class
#e.g. [aeiouAEIOU] 

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD')

#e.g. [a-zA-Z0-9] will match all lowercase letters, uppercase letters and numbers
#By placing a caret character (^) just after the character class’s opening
#bracket, you can make a negative character class.

vowelRegex = re.compile(r'[^aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD')

# use ^ to indicate that a match must occur at the beggining of the searched text
# use $ to indicate that a match must occur at te end
# use both to indicate that the entire string must match the regex

begins_with_hello = re.compile(r'^Hello')
begins_with_hello.search('Hello World')

begins_with_hello.search('He said hello') == None

ends_with_number = re.compile(r'\d$')
ends_with_number.search('Your Number is 45')
ends_with_number.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')

#the . character in a regular expression is called a wildcard and will match any character except for a new line

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
#to match an actual dot escape the dot with \ like \.

#Matching Everything with Dot-Star

matchname = re.compile(r'First name: (.*) Last Name: (.*)')
mo = matchname.search(r'First name: Andre Last Name: Viola')
mo.group(1)
mo.group(2)

#To match any and all text in a nongreedy fashion, use the dot, star,
#and question mark (.*?). 

nongreedy= re.compile(r'<.*?>')
mo = nongreedy.search('<To serve man> for dinner.>')
mo.group()

greedy = re.compile(r'<.*>')
mo = greedy.search('<To serve man> for dinner.>')
mo.group()

#y passing re.DOTALL as
#the second argument to re.compile(), you can make the dot character match
#all characters, including the newline character

no_new_line = re.compile('.*')

no_new_line.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()


new_line = re.compile('.*', re.DOTALL)
new_line.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()


#using re.IGNORECASE or re.I to match letters no matter the case

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

#Substituting Strings with the sub() Method
#The first argument is a string to replace any matches.
#The second is the string for the regular expression.

names = re.compile(r'Agent \w+')
names.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')


#censoring the names of the secret agents by
#showing just the first letters of their names.



agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

#verbose mode

phoneRegex = re.compile(r'''(
(\d{3}|\d{3}))? #areacode
(\s|-|\.)? #separator
\d{3} #first 3 digits
(\s|-|\.)  #separator
\d{4} #last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? #extension
)''', re.VERBOSE)
                        
#uses the triple-quote syntax (''') to
#create a multiline string so that you can spread the regular 
#expression definition over many lines, making it much more legible

#bitwise or operator |

some_regex_value = re.compile('foo',re.I|re.DOTALL|re.VERBOSE)
