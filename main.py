from pyscript import display, document

def verify_account(e):
    document.getElementById('output').innerHTML = ' '

    user = document.getElementById('username').value
    password = document.getElementById('password').value

    user_count = 0
    user_good = False

    for char in user:
        user_count += 1

    if user_count >= 7:
        user_good = True
    else:
        display(f'Username must be at least 7 characters', target='output')
        return
    

    letter = False
    number = False
    count = 0

    for char in password:
        count += 1
        if char.isalpha():
            letter = True
        if char.isdigit():
            number = True

    if count < 10:
        display(f'Password must be at least 10 characters', target='output')
    elif not letter:
        display(f'Password must contain at least 1 letter', target='output')
    elif not number:
        display(f'Password must contain at least 1 number', target='output')
    else:
        display(f'Account successfully created!', target='output')