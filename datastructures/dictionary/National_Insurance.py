#-------------------------------------------------------------------------------
# Author:      PGOnline
# Created:     21/05/2016
#-------------------------------------------------------------------------------


NatIns = {110:("Musk", "Elon"),120:("Torvalds", "Linus"),130:("Axmark", "David"),
          140:("Carmack", "John"),150:("Goodger", "Ben"),160:("Gates", "Bill"),
          170:("Page", "Larry"),180:("Brin", "Sergey"),190:("Berners-Lee", "Tim")}


print ("==== The entire dictionary looks like this: ")
for key,value in NatIns.items():
    print (key, value)

print ("=== Checking who has the number 160")
print (NatIns[160][1], NatIns[160][0])

print ("=== Adding record 200:Niklaus Wirth")
NatIns[200]=("Wirth", "Niklaus")
for key,value in NatIns.items():
    print (key, value)

print ("=== Deleting record 120")
NatIns.pop(120)
for key,value in NatIns.items():
    print (key, value)

print ("=== Changing 160 from Bill Gates to Snow White")
NatIns[160] = ("White", "Snow")
for key,value in NatIns.items():
    print (key, value)