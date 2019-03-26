#coding:utf-8

import os

class File:
	
	total_file = 0

	

	def __init__(self, path):
		self._path = path
		self._content = ""
		self.name = os.path.split(path)[-1]

		File.total_file += 1
		print('[FILE CREATION]', self)
		self.update_content()

	def __repr__(self):
		return '\n\nDEFINING FILE "{}"" \nLocated in "{}" with content:\n"{}"'\
				.format(self.name, self.path, self.content)

	"""-------------------- File instance method -------------------------"""

	def update_content(self):
		print('[FILE] Update content of "{}".'.format(self.name))
		try:
			with open(self.path, "r") as ofi:
				self.content = ofi.read()
		except:
			print('Update content FAILED.\n')


	"""-------------------- File Attribute property ----------------------"""

	def _get_File_path(self):
		#print('[FILE] Get Path of "{}".'.format(self.name))

		try:
			return self._path
		except:
			print('Get path FAILED.\n')

	def _set_File_path(self, newPath):
		#print('[FILE] Set Path of "{}".'.format(self.name))

		try:
			self._path = newPath
		except:
			print('Set newPath  FAILED.\n')



	def _get_File_content(self):
		#print('[FILE] Get content of "{}".'.format(self.name))

		try:
			return self._content
		except:
			print('Get content FAILED.\n')

	def _set_File_content(self, newContent):
		#print('[FILE] Set content of "{}".'.format(self.name))

		try :
			self._content = newContent
		except:
			print('Set content FAILED.\n')



	




	path = property(_get_File_path, _set_File_path)
	content = property(_get_File_content, _set_File_content)