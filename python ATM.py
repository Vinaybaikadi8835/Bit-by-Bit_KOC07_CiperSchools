print ('Welcome to LPU ATM Services')
restart = 'Y'
chances = 3
balance = 100000
while chances >= 0:
    pin = int (input ('Please Enter You 4 Digit Pin: '))
    if pin == 1234:
        print ('You entered you pin Correctly\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print ('\nPlease Press 1 For Your Balance\n')
            print ('Please Press 2 To Make a Withdrawal\n')
            print ('Please Press 3 To Deposit\n')
            print ('Please Press 4 To Return Card\n')
            option = int (input ('What Would you like to choose? '))
            if option == 1:
                print ('\nYour Balance is ₹', balance, '\n')
                if balance<5000:
                    print ('You Have A Low Balance\n')
                restart = input ('Would You like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print ('***THANK YOU***')
                    break
            elif option == 2:
                option2 = 'y'
                withdrawal = float (input ('\nHow Much Would you like to withdraw? '))
                if 1 <= withdrawal < 100000:
                    balance = balance - withdrawal
                    print ('\nYour Balance is now ₹', balance)
                    restart = input ('\nWould You like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print ('***Thank You***')
                        break
                else:
                    print ('LOW BALANCE')
            elif option == 3:
                Deposit = float (input ('\nHow Much Would You Like To Deposit? '))
                balance = balance + Deposit
                print ('\nYour Balance is now ₹', balance)
                restart = input ('\nWould You like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print ('***Thank You***')
                    break
            elif option == 4:
                print ('\nPlease wait whilst your card is Returned...\n')
                print ('***Thank you for using our service***\n')
                break
            else:
                print ('Please Enter a correct number. \n')
                restart = 'y'
    elif pin != '1234':
        print ('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print ('\nNo more tries')
            break
