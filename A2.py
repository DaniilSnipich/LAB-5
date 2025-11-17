import re

text = 'He jests at scars. That never felt a wound!   Hello, friend!   Are you OK?'
sentences = re.split(r'(?<=[.?!]) +', text)

def stroki (items):
    for item in items:
        print(item)

stroki(sentences)
print(f'Предложений в тексте: {len(sen)}')


