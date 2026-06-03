import os              #os module --> operating system module; library import gare ko module ho; file handling ma file haru sanga interact garna ko lagi use garincha; file haru create, delete, rename, move, copy, etc. garna ko lagi
print('_____________________________________________________________________')
print('Current working directory:', os.getcwd())            #getcwd() --> get current working directory

""" 
os.chdir(r"\DScience\python-basics_to_adv")         #chdir() --> change current working directory; windows ma 'r' lekhera file path dine natra error aauxa,aaru ma pardaina; file path ma backward slash '\' --> windows; forward slash '/'->linux,mac
print("changed working directory: ", end="")
print(os.getcwd())

#output:
_____________________________________________________________________
Current working directory: D:\DScience\python-basics_to_adv\File Handling       i.e current working directory bata tesko parent directory ma janxa
changed working directory: D:\DScience\python-basics_to_adv
 """

print(os.listdir())                   #-->File Handling directory ma bhako file haru ko list print garxa
#output: ['append.py', 'file.txt', 'learning_os.py', 'not_copy.jpg', 'read.py', 'test.py', 'write.py']

# os.mkdir("test_dir")                  -->make directory: test_dir nam ko directory banauxa; already exist bhaye error aauxa
# os.rmdir("test_dir")                  -->remove directory: test_dir nam ko directory delete garxa; directory empty bhaye matra delete garxa; already exist nabhaye error aauxa

# os.makedirs("test_dir/sub_dir")       -->make directories: test_dir nam ko directory vitra sub_dir nam ko directory banauxa wa parenthesis vitra diyiyeko file path aanusar directories banuxa; already exist bhaye error aauxa
# os.removedirs("test_dir/sub_dir")     -->remove directories: test_dir/sub_dir nam ko directory delete garxa; directory empty bhaye matra delete garxa; already exist nabhaye error aauxa
# os.rename("Copy.jpg", "not_copy.jpg")     -->rename file: Copy.jpg nam ko file ko naam not_copy.jpg ma rename garxa
