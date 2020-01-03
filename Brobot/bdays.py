import time

def checkTodaysBirthdays(): 
    birthdays = open('BirthdayFile.txt', 'r') 
    today = time.strftime('%m/%d') 
    bday = False
    for line in birthdays:
        date,name = line.split('-')
        if today==date:
            print(name,'has their Birthday today.')
            bday = True
    if bday:
        print('Wish them well!!')
    else:
        print('There are no bdays today.')
            
        

checkTodaysBirthdays()

