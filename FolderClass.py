#coding:utf-8
import os

class Folder:
	total_folder = 0

	def __init__(self, name):
		self._path = os.getcwd() + "\\" + name
		self._contentList = []
		self.name = name
		
		Folder.total_folder += 1

		self.update_contentList()

	"""-------------------- Folder Attribute property ----------------------"""

	def __repr__(self):
		folderLen = len(self.contentList)
		return '\n\nDEFINING FOLDER "{}" \nLocated in "{}" have {} file(s) inside.\n'\
			.format(self.name, self.path, folderLen)


	def _get_path(self):
		print('[FOLD] Get Path of "{}".'.format(self.name))

		try:
			return self._path
		except:
			print('Get path FAILED.\n')


	def _set_path(self, newPath):
		print('[FOLD] Set Path "{}" to "{}".'.format(self.path, newPath))

		try:
			self._path = newPath
		except:
			print('Set newPath  FAILED.\n')




	def _get_contentList(self):
		print('[FOLD] Get contentList of "{}".'.format(self.name))

		try:
			return self._contentList
		except:
			print('Get contentList FAILED.\n')


	def _set_contentList(self, newContentList):
		print('[FOLD] Set contentList from "{}" to "{}".'.format(self.contentList, newContentList))

		try :
			self._contentList = newContentList
		except:
			print('Set contentList FAILED.\n')

	path = property(_get_path, _set_path)
	contentList = property(_get_contentList, _set_contentList)
	

	"""-------------------- Folder Method ----------------------"""


	def update_contentList(self):
		print('[FOLD] Update contentList "{}".'.format(self.contentList))

		try:
			self.contentList = os.listdir(self.path)
		except:
			print('Update contentList FAILED.\n')


	def get_contentList_path(self):
		print('[FOLD] Get path of contentList "{}" of "{}".'.format(self.contentList, self.name))

		contentList_path = []
		try:
			for content in contentList:
				newPath = self.path + '\\' + content
				contentList_path.append(newPath)
			return contentList_path
		except:
			print('Get contentList path FAILED.\n')

