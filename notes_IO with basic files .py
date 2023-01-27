
myfile = open('myfile.txt')
myfile.read()
#如果想要再次读取，需要reset，即：
myfile.seek(0)

myfile.readlines()

#File Locations
#for windows :要使用\\，如：
myfile = open("C:\\Users\\UserName\\Folder\\test.txt")
#for MacOS:要用/，如：
myfile = open("C:/Users/UserName/Folder/test.txt")

pwd #用来显示当前文件路径

myfile.close()

#txt备份
with open('myfile.txt') as my_new_file:
    #这个block下的操作都是针对my_new_file
    contents = my_new_file.read()
    #这样的话，就不用担心会closing the file

with open('myfile.txt', mode = "w/r/a") as myfile:
    #mode里的w代表write，r代表read,a表示append
    contents = myfile.read()

with open('myfile.txt', mode = "a") as f:
    f.write('FOUR ON FOURTH')

#打开一个文件，写入内容
x = open('myfile.txt','w')
x.write('This is my file')
x.close()
