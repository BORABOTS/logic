"""1. Write a python program to display a user entered name followed by Good Afternoon using
input() function."""
name=input('enter name: ')
print('Good Afternoon ',name)

"""
2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""
letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
    '''
replaced=letter.replace("<|Name|>","harry").replace("<|Date|>","5-sep-2025")
print(replaced)
"""
3. Write a program to detect double space in a string.
"""
name='harry  pajji'
print(name.find("  "))
"""
4. Replace the double space from problem 3 with single spaces.
"""
name='My name is harry  pajji'
print(name.find(" "))
"""
5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"""
letter = "Dear Harry,\n\t this python course is nice.\n Thanks!"
print(letter)
