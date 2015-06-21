#!/usr/bin/env python
import os, fcntl
import unittest
from lock_checker import LockChecker

class CaptureLock(object):
	fila=''
	fid=-1
	fi_open=-1
	
	def capture_lock(self,filename):
		if os.path.isfile(filename):
			self.fila = filename
			self.fi_open = open(self.fila, 'a')
			self.fid = self.fi_open.fileno()
			print "FID = " + str(self.fid)
			self.assert_lock()
		else:
			print "File does not exist"
			exit(1)

	def assert_lock(self):
		try:
			fcntl.flock(self.fid, fcntl.LOCK_EX | fcntl.LOCK_NB)
		except IOError:
			print "Can't immediately write-lock the file, blocking"
		else:
			print "Lock acquired. No error."

	def release_lock(self): 
		fcntl.flock(self.fid, fcntl.F_UNLCK)
		print "Lock released"
	

class TestLockList(unittest.TestCase):

	def test_lock(self):
		instance1 = CaptureLock()
		filename1 = os.path.join(os.getcwd(), 'TestData/file1.txt')
		instance1.capture_lock(filename1)

		instance2 = CaptureLock()
		filename2 = os.path.join(os.getcwd(), 'TestData/file2.txt')
		instance2.capture_lock(filename2)


		lock_checker = LockChecker()
		generated_output = lock_checker.what_is_locked()
		expected_output = ['/home/bladerunner/Documents/mesosphereProject/Locker/LockChecker/TestData/file1.txt', '/home/bladerunner/Documents/mesosphereProject/Locker/LockChecker/TestData/file2.txt']
		self.assertEqual(generated_output,expected_output)

		instance1.release_lock()
		instance2.release_lock()

if __name__=='__main__':
	unittest.main()