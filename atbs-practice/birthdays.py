birthdays = {'Allison': 'August 12', 'Sheila': 'January 5',
              'Richard': 'September 27', 'Stephane': 'September 3', 'Lawrence': 'May 1'}
while True:
    print('Enter a family name to check their birthday, enter nothing to quit')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + "'s birthday is " + birthdays[name] + '\n')
    else:
        print('This name is not registered \n When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('This birthday has been added')