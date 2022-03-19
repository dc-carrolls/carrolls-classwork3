RED = (255,0,0)
BLUE = [0,0,255]

def change_to_green1(colour):
  colour[0]=0
  colour[1]=255
  colour[2]=0
  print(colour)
#end procedure

def change_to_green2(colour):
  colour=(0,255,0)
  print(colour)
#end procedure

# change_to_green1(BLUE)
# print(BLUE)

change_to_green2(RED)
print(RED)

ref_args={'x':5}

def add_one(ref_params):
  ref_params['x']+=1
  return ref_params['x']

print(ref_args['x'])
print(add_one(ref_args))
print(ref_args['x'])