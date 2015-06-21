# LockChecker
Provides a list of all resources locked with a flock() call in Linux


HOW TO GET IT:
====================================================================================
Steps:
1. Clone the repo to your desired directory: git clone https://github.com/theblueskies/LockChecker
2. cd into LockChecker. If you do an "ls" it should show up as "LockChecker"


TEST IT:
====================================================================================
1. Once you are in the folder LockChecker, Test it by running: ./lock_checker_test.py
2. For a more manual approach to testing, I have included helper_locker.py. This locks TestData/file2.txt and aims to show that it works: 

2a. Fire it up on the terminal: python helper_locker.py
2b. On another tab of the terminal run: ./lock_checker.py
2c. You should get the output of the relative path of "file2.txt" (Eg: YouAsUser/Documents/LockChecker/TestData/file2.txt")


HOW TO RUN THE LOCK CHECKER
====================================================================================
1. To check for locks in current working directory, run: ./lock_checker.py
2. To check for locks in a random_directory, run: ./lock_checker.py random_directory
3. You can import the class and call the public function what_is_locked() to get a list of locked files. As before, you can specify a random location too
4. The function what_is_locked() can take either a directory or specific filename. It defaults to the current working directory of the file 


NOTES:
====================================================================================
1. This is designed for a Linux system. It checks for Exclusive, Non Blocking locks.
2. Specific directories or files that needs to be checked can be supplied as command line arguments. The class LockChecker can also be imported into your code. The function what_is_locked() will return a list of locked files.
3. An invalid directory or filename supplied as command line argument will throw a message and exit
4. If no command line arguments are supplied, it will recursively check for locks in its current working directory and subdirectories
5. Test coverage done
6. It returns a list (of files). If no files are locked (or a specific file being searched for is unlocked) then it returns an empty list

