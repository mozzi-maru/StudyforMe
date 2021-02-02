import random as rd


get_exp = 1
level = 1
exp_req = 20
exp_now = 0


def level_up2(exp_now, level):
    exp_requ = exp_req
    if exp_now > exp_requ:
        while exp_now > exp_requ:
            exp_now = exp_now - exp_requ
            level = level + 1

            def exp_require(exp_req):
                exp_req = (exp_req + 30 ^ 3)
                return exp_req

            exp_requ = exp_require(exp_requ)
            print("Level UP!!!")
            print("Now Your EXP. = " + str(exp_now))
            print("Require EXP is = " + str(exp_requ))
            print("Your Level is = " + str(level) + "\n")
    return exp_now, level


exp_now = exp_now + rd.randint(500, 1000)
level_up2(exp_now, level)
