from arrStr import arrStr
from strArr import strArr
from getLetter import getLetter
import re

ap = '’'
# print(ap)
# print(ord('’'))
# apos= chr(8217)

def longestPalindrome(string):
  
  lowstr = string.lower()
  lowstr = re.sub('[^\w]','',lowstr)
  # r = lowstr[::-1]
  length = len(lowstr)

  straight = lowstr[10:length-1]
  # print(lowstr[10:length-1])

  # print(straight[::-1])

  while length > 0:
    for i in range(len(lowstr)):
      straight = lowstr[i:length-i]
      reverse = straight[::-1]
      if straight == reverse and len(straight) > 1:
        # print(straight)
        return straight
    length -= 1
  


  #start with small slice at least 2 elements, if reversed is equivalent, check the slice with 3 elements, till it no longer matches reversed.  then store that in the longpal var.longpal 
  



#trying various inputs to test the function

sentence = open('sentence.txt')
s = sentence.read()
sentence.close()

str1 = 'Madam In Eden, I’m Adam'
rand = arrStr([getLetter() for i in range(10)])

teststring = rand + str1 + rand

longtest = rand + s + rand
x = longestPalindrome(longtest)
print('the worlds longest palindrome:', len(x), 'letters long')

l = longestPalindrome(teststring)
print(l)








