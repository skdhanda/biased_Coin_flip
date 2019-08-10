import random

def biasedflip(trials,prob,runs=10):
  heads=0
  tails=0
  print("Iter\tHeads\tTails")
  for r in range(0,runs):
    i=0
    nhead=0
    ntail=0
    while i <trials:
      if random.randint(0,100) <prob:
        heads+=1
        nhead+=1
      else:
        tails+=1
        ntail+=1
      i+=1
    r+=1
    print("{0}\t{1}\t{2}").format(r,nhead,ntail)
  print("sum of total iternations\n-\t-\t-\t")
  print("{0}\t{1}\t{2}").format(r,heads,tails)
  return heads,tails



trials=int(input("Please provide the number of coin flips in an iteration: "))
runs=int(input("Please provide the total number of iterations : "))
prob=int(input("Plesae provide the probabality to bias the flip of coin to return heads range (0-100)  : "))

if 1<= prob >100:
  prob=int(input("Plesae provide the probabality to bias the flip of coin to return heads range (0-100)  : "))

total_heads,total_tails=biasedflip(trials,prob,runs)
obs_prob=round(total_heads*100/float(total_heads+total_tails),2)
print("Expected probabality = {0}\nObserved Probability {1}/({1}+{2}) = {3} ").format(prob,total_heads,total_tails,obs_prob)
