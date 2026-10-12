x = -6
if x < 0:
    print(x)
    x = -x

print(x)

a = int(input("შეიყვანეთ რაიმე რიცხვი: "))
b = int(input("შეიყვანეთ რაიმე რიცხვი: "))
print(a, b,' if-aამდე')
if a<b and a != 0 or b != 0:
    a,b = b,a # კასკადური მინიჭება

print(a, b,' if-ის მერე')

#------------------------------------

ages = [34, 38, 62, 63]
x = int(input('შეიყვანეთ თქვენი ასაკი: '))
if x in ages:
    print('თქვენ მოიგეთ ლატარეა')
else:
    print('თქვენ ვერ გაარტყით')