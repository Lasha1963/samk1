"""
პროგრამა ითვლის შეყვანილი კენტი რიცხვების ჯამს
"""
number = 1
sum = 0

while number != 0:
    number = int(input ("შეიყვანეთ ნატურალური რიცხვი ან დასამთავრებლად - 0: "))
    if number % 2 != 0: #  თუ კენტია
        sum += number

    if number != 0: continue    # თუ 0 არაა, ვაგრძელებთ
    else: break

print('შეყვანილი კენტი რიცხვების ჯამია: ', sum)