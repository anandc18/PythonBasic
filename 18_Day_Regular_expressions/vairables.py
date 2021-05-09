import re;
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I', txt, re.I)
print(match)
span = match.span()
print(span)
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
