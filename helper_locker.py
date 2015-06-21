import os, fcntl

filo = os.path.join(os.getcwd(), 'TestData/file2.txt')
fi_open = open(filo, 'a')
fid = fi_open.fileno()
def assert_lock():	
	try:
		fcntl.flock(fid, fcntl.LOCK_EX | fcntl.LOCK_NB)
	except IOError:
		print "Can't immediately write-lock the file, blocking"
	else:
		print "No error"

def release_lock(): 
	filo ='/home/bladerunner/Documents/mesosphereProject/data/file1.txt'
	locker = fcntl.flock(filo, 2)
	return locker

assert_lock()
while True:
	continue
