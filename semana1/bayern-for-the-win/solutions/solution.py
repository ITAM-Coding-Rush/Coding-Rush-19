P1 = int(input())
R1 = int(input())
R2 = int(input())
P2 = int(input())

GB = P1 + P2
GR = R1 + R2

if GB > GR:
  print("Gana Bayern")
  
if GB < GR:
  print("Pierde Bayern")
  
if GB == GR:
  print("ChinChanPu")
