#!/usr/bin/env python
import os, fcntl, sys
from Constants import LOCKED, UNLOCKED, DOES_NOT_EXIST

class LockChecker(object):
	initial_directory = ''

	def __init__(self):
		if sys.platform == 'linux' or sys.platform == 'linux2':
			if len(sys.argv)>2:
				print "Can accept only one root directory"
				return DOES_NOT_EXIST

			elif len(sys.argv)==2:
				if os.path.exists(sys.argv[1]):
					self.initial_directory = sys.argv[1]
				else:
					print "Directory/File does not exist"
					return DOES_NOT_EXIST
			else:
				self.initial_directory = os.getcwd()
		else:
			print "Can only handle Linux systems now"
			exit(1)

	def _generate_all_filepaths(self):
		filepaths = []

		if os.path.isfile(self.initial_directory):
			return [self.initial_directory]

		for folder, subs, files in os.walk(self.initial_directory):
			if '.' not in folder:
				for filename in files:
					filepath = os.path.join(folder, filename)
					filepaths.append(filepath)
		return filepaths

	def _check_for_lock(self, filepath):
		fopen = open(filepath, 'a')
		fid = fopen.fileno()
		try:
			fcntl.flock(fid, fcntl.LOCK_EX | fcntl.LOCK_NB)
		except IOError:
			return LOCKED
		else:
			fcntl.flock(fid, fcntl.F_UNLCK)
			return UNLOCKED

	def what_is_locked(self,filename=''):
		if not os.path.exists(filename) and filename is not '':
			print "Directory/File does not exist"
			return DOES_NOT_EXIST

		if os.path.exists(filename) and os.path.isfile(filename):
			if self._check_for_lock(filename):
				return [filename]

		if os.path.exists(filename) and not os.path.isfile(filename):
				self.initial_directory = filename

		locked_list = []
		filepaths = self._generate_all_filepaths()
		for single_file in filepaths:
			if self._check_for_lock(single_file):
				locked_list.append(single_file)
		return locked_list


if __name__ == '__main__':
	lockChecker = LockChecker()
	print lockChecker.what_is_locked()