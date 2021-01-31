import string as stri
import random as rd

results = ""
i = 0

while i < 20:
    results += rd.choice(stri.ascii_letters)
    if rd.randint(0, 9) == rd.randint(0, 9):
        results += str(rd.randint(0, 9))
    if len(results) == 20:
        break
    i = i + 1

print(results)
