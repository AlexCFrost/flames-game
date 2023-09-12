name1 = input("Your😎 Name: ").upper()
name2 = input("Your Crush😘 Name: ").upper()
for char in name1:
    if char in name2:
        name1 = name1.replace(char, '', 1)
        name2 = name2.replace(char, '', 1)

flames = list("flames")

while len(flames) > 1:
    char_index = (len(name1) % len(flames)) - 1
    if char_index >= 0:
        flames.pop(char_index)
    else:
        flames.pop(len(flames) - 1)

results = {
    'f': 'Friendship',
    'l': 'Love',
    'a': 'Affection',
    'm': 'Marriage',
    'e': 'Enmity',
    's': 'Sibling'
}

result = results[flames[0].lower()]
print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {result}")
