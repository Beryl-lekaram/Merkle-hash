import os
import hashlib

os.getcwd()

hashArray = []  
for file in os.listdir("tophash"):
    if file.endswith(".txt"):
        with open(os.path.join("tophash", file), 'rb') as f:
            print(file)
            contents = f.read()
            hash=hashlib.md5(contents).hexdigest()
            hashArray.append(hash)

print("Hash value of L1, L2, L3, L4:")
print(hashArray)
if(len(hashArray)%2!=0):
        hashArray.append(hashArray[-1])
while(len(hashArray)>1):
    j=0
    for i in range(0, len(hashArray)-1):
        f = str(hashArray[i]+hashArray[i+1])
        hashArray[j]=hashlib.md5(f.encode()).hexdigest()
        
        i+=2
        j+=1
    del hashArray[j:]

if (len(hashArray)==1):
    print("The top Hash:") 
    print(hashArray)
        
    