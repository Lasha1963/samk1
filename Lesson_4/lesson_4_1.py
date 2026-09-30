str = ("Welcome home")
print(str)
print(str.upper()) # დიდი ასოები
print(str.lower()) # პატარა ასოები
print(str.count("e")) # რამდენი e-ასოა
print(str.count("e", 2,10)) # რამდენი e-ასოა დაწყებული მე-2-ე ინდექსიდან მე-10-მდე
print(str.replace("e","E"))  # ვბეჭდავთ გამოცვლილ ასოებს მაგრამ თავად ცვლადში არაფერი იცვლება
print(str)

s="hgff     2135 565,,, jfjfjf"
print(s.replace(" ",'' ).split(",")) # ჯერ ცარიელი ადგილები ამოიღო და მერე დაყო ,-იბით