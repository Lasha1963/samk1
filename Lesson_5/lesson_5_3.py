a = [2.0 , 2.44, 3.6767, 5.89, 6, 67, 67,0]
print(len(a))
print(a)

a.append(200)
a.append('text')
a.append(True)
a.append([1, 2, 3])
a.insert(1, False)  # მითითებულ ინდექსზე ჩავამატეთ რაღაც
print(a)
print(a.count(True)) # დავითვალოთ რამდენი True-ა სიაში
print(a.index(True)) # ვეძებთ საძიებო ცვლადის ინდექსს
a.reverse() # მოატრიალა სია
print(a)
a.remove(True)
print(a)

b = a[:] # კოპირების სამი ვარიანტი
b = list(a)
b = a.copy()
print(b)

print(id(a)) # a და b სხვადასხვა ობიექტებია
print(id(b))
