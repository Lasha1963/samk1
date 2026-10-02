a = [2.0 , 2.44, 3.6767, 5.89, 6, 67, 67,0]
print(len(a))
print(a)

a.append(200)
a.append('text')
a.append(True)
a.append([1, 2, 3])
a.insert(1, False)  # მითითებულ ინდექსზე ჩავამატეთ რაღაც
print(a)
a.remove(True)
print(a)