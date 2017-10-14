# Accessing Values in Strings
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

# Updating Strings
var1 = 'Hello World!'

print "Updated String :- ", var1[:6] + 'Python'

# String Formatting Operator
print "My name is %s and age is %d years!" % ('Sid', 26)

# Unicode String
print u'Hello, world!'

#------------ Built-in String Methods -------------
# capitalize() ------ Capitalizes first letter of string
str = "this is string example....wow!!!";
print str
print "str.capitalize() : ", str.capitalize()

# center(width,fillchar) ---- Returns a space-padded string with the original string centered to a total of width columns.
print "str.center(40, 'a') : ", str.center(40, 'a')

# count(str, beg= 0,end=len(string))
# Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

# decode(encoding='UTF-8',errors='strict')
# Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.
Str = "this is string example....wow!!!";
Str = Str.encode('base64','strict');

print "Encoded String: " + Str
print "Decoded String: " + Str.decode('base64','strict')

# encode(encoding='UTF-8',errors='strict')
# Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.
print "Encoded String: " + str.encode('base64','strict')

# endswith(suffix, beg=0, end=len(string))
# Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
suffix = "wow!!!";
print str.endswith(suffix)
print str.endswith(suffix,20)

suffix = "is";
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

# expandtabs(tabsize=8)
# Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.
str = "this is\tstring example....wow!!!";
print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)

# find(str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 16, 40)

# index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.
print str1.index(str2)
print str1.index(str2, 10)
print str1.index(str2, 15, 40)

# isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
str = "this2009";  # No space in this string
print str.isalnum()

str = "this is string example....wow!!!";
print str.isalnum()

# isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
str = "this";  # No space & digit in this string
print str.isalpha()

str = "this is string example....wow!!!";
print str.isalpha()

# isdigit() --- Returns true if string contains only digits and false otherwise.
str = "123456";  # Only digit in this string
print str.isdigit()

str = "this is string example....wow!!!";
print str.isdigit()

# islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
str = "THIS is string example....wow!!!"; 
print str.islower()

str = "this is string example....wow!!!";
print str.islower()

# isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.
str = u"this2009";  
print str.isnumeric()

str = u"23443434";
print str.isnumeric()

# isspace()
# Returns true if string contains only whitespace characters and false otherwise.

str = "       "; 
print str.isspace()

str = "This is string example....wow!!!";
print str.isspace()

# istitle()
# Returns true if string is properly "titlecased" and false otherwise.

str = "This Is String Example...Wow!!!";
print str.istitle()

str = "This is string example....wow!!!";
print str.istitle()

# isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
str = "THIS IS STRING EXAMPLE....WOW!!!"; 
print str.isupper()

str = "THIS is string example....wow!!!";
print str.isupper()

# join(seq)
# Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

# len(string) ------ Returns the length of the string
str = "this is string example....wow!!!";

print "Length of the string: ", len(str)

# ljust(width[, fillchar])
# Returns a space-padded string with the original string left-justified to a total of width columns.
str = "this is string example....wow!!!";

print str.ljust(50, '0')

# lower() ------ Converts all uppercase letters in string to lowercase.
str = "THIS IS STRING EXAMPLE....WOW!!!";

print str.lower()

# lstrip() ------ Removes all leading whitespace in string.
str = "     this is string example....wow!!!     ";
print str.lstrip()
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8')

# maketrans() ----- Returns a translation table to be used in translate function.
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)

# max(str) ----- Returns the max alphabetical character from the string str.
str = "this is really a string example....wow!!!";
print "Max character: " + max(str)

str = "this is a string example....wow!!!";
print "Max character: " + max(str)

# min(str) ----- Returns the min alphabetical character from the string str.
str = "this-is-real-string-example....wow!!!";
print "Min character: " + min(str)

str = "this-is-a-string-example....wow!!!";
print "Min character: " + min(str)

# replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.
str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 2)

# rfind(str, beg=0,end=len(string)) ----- Same as find(), but search backwards in string.
str1 = "this is really a string example....wow!!!";
str2 = "is";
print str1.rfind(str2)

print str1.rfind(str2, 0, 10)
print str1.rfind(str2, 10, 0)

print str1.find(str2)
print str1.find(str2, 0, 10)
print str1.find(str2, 10, 0)

# rindex( str, beg=0, end=len(string)) ---- Same as index(), but search backwards in string.
str1 = "this is string example....wow!!!";
str2 = "is";

print str1.rindex(str2)
print str1.index(str2)

# rjust(width,[, fillchar])
# Returns a space-padded string with the original string right-justified to a total of width columns.
str = "this is string example....wow!!!";

print str.rjust(50, '0')

# rstrip() ------ Removes all trailing whitespace of string.
str = "     this is string example....wow!!!     ";
print str.rstrip()
str = "88888888this is string example....wow!!!8888888";
print str.rstrip('8')

# split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and 
# returns list of substrings; split into at most num substrings if given.
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )

# splitlines( num=string.count('\n'))
# Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str.splitlines( )
print str.splitlines( 0 )
print str.splitlines( 3 )
print str.splitlines( 4 )
print str.splitlines( 5 )

# startswith(str, beg=0,end=len(string))
# Determines if string or a substring of string (if starting index beg and
# ending index end are given) starts with substring str; returns true if so and false otherwise.
str = "this is string example....wow!!!";
print str.startswith( 'this' )
print str.startswith( 'is', 2, 4 )
print str.startswith( 'this', 2, 4 )
 
# strip([chars]) ------ Performs both lstrip() and rstrip() on string
str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' )

# swapcase() ----- Inverts case for all letters in string.
str = "this is string example....wow!!!";
print str.swapcase()

str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.swapcase()

# title() ---------- Returns "titlecased" version of string, 
# that is, all words begin with uppercase and the rest are lowercase.
str = "this is string example....wow!!!";
print str.title()

# translate(table, deletechars="")
# Translates string according to translation table str(256 chars), removing those in the del string.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab)

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab, 'xm')

# upper() ------ Converts lowercase letters in string to uppercase.
str = "this is string example....wow!!!";

print "str.capitalize() : ", str.upper()

# zfill (width) ---- Returns original string leftpadded with zeros to a total of width characters; 
# intended for numbers, zfill() retains any sign given (less one zero).
str = "this is string example....wow!!!";

print str.zfill(40)
print str.zfill(50)

# isdecimal() ---- Returns true if a unicode string contains only decimal characters and false otherwise.

str = u"this2009";  
print str.isdecimal();

str = u"23443434";
print str.isdecimal();