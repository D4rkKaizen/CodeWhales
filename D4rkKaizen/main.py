# D4rkKaizen
# print("bober")

# print("--------------------------")

# def aboba(bober):
#   print(bober)

# aboba("vlas")

import random
import time

dellay = random.uniform(0.05, 0.2)

a=1000
randomchik= ["сука", "блять", "ненавижу", "твари","ненавижу блять"]
while a>=0:
  a=a-7
  print(str(a) + str(" " + random.choice(randomchik)))
  time.sleep(dellay)


