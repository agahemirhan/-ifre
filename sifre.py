import random
harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifre uzunluğunu giriniz"))
parola = ""
for i in range(uzunluk):
    parola += random.choice(harfler)
print(parola)
