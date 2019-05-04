#coding:utf-8
import os
from FileClass import File
import logging

class Folder:
	total_folder = 0
	foldList = []


	def __init__(self, dirEntry):
		self._path = dirEntry.path
		self._contentList = []*len(os.listdir(dirEntry.path))

		self.dirEntry = dirEntry
		self.name = dirEntry.name
		self.lbx_name = self.name
		
		Folder.total_folder += 1
		Folder.foldList.append(self)

		logging.info('Create <%s>'%self)
		self.update_contentList()
		self.update_lbx_name()
		

	def __repr__(self):
			folderLen = len(self.contentList)
			return '"{}" with {} file(s) inside.'.format(self.name, folderLen)

	"""--------------------Folder Instance method -----------------------"""

	def update_contentList(self):
		logging.info('FOLD - <{}> Update contentList.'.format(self.name))

		try:
			for content in os.scandir(self.path):

				if content.is_dir():
					newFold = Folder(content)
					newFold.lbx_name = "   " + newFold.lbx_name
					self.contentList.append(newFold)

				elif content.is_file():
					newFile = File(content)
					newFile.lbx_name = "   " + newFile.lbx_name
					self.contentList.append(newFile)


		except Exception as exception:
			logging.error('FOLD - <{}> Update contentList FAILED.\n'.format(type(exception).__name__))


	def update_lbx_name(self):
		logging.info('FOLD - Format "{}" for listbox name.'.format(self.name))

		try:
			parentFolder = self.get_parent_folder()
			print(parentFolder)
			if Folder.is_in_foldList(parentFolder):
				self.lbx_name = "   " + self.lbx_name
				
				# File.lbx_name update
				for content in self.contentList:
					content.lbx_name = "   " + content.lbx_name
					
		except Exception as exception:
			logging.error('FOLD - Format "{}" FAILED'.format(self.name))


	def get_parent_folder(self):
		logging.info('FOLD - Get parent folder of "{}"'.format(self.name))

		try:
			return os.path.dirname(self.path)

		except Exception as exception:
			logging.error('FOLD - Get parent folder of "{}"" FAILED.\n'.format(self.name))


	def is_in_foldList(searched_folderName):
		logging.info('FOLD - Is "{}"  in foldList ?'.format(searched_folderName))
		try:
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName:
					logging.info("YES")
					return True

		except Exception as exception:
			logging.error("FOLD - Search in foldList FAILED:\n%s"%exception)


	def get_folder_in_foldList(searched_folderName):
		logging.info('FOLD - <{}> Get FolderObject from foldList'.format(searched_folderName))

		try :
			if Folder.is_in_foldList(clicked_content):
				for folder in Folder.foldList:
					if folder.lbx_name == searched_folderName:
						logging.info('FOLD - Return <%s>' % folder)
						return folder
			else:
				return None

		except Exception as exception:
			logging.error('FOLD - Get "{}" from foldList FAILED.\n'.format(type(exception).__name__, searched_folderName))



	"""-------------------- Folder Attribute property ----------------------"""

	


	def _get_Folder_path(self):
		try:
			return self._path
		except:
			logging.error('FOLD - Get path FAILED.\n')

	def _set_Folder_path(self, newPath):
		try:
			self._path = newPath
		except:
			logging.error('FOLD - Set newPath  FAILED.\n')


	def _get_Folder_contentList(self):
		try:
			return self._contentList
		except:
			logging.error('FOLD - Get contentList FAILED.\n')

	def _set_Folder_contentList(self, newContentList):
		try :
			self._contentList = newContentList
		except:
			logging.error('FOLD - Set contentList FAILED.\n')





	path = property(_get_Folder_path, _set_Folder_path)
	contentList = property(_get_Folder_contentList, _set_Folder_contentList)
	



