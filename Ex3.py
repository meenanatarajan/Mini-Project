import re
def text_match(text):
        #Add your code here
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("abbbbbcccc"))
print(text_match("aabbbbbc"))
