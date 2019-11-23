def login():
    log_or_sign = input('Do you want to log into an account or create one? (log/create) ')
    if log_or_sign == 'create':
        username = input('Username: ')
        newpass1= input('Password(number only): ')
        newpass2 = input('Confirm Passworrd: ')
        if newpass1 == newpass2:
            newpass = int(newpass1)
            newpass *= 132
            newpass = str(newpass)
            print ('Account Created Succesfully.')
            # f = open('loginInfo.txt','w')
            f = open('loginInfo.txt','a+') #Esto agrega en lugar de reescribir
            record = newpass + '_' + username + '\n' #El \n es para hacer un salgo de linea
            f.write(record)
            f.close()
        else:
            print('Both Passwords Must Match.')
    elif log_or_sign == 'log':
        username = input('Username: ')
        halfpass = input('Password: ')
        password = int(halfpass)
        password *= 132
        password = str(password)
        userpass = (password +'_' + username)
        f = open('loginInfo.txt','r')
        # info = (f.read())
        info = f.read().splitlines()
        f.close()
        encontre_record = False
        for record in info:
            if record == userpass:
                print('Access Granted, Welcome',username,"!")
                encontre_record = True
        if not encontre_record:
            print("That's Not A Valid Username Or Password.")
    else:
        print("That's not a valid answer. ")

if __name__ == "__main__":
    login()