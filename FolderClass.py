#coding:utf-8
import os

class Folder:
	total_folder = 0
	foldList = []


	def __init__(self, path):
		self._path = path
		self._contentList = []
		self.name = os.path.split(path)[-1]
		
		Folder.total_folder += 1
		Folder.foldList.append(self)

		self.update_contentList()
		self.update_foldList()

	def __repr__(self):
			folderLen = len(self.contentList)
			return '\n\nDEFINING FOLDER "{}" \nLocated in "{}" have {} file(s) inside.\n'\
				.format(self.name, self.path, folderLen)

	"""-------------------- Folder Method ----------------------"""

	def update_contentList(self):
		print('[FOLD] Update contentList of "{}".'.format(self.name))

		try:
			self.contentList = os.listdir(self.path)
		except:
			print('Update contentList FAILED.\n')


	def update_foldList(self):
		print('[FOLD] Update foldList with "{}" content'.format(self.name))

		for contentPath in self.get_contentList_path():
			if os.path.isdir(contentPath):
				Folder(contentPath)


	def get_contentList_path(self):
		print('[FOLD] Get path of contentList of "{}".'.format(self.name))

		contentList_path = []
		try:
			for content in self.contentList:
				newPath = self.path + '\\' + content
				contentList_path.append(newPath)

			return contentList_path
		except:
			print('Get contentList path FAILED.\n')

	
	def get_parent_folder(self):
		print('[FOLD] Get parent folder of "{}"'.format(self.name))

		try:
			return os.path.split(self.path)[-2]
		except:
			print('Get parent folder of "{}"" FAILED.\n'.format(self.name))


	"""--------------------Folder Instance method -----------------------"""
	
	def get_folder_in_foldList(searched_folderName):
		print('[FOLD] Get "{}" FolderObject from foldList'.format(searched_folderName))

		try :
			for folder in Folder.foldList:
				if folder.name == searched_folderName:
					return folder
		except:
			print('Get "{}"" from foldList FAILED.\n'.format(searched_folderName))


	"""-------------------- Folder Attribute property ----------------------"""

	


	def _get_Folder_path(self):
		#print('[FOLD] Get Path of "{}".'.format(self.name))

		try:
			return self._path
		except:
			print('Get path FAILED.\n')

	def _set_Folder_path(self, newPath):
		#print('[FOLD] Set Path of "{}".'.format(self.name))

		try:
			self._path = newPath
		except:
			print('Set newPath  FAILED.\n')


	def _get_Folder_contentList(self):
		#print('[FOLD] Get contentList of "{}".'.format(self.name))

		try:
			return self._contentList
		except:
			print('Get contentList FAILED.\n')

	def _set_Folder_contentList(self, newContentList):
		#print('[FOLD] Set contentList of "{}".'.format(self.name))

		try :
			self._contentList = newContentList
		except:
			print('Set contentList FAILED.\n')





	path = property(_get_Folder_path, _set_Folder_path)
	contentList = property(_get_Folder_contentList, _set_Folder_contentList)
	



