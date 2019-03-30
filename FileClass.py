#coding:utf-8

import os

class File:
	
	total_file = 0

	

	def __init__(self, path):
		self._path = path
		self._content = ""
		self.name = os.path.split(path)[-1]
		self.lbx_name = self.name

		File.total_file += 1
		self.update_content()

	def __repr__(self):
		return '\n\nDEFINING FILE "{}"" \nLocated in "{}" with content:\n"{}"'\
				.format(self.name, self.path, self.content)

	"""-------------------- File instance method -------------------------"""

	def update_content(self):
		#print('     FILE "{}" Update content.'.format(self.name))
		try:
			with open(self.path, "r") as ofi:
				self.content = ofi.read()

		except Exception as exception:
			print('\t{}\n\tUpdate content FAILED.\n'.format(type(exception).__name__))


	"""-------------------- File Attribute property ----------------------"""

	def _get_File_path(self):
		#print('\tFILE Get Path of "{}".'.format(self.name))

		try:
			return self._path
		except:
			print('\t     Get path FAILED.\n')

	def _set_File_path(self, newPath):
		#print('\tFILE Set Path of "{}".'.format(self.name))

		try:
			self._path = newPath
		except:
			print('\t     Set newPath  FAILED.\n')



	def _get_File_content(self):
		#print('\tFILE Get content of "{}".'.format(self.name))

		try:
			return self._content
		except:
			print('\t     Get content FAILED.\n')

	def _set_File_content(self, newContent):
		#print('\tFILE Set content of "{}".'.format(self.name))

		try :
			self._content = newContent
		except:
			print('\t     Set content FAILED.\n')



	




	path = property(_get_File_path, _set_File_path)
	content = property(_get_File_content, _set_File_content)