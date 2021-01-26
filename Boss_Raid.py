import random as rd


def item(b):
    b = (b * 15) + 5
    return b


def boss_avoid(b):
    b = b / 0.115
    return b


def min_damage(b):
    b = 0
    b = b + item(1)
    return b


def max_damage(b):
    b = 0
    b = b + item(1500)
    return b


def critical_hit(a):
    a = 0
    damage = rd.randint(min_damage(1), max_damage(1500))
    probability = rd.random()
    if probability >= 0.8:
        critical_damage = damage * 11
        critical_damage = item(critical_damage)
        print("Critical Hit! Damage : " + str(int(critical_damage)))
        a = critical_damage
    else:
        damage = item(damage)
        print("Hit! Damage : " + str(int(damage)))
        a = damage
    return a


bossHP = 100000000
hit_count = 0
total_damage = 0
while bossHP > 0:
    probability = boss_avoid(rd.random())
    if probability >= 0.5:
        damage = critical_hit(0)
        bossHP = bossHP - damage
        print("Boss HP : " + str(int(bossHP)) + "\n")
        total_damage = total_damage + damage
    else:
        print("Miss!!!!!!!!!!!!!\n")
    hit_count = hit_count + 1

print("Total Hit Count : " + str(hit_count))
print("Total Damage : " + str(total_damage))
