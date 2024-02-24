bank_account_balance = 1000
max_attempts = 3
loop = 'yes'

print('Welcome to KC bank!')
print()
print(f'Bank Account Balance: ${bank_account_balance}')

while loop == 'yes':
    print()
    print('KC Bank Menu:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Exit')

    
    for attempt in range(1, max_attempts +1):
        operation = int(input('Choose an operation (1-4): '))
        
        #Deposit logic & output
        if operation == 1:
            deposit_amount = float(input('Enter the deposit amount: '))
            bank_account_balance = bank_account_balance + deposit_amount
            print(f'Deposit successful. New balance: ${bank_account_balance:.2f}')
            print(f'Bank Account Balance: ${bank_account_balance:.2f}')
            break
                    
        #Withrawal logic & output          
        elif operation == 2:
            withraw_amount = float(input('Enter the withdrawal amount: '))
            if withraw_amount > bank_account_balance:
                print('Error: insufficient funds. Withdrawal amount exceeds the current balance.')
                print(f'Bank Account Balance: ${bank_account_balance:.2f}')
                break
            else:
                bank_account_balance = bank_account_balance - withraw_amount
                print(f'Withdrawal successful. New balance: ${bank_account_balance:.2f}')
                print(f'Bank Account Balance: ${bank_account_balance:.2f}')
                break
                
        #Check balance output    
        elif operation == 3:
            print(f'Current Balance: ${bank_account_balance:.2f}')
            print(f'Bank Account Balance: ${bank_account_balance:.2f}')
            break

        elif operation == 4:
            print()
            print('Exiting KC Bank. Thank you!')
            loop = 'no'
            break
        
        else:
            print('Invalid option. Please enter a number between 1 and 4')
            print(f'You used {attempt} attempts')
            if attempt == max_attempts:
                print()
                print('Exceeded maximum attempts (3). Exiting the Bank Account')
                loop = 'no'
                break
            else:
                continue


    
