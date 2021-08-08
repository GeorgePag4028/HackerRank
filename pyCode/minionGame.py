#!/usr/bin/env python3

vowels = 'AEIOU'
def minion_game(string) :
  leng = len(string)
  a =0 
  b = 0
  for i in range(leng) :
      if string[i] in vowels : 
        b += (leng -i)
      else : 
        a += (leng -i)
  if a >b: 
    print("Stuart",a)
  elif a==b : 
    print("Draw")
  else : 
    print("Kevin",b)


if __name__ == '__main__' :
  s = input()
  minion_game(s)
