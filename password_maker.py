def domain_check(username):
    '''makes sure doman is correct'''
    
    valids = False
    if '@' in username:
        split = username.split('@')
        if split[1] == 'gmail.com':
            valids = True
    return valids

def user_space_check(username):
    '''makes sure no space in username'''

    valids = False
    for i in username:
        if i.isspace():
            valids = True
    return valids

def user_space_check(password):
    '''makes sure no spaces in password'''

    valids = False
    for i in password:
        if i.isspace():
            valids = True
    return valids
    
def length_check(password):
    '''makes sure lenght is >= 8'''
    
    valids = False
    if len(password) >= 8:
        valids = True
    return valids

def digit_check(password):
    '''makes sure atleast one digit in password'''
    
    valids = False
    for run in password:
        if run.isdigit():
            valids = True
    return valids

def capital_check(password):
    '''makes sure atleast one capital in password'''
    
    valids = False
    for letter in range(len(password)):
        if password[letter].isupper():
            valids = True
    return valids

def special_check(password):
    '''makes sure atleast one special character in password'''
    
    valids = False
    for letter in range(len(password)):
        if password[letter].isalnum():
            valids = True
    return valids

def main():
    

    validFirst = False
    while not validFirst:
        username = input('Enter your username: ')
        domain = domain_check(username)
        space_one = user_space_check(username)
        validFirst = True
        if domain == False or space_one == True:
            print('Username not valid. Domain name should be gmail.com, and no spaces allowed.')
            validFirst = False


    validSecond = False
    while not validSecond:
        password = input('Enter your password. It needs to be 8 characters long, and contain atleast one digit, capital letter, and special character: ')
        space_second = user_space_check(password)
        length = length_check(password)
        digit = digit_check(password)
        capital = capital_check(password)
        special = special_check(password)
        validSecond = True
        if space_second is True or length is False or digit is False or capital is False or special is False:
            print('Program does not meet requirements.')
            validSecond = False
    print('Congratulations. Registration completed!')


if __name__ == "__main__":
    main()


