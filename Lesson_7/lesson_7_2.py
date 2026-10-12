correct_password = 'home'
counter = 0
input_password = input('შეიყვანეთ პაროლი: ')
while input_password != correct_password:

    print('თქვენი პაროლი არა სწორია')
    input_password = input('თავიდან სცადეთ: ')
    counter += 1
    if counter ==3:
        print('თქვენ 3-ჯერ არა სწორედ შეიყვანეთ პაროლი')
        break
print('\n\nთქვენი პაროლი სწორია')