# 파이썬과 루비로 조건문과 입력함수 복습해보기

import random as rd

i = 0
criticalhit = 0
hitcount = 0
total_critical_damage = 0
total_normal_damage = 0

while i < 10000:
    damage = rd.randint(0, 100)
    probability = rd.randint(0, 100)
    if probability >= 90 and damage > 70:
        critical_damage = damage * 10
        print("critiral hit!!! Damage : " + str(critical_damage))
        total_critical_damage = total_critical_damage + critical_damage
        criticalhit = criticalhit + 1
    else:
        print("Hit!!! Damage : " + str(damage))
        total_normal_damage = total_normal_damage + damage
        hitcount = hitcount + 1
    i = i + 1

print("Critical HIT Count : " + str(criticalhit))
print("Total Critical Damage : " + str(total_critical_damage))
print("Hit count : " + str(hitcount))
print("Total Damage : " + str(total_normal_damage))
