"""
Muallif: Abdinazarov Erali
Sana: 14-01-2022
Murakkab parol yaratish
"""
"""Bu dasturda men yaratgan parol andozaga (ya'ni barcha belgilar qatnashganligini)
   mos yoki yo'qligini tekshirishdan iborat"""

import random
import re

andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

belgilar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"

parol=""
for i in range(16):
    son = random.randint(0,len(belgilar)-1)
    parol+=belgilar[son]
print(parol)
ishora=True
while ishora:
    if re.match(andoza,parol):
        print("Parol to'g'ri kiritildi!")
        break
    else:
        print("Parol talabga javob bermaydi.")
        break
