# A Hallowe’en display needs a computer controlled light which will flicker. 
# Flicker the light for a random number of seconds between 1/10 and 1/100 
# of a second. You can use a pause function that takes as a parameter the 
# number of milliseconds to pause the program. For example pause(1000) 
# will pause the program for 1 second.  To turn the light on and off, 
# set the value of light to HIGH for ON and LOW for OFF.  
# The control loop should run continuously.
import random
import time
light = 'LOW'
program_over = False
while not program_over:
  print(light)
  gap = random.uniform(0.1, 0.5)
  time.sleep(gap)
  if light == 'HIGH':
    light = 'LOW'
  else:
    light = 'HIGH'
  #endif
#endwhile





