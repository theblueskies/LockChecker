import os, fcntl

LOCKED = True
UNLOCKED = False

class LockChecker(object):
	initial_directory = ''

	def __init__(self):
		self.initial_directory = os.getcwd()

	def _generate_all_filepaths(self):
		filepaths = []
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

	def what_is_locked(self):
		locked_list = []
		filepaths = self._generate_all_filepaths()
		for single_file in filepaths:
			if self._check_for_lock(single_file):
				locked_list.append(single_file)
		return locked_list

lockChecker = LockChecker()
print lockChecker.what_is_locked()
