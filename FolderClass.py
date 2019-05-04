#coding:utf-8
import os
from FileClass import File
import logging

logging.basicConfig(filename='debug.txt', filemode='w+', level = logging.DEBUG,format=' %(asctime)s - %(levelname)s - FOLDER - %(message)s')

class Folder:
	total_folder = 0
	foldList = []


	def __init__(self, dirEntry):
		self._path = dirEntry.path
		self._contentList = []
		self.dirEntry = dirEntry
		self.name = dirEntry.name
		self.lbx_name = self.name
		
		Folder.total_folder += 1
		Folder.foldList.append(self)

		logging.info('Create <%s>'%self)
		self.update_contentList()
		

	def __repr__(self):
			folderLen = len(self.contentList)
			return '"{}" with {} file(s) inside.'.format(self.path, folderLen)

	"""--------------------Folder Instance method -----------------------"""

	def update_contentList(self):
		logging.info('<{}> Update contentList.'.format(self.name))

		try:
			for content in os.listdir(self.path):
				newPath = os.path.join(self.path, content)

				if os.path.isdir(newPath):
					newFold = Folder(os.path.join(self.path, content))
					newFold.lbx_name = "   " + newFold.lbx_name
					self.contentList.append(newFold)

				elif os.path.isfile(newPath):
					newFile = File(os.path.join(self.path, content))
					newFile.lbx_name = "   " + newFile.lbx_name
					self.contentList.append(newFile)


		except Exception as exception:
			logging.error('Update contentList FAILED.\n'.format(type(exception).__name__))


	def update_lbx_name(self):
		logging.info('Format "{}" for listbox name.'.format(self.name))

		try:
			parent_folder = self.get_parent_folder()
			
			if Folder.is_in_foldList(parent_folder):
				self.lbx_name = "   " + self.lbx_name
				
				# File.lbx_name update
				for content in self.contentList:
					content.lbx_name = "   " + content.lbx_name
					
		except Exception as exception:
			logging.error('Format "{}" FAILED'.format(self.name))


	def get_parent_folder(self):
		logging.info('Get parent folder of "{}"'.format(self.name))

		try:
			return os.path.split(os.path.split(self.path)[0])[1]

		except Exception as exception:
			logging.error('Get parent folder of "{}"" FAILED.\n'.format(self.name))


	def is_in_foldList(searched_folderName):
		logging.info('Is "{}"  in foldList ?'.format(searched_folderName))
		try:
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName:
					#print("     It is in foldList")
					return True

		except Exception as exception:
			logging.error("Search in foldList FAILED.\n")


	def get_folder_in_foldList(searched_folderName):
		logging.info('<{}> Get FolderObject from foldList'.format(searched_folderName))

		try :
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName:
					return folder
		except Exception as exception:
			logging.error('Get "{}" from foldList FAILED.\n'.format(type(exception).__name__, searched_folderName))



	"""-------------------- Folder Attribute property ----------------------"""

	


	def _get_Folder_path(self):
		try:
			return self._path
		except:
			logging.error('Get path FAILED.\n')

	def _set_Folder_path(self, newPath):
		try:
			self._path = newPath
		except:
			logging.error('Set newPath  FAILED.\n')


	def _get_Folder_contentList(self):
		try:
			return self._contentList
		except:
			logging.error('Get contentList FAILED.\n')

	def _set_Folder_contentList(self, newContentList):
		try :
			self._contentList = newContentList
		except:
			logging.error('Set contentList FAILED.\n')





	path = property(_get_Folder_path, _set_Folder_path)
	contentList = property(_get_Folder_contentList, _set_Folder_contentList)
	



