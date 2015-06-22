#!/usr/bin/env python
import os, fcntl
import unittest, time
from Constants import DOES_NOT_EXIST
from lslock import LockChecker

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
			print "Cannot write-lock the file, blocking"
		else:
			print "Lock acquired. No error."

	def release_lock(self): 
		fcntl.flock(self.fid, fcntl.F_UNLCK)
		print "Lock released"
	

class TestLockList(unittest.TestCase):

	def setUp(self):
		#Get Lock on a file
		self.instance1 = CaptureLock()
		self.filename1 = os.path.join(os.getcwd(), 'TestData/file1.txt')
		self.instance1.capture_lock(self.filename1)

		self.lock_checker = LockChecker()

	def tearDown(self):
		#Release lock and destroy
		self.instance1.release_lock()
		self.instance1 = None

	def test_multiple_locks_and_defaults(self):
		#Get Lock on another file : file2.txt
		instance2 = CaptureLock()
		filename2 = os.path.join(os.getcwd(), 'TestData/file2.txt')
		instance2.capture_lock(filename2)

		#Examine locked files
		pid1 = self.lock_checker.get_pid(self.filename1)
		pid2 = self.lock_checker.get_pid(filename2)

		generated_output = self.lock_checker.what_is_locked(filename='')
		expected_output = [(os.path.join(os.getcwd(), 'TestData/file1.txt'), pid1), (os.path.join(os.getcwd(), 'TestData/file2.txt'), pid2)]
		
		self.assertEqual(generated_output,expected_output)

		instance2.release_lock()

	def test_success_for_specific_directory(self):
		pid = self.lock_checker.get_pid('TestData/file1.txt')
		expected_output = [('TestData/file1.txt', pid)]

		good_directory = 'TestData'
		generated_output = self.lock_checker.what_is_locked(good_directory)

		self.assertEqual(expected_output, generated_output)

	def test_success_for_specific_file(self):
		pid = self.lock_checker.get_pid('TestData/file1.txt')
		expected_output = [('TestData/file1.txt', pid)]
		good_file = 'TestData/file1.txt'
		generated_output = self.lock_checker.what_is_locked(good_file)

		self.assertEqual(expected_output, generated_output)

	def test_fail_on_bad_directory_or_file(self):
		bad_input = 'bad_directory_or_filename'
		generated_output = self.lock_checker.what_is_locked(bad_input)

		self.assertEqual(generated_output, DOES_NOT_EXIST)


if __name__=='__main__':
	unittest.main()
