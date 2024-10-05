import type1

print('''Type 1: Take large clip (3m) and 
      divide it into smaller 6 second clips then join them''')
print("/n")
print('Type 2: Take small clip (15~60s) and add a subtitle, music and speech')
typeOfUse = int(input('Which type do you want?'))

if typeOfUse == 1:
    type1.movie()
elif typeOfUse == 2:
    print('hey')
else:
    print('Only type either 1 or 2')