# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def sayi(int1):
  bolen = 2
  while int1 != 1:
    if int1 / bolen == 1:
      print(bolen)
      break
    elif int1 % bolen == 0:
      int1 /= bolen
    else:
      bolen += 1
sayi(600851475143)