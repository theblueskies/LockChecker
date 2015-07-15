# LockChecker
Provides a list of all resources that have been locked with a flock() call in Linux, and the process ID of the code that is locking it.


HOW TO GET IT:
====================================================================================
Steps:
1. Clone the repo to your desired directory: git clone https://github.com/theblueskies/LockChecker
2. cd into LockChecker. If you do an "ls" it should show up as "LockChecker"
3. Run this command: python setup.py install
   #Depending on the restrictiveness of your system, you might have to run:
	python setup.py install --user

TEST IT:
====================================================================================
1. Once you are in the folder LockChecker, Test it by running: ./lslock-test.py
2. For a more manual approach to testing, I have included helper_locker.py. This locks TestData/file2.txt and aims to show that it works: 

2a. Fire it up on the terminal: python helper_locker.py
2b. On another tab of the terminal run: ./lslock.py
2c. You should get the output of the relative path of "file2.txt" (Eg: [YouAsUser/Documents/LockChecker/TestData/file2.txt", Process_ID)]


HOW TO RUN THE LOCK CHECKER
====================================================================================
1. To check for locks in current working directory, run: ./lslock.py
2. To check for locks in a random_directory, run: ./lslock.py random_directory
3. You can import the class LockChecker and call the public function what_is_locked() to get a list of locked files. As before, you can specify a random location too
4. The function what_is_locked() can take either a directory or specific filename. It defaults to the current working directory of the file 
5. It returns a list of tuples : [(file, PID of process locking the file)]

NOTES:
====================================================================================
1. This is designed for a Linux system. It checks for Exclusive, Non Blocking locks.
2. Specific directories or files that needs to be checked can be supplied as command line arguments. The class LockChecker can also be imported into your code. The function what_is_locked() will return a list of locked files.
3. An invalid directory or filename supplied as command line argument will throw a message and exit
4. If no command line arguments are supplied, it will recursively check for locks in its current working directory and subdirectories
5. Test coverage done
6. It returns a list of tuples(files, process_ID of what has locked the file). If no files are locked (or a specific file being searched for is unlocked) then it returns an empty list.

