def nota_final(ap1, ap2, ap3):
  return ap1*0.4 + ap2*0.4 + ap3*0.2

def imc(peso,altura):
  return peso/(altura*altura)

def FtoC(f):
  c = (5 * (f-32) / 9)
  return c

if __name__ == '__main__':
  print(nota_final(8,8,8))
  print(imc(100,100.0))
  print(FtoC(122))