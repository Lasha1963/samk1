text1 = """First line
Second line
Third line"""

text2 = "First line\nSecond line\nThird line" # სტრიქონის გადატანა
text3 = "First line\tSecond line\tThird line" # ტაბულაციით დაშორება
text4 = "Text \nText line"
text5 = "Text \\nText line" # მეორე \-ით მომდევნო სპეც სიმბოლო გადაიქცევა უბრალო ტეხტად
text6 = r"Text \\nText /\/\/\\tLine" # ტექსტამდე-r დანარჩენს სუფთა ტეხქსტად გადააქცევს

print(text1)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)