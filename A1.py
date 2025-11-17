text = str(input())

while '(' in text:
        position1 = text.find('(')
        position2 = text.find(')', position1)

if position2 != 1:
            text = text.replace(text[position1:position2 + 1], '')
