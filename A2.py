import re

text = 'He jests at scars. That never felt a wound!   Hello, friend!   Are you OK?'
sen = re.split(r'(?<=[.?!]) +', text)
