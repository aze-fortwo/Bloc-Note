#coding:utf-8

import os
import logging



class File:
	
	total_file = 0
	

	def __init__(self, dirEntry):
		self._path = dirEntry.path
		self._content = ""
		self.name = dirEntry.name
		self.lbx_name = self.name

		File.total_file += 1
		logging.info('Create <%s> File'%self.name)
		self.update_content()

	def __repr__(self):
		return '\n\nDEFINING FILE "{}"" \nLocated in "{}" with content:\n"{}"'\
				.format(self.name, self.path, self.content)

	"""-------------------- File instance method -------------------------"""

	def update_content(self):
		logging.info('FILE - "{}" Update content.'.format(self.name))
		try:
			with open(self.path, "r") as ofi:
				self.content = ofi.read()

		except Exception as exception:
			logging.error('FILE - {} Update content FAILED.\n'.format(type(exception).__name__))


	"""-------------------- File Attribute property ----------------------"""
	def _get_File_path(self):

		try:
			return self._path
		except:
			logging.error('FILE - Get path FAILED.')

	def _set_File_path(self, newPath):

		try:
			self._path = newPath
		except:
			logging.error('FILE - Set newPath  FAILED.')



	def _get_File_content(self):
		try:
			return self._content
		except:
			logging.error('FILE - Get content FAILED.')

	def _set_File_content(self, newContent):
		try :
			self._content = newContent
		except:
			logging.error('FILE - Set content FAILED.')

	




	path = property(_get_File_path, _set_File_path)
	content = property(_get_File_content, _set_File_content)