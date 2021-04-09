P1 = int(input())
R1 = int(input())
R2 = int(input())
P2 = int(input())

GP = P1 + P2
GR = R1 + R2

if GP > GR:
  print("Gana Bayern")
  
if GP < GR:
  print("Pierde Bayern")
  
if GP == GR:
  print("ChinChanPu")
