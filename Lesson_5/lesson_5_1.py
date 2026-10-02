name = ['ლაშა', 'ირაკლი', 'მარტინა', 'გიო']
age = [62, 55, 63, 30, 43, 67, 89]

print(name[0])
print(age[0])

age[-1] = 35 #ბოლოდან პირველი შევცვალეთ

print(name[-1])
print(age[-1])
avg_age = int(sum(age) / len(age))
print(f"საშუალო ასაკია: {avg_age}")

# ვქმნით სიებს
lst2 = []
lst3 = list() # იგივეა რაც lst3 = []
lst4 = list("Tbilisi")

print(age)
print(age[::-1]) #  უკუღმა - უარყოითი ბიჯით

print(len(age))
print(min(age))
print(max(age))
print(sum(age))

print(sorted(age))
print(sorted(age, reverse=True)) # უკუღმა
print(sorted(age[::-1])) #  უკუღმა - იგივე შედეგი უარყოითი ბიჯით
print(age)
print(age[::2]) # ყოველი მეორე
print(age[1::2]) # ყოველი მეორე დაწყებული პირველი ინდექსიდან
print(age[1::2]) # ყოველი მეორე დაწყებული პირველი ინდექსიდან
print(age[1:5:2]) # ყოველი მეორე დაწყებული პირველი ინდექსიდან და დამთავრებული მე-5-ეზე
print(id(age[1]))