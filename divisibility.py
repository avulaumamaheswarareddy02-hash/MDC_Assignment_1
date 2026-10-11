# 1. Numbers divisible by 7 but not a multiple of 3

print("1. Numbers divisible by 7 but not a multiple of 3:")

result = ""

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        if result == "":
            result = str(i)
        else:
            result = result + "," + str(i)

print(result)
