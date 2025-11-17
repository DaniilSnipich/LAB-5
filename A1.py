text = str(input())

while '(' in text:
        position1 = text.find('(')
        position2 = text.find(')', position1)
