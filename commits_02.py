password = input ('Do you know the secret password?')
if password != '--secret':
    print('not correct')
else:
    print('correct password')
    

    
user_age = int(input('What is your age?'))
user_country = input ('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programme')
else:
    print ('Sorry, you do not qualify')
    





        