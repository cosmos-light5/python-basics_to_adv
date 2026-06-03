import os              #os module --> operating system module(e.g. os.listdir(),os.mkdir()); os-library import gare ko; file handling ma file haru sanga interact garna ko lagi; file haru create, delete, rename, move, copy, etc. garinxa
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

#print(os.listdir())                   #-->File Handling directory ma bhako file haru ko list print garxa
#output: ['append.py', 'file.txt', 'learning_os.py', 'not_copy.jpg', 'read.py', 'test.py', 'write.py']

# os.mkdir("test_dir")                  -->make directory: test_dir nam ko directory banauxa; already exist bhaye error aauxa
# os.rmdir("test_dir")                  -->remove directory: test_dir nam ko directory delete garxa; directory empty bhaye matra delete garxa; already exist nabhaye error aauxa

# os.makedirs("test_dir/sub_dir")       -->make directories: test_dir nam ko directory vitra sub_dir nam ko directory banauxa wa parenthesis vitra diyiyeko file path aanusar directories banuxa; already exist bhaye error aauxa
# os.removedirs("test_dir/sub_dir")     -->remove directories: test_dir/sub_dir nam ko directory delete garxa; directory empty bhaye matra delete garxa; already exist nabhaye error aauxa
# os.rename("Copy.jpg", "not_copy.jpg")     -->rename file: Copy.jpg nam ko file ko naam not_copy.jpg ma rename garxa

""" 
    github ma push garda yaha python-basics_to_adv kholera push garne ho vane git push origin "branch_name" dinu parxa 
ie. File handling dinu parxa; yaha hami le direct python-basics_to_adv ko File Handling vs-code ma khole run gareko le git push matra garda pani proper directory ma gayera basxa.. 
    """

r"""    python ma comment vitra \..\..\ use gare error aauxa because Python treat backslashes as escape characters.
        The 'r' tells Python not to treat backslashes as escape characters where 'r'= raw.

file_path= os.path.join('data','users','profile.txt')
print(file_path)
 data\users\profile.txt  -->file path banauxa jaha diyiyeko names chai folder banxan vane format sahit ko name chai file banxa.
                            -->yo os.path.join() module le mkdirs lai replace garna sakxa because of it's simplicity to write
                            -->yo module use garna kunai os specific way of path definition necessary xaina i.e windows ma  hunxa path ma vane linux, mac ma /../..
    """

#check existance of file/folder
if os.path.exists('copy.txt'):
    print("file exists")
else:
    print("not available..")


#adding file in cwd
path=os.path.join(os.getcwd(), 'app.log')           #app.log file banaudai xam vane yesko absolute file path join garera nikalna milxa
print(path)                                         #D:\DScience\python-basics_to_adv\File Handling\app.log

print("basename", os.path.basename(path))           #basename app.log
print("directory", os.path.dirname(path))           #directory D:\DScience\python-basics_to_adv\File Handling
print("split", os.path.splitext(path))              #split ('D:\\DScience\\python-basics_to_adv\\File Handling\\app', '.log')

