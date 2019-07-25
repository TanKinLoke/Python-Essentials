f1 = open("simplefile.txt","w") #Write-W, Read-R
f1.write("a")
f1.write("bc")
f1.writelines("123/n") #Not showing in windows
f1.writelines("hij") #Not showing in windows
f1.close()

f = open ("simplefile.txt")
print (f.readline()) #Print the words in the file
