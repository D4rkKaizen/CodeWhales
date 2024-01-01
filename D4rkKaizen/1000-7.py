import random
import time

delay = random.uniform(0.03, 0.05)

a=1000
randomchik= ["сука", "блять", "ненавижу", "твари","ненавижу блять"]
while a>=0:
  a=a-7
  print(str(a) + str(" | " + random.choice(randomchik)))
  time.sleep(delay)
