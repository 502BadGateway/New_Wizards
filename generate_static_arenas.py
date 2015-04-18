import gen_arena
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("./ASSETS/cities/") if isfile(join("./ASSETS/cities/",f))]
print files

for f in files:
    name = f
    name = name.replace("staticmap","")
    name = name.replace(".png","")
    a = gen_arena.arena(name, [], "ASSETS/cities/"+str(f), False, True)



