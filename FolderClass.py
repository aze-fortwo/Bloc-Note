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
		self.lbx_name = ""
		
		Folder.total_folder += 1
		Folder.foldList.append(self)

		logging.info('FOLD - __init__ %s'%self)
		self.update_lbx_name()
		self.update_contentList()
		

	def __repr__(self):
			folderLen = len(self.contentList)
			return '"{}" with {} file(s) inside.'.format(self.name, folderLen)

	"""--------------------Folder Instance method -----------------------"""

	def update_contentList(self):
		logging.info('FOLD - update_contentList({})'.format(self.name))

		try:
			for content in os.scandir(self.path):

				if content.is_dir():
					newFold = Folder(content)
					self.contentList.append(newFold)
					Folder.foldList.append(newFold)
					logging.info('FOLD - Add <{}> to {} contentList'.\
							format(newFold.name, self.name))

				elif content.is_file():
					newFile = File(content)
					self.contentList.append(newFile)
					Folder.foldList.append(newFile)
					logging.info('FOLD - Add <{}> to {} contentList'.\
							format(newFile.name, self.name))
		except Exception as exception:
			logging.error('FOLD - update_contentList({}) FAILED.'.format(type(exception).__name__))


	def update_lbx_name(self):
		logging.info('FOLD - update_lbx_name({}).'.format(self.name))

		try:
			parentFolder = os.path.dirname(self.path)
			parentFolder = Folder.get_folder_in_foldList(os.path.split(parentFolder)[-1])

			if parentFolder != None:
				while parentFolder != None:
					self.lbx_name += '   '
					parentFolder = Folder.get_folder_in_foldList(os.path.split(\
											os.path.dirname(parentFolder.path))[-1])
				self.lbx_name += self.name
				logging.info('FOLD - lbx_name -> %s'%(self.lbx_name))

			else:
				self.lbx_name = self.name
				logging.info('FOLD - lbx_name -> %s'%(self.lbx_name))

					
		except Exception as exception:
			logging.error('FOLD - update_lbx_name({}) FAILED:\n{}'.format(self.name, exception))


	def get_folder_in_foldList(searched_folderName):
		logging.info('FOLD - get_folder_in_foldList({})'.format(searched_folderName))

		try :
			if Folder.is_in_foldList(searched_folderName):
				for folder in Folder.foldList:
					if folder.name == searched_folderName \
					or folder.lbx_name == searched_folderName:
						logging.info('FOLD - Return <%s>' % folder)
						return folder
			else:
				return None

		except Exception as exception:
			logging.error('FOLD - get_folder_in_foldList({}) FAILED.'.\
					format(type(exception).__name__, searched_folderName))

	def is_in_foldList(searched_folderName):
		logging.info('FOLD - Folder.is_in_foldList({})'.format(searched_folderName))
		try:
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName or folder.name == searched_folderName:
					logging.info("FOLD - YES")
					return True

			logging.info("FOLD - NO")
			return False

		except Exception as exception:
			logging.error("FOLD - Folder.is_in_foldList({}):\n{}".\
					format(searched_folderName,exception))


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
	



