def fac(number):
    if number == 0:
        return 1
    else:
        return number * fac(number-1)

# 40 tane yol var 20 tanesi aynı aşağı doğru 20 tanesi yine aynı sağa doğru
print(int(fac(40) / (fac(20) * fac(20))))