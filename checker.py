import sys
import os
import hashlib
from functools import partial

def calchash(file):
    ha = hashlib.sha1()
    with open(file,'rb') as f:
        for buf in iter(partial(f.read, 1024*1024), b''):
            ha.update(buf)
    return ha.hexdigest()

args=sys.argv

dir1=args[1]
dir2=args[2]


file_set1 =set()
file_set2 = set()
file_table1={}

for curdir , dirs, files  in os.walk(dir1):
    for file in files:
        file_set1.add(os.path.join(curdir,file).replace(dir1,"",1))

for curdir , dirs, files  in os.walk(dir2):
    for file in files:
        file_set2.add(os.path.join(curdir,file).replace(dir2,"",1))



#print(file_set1)
#print(file_set2)


#print(file_set1.union(file_set2))
#print(file_set1.intersection(file_set2))
print(file_set1.difference(file_set2))
print(file_set2.difference(file_set1))

#print(file_set1.intersection(file_set2))


for file in file_set1.intersection(file_set2):
#    print(dir1)
#    print(file)


    h1 =calchash(dir1+'/'+(file))
    h2= calchash(dir2+'/'+(file))
#    print(h1)
#    print(h2)
    if h1!=h2:
        print(file)