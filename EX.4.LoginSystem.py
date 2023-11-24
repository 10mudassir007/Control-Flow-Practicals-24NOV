#taking username and password as input
input_username = input('Enter Username: ')
input_password = input('Enter Password: ')
#checking if username and password are correct if yes then login otherwise login failed
if input_username == 'admin' and input_password == '12345':
    print('Login Successful')
else:
    print('Login Failed')

