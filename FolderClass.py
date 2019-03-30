#coding:utf-8
import os
from FileClass import File

class Folder:
	total_folder = 0
	foldList = []


	def __init__(self, path):
		self._path = path
		self._contentList = []
		self.name = os.path.split(path)[1]
		self.lbx_name = self.name
		
		Folder.total_folder += 1
		Folder.foldList.append(self)

		self.update_contentList()
		

	def __repr__(self):
			folderLen = len(self.contentList)
			return '\n\nDEFINING FOLDER "{}" \nLocated in "{}" have {} file(s) inside.\n'\
				.format(self.name, self.path, folderLen)

	"""--------------------Folder Instance method -----------------------"""

	def update_contentList(self):
		#print('\nFOLD "{}" Update contentList.'.format(self.name))

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
			print(exception)
			print('\nUpdate contentList FAILED.\n'.format(type(exception).__name__))


	def update_lbx_name(self):
		#print('\nFOLD Format "{}" for listbox name.'.format(self.name))

		try:
			parent_folder = self.get_parent_folder()
			
			if Folder.is_in_foldList(parent_folder):
				self.lbx_name = "   " + self.lbx_name
				
				# File.lbx_name update
				for content in self.contentList:
					content.lbx_name = "   " + content.lbx_name
					
		except Exception as exception:
			print(exception)
			print('\nFormat "{}" FAILED'.format(self.name))


	def get_parent_folder(self):
		#print('\nFOLD Get parent folder of "{}"'.format(self.name))

		try:
			return os.path.split(os.path.split(self.path)[0])[1]

		except Exception as exception:
			print(exception)
			print('\nGet parent folder of "{}"" FAILED.\n'.format(self.name))


	def is_in_foldList(searched_folderName):
		#print('\nFOLD Is "{}"  in foldList ?'.format(searched_folderName))
		try:
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName:
					#print("     It is in foldList")
					return True

		except Exception as exception:
			print(exception)
			print("\nSearch in foldList FAILED.\n")


	def get_folder_in_foldList(searched_folderName):
		#print('\nFOLD "{}" Get FolderObject from foldList'.format(searched_folderName))

		try :
			for folder in Folder.foldList:
				if folder.lbx_name == searched_folderName:
					return folder
		except Exception as exception:
			print(exception)
			print('\nGet "{}" from foldList FAILED.\n'.format(type(exception).__name__, searched_folderName))



	"""-------------------- Folder Attribute property ----------------------"""

	


	def _get_Folder_path(self):
		#print('FOLD Get Path of "{}".'.format(self.name))

		try:
			return self._path
		except:
			print('Get path FAILED.\n')

	def _set_Folder_path(self, newPath):
		#print('FOLD Set Path of "{}".'.format(self.name))

		try:
			self._path = newPath
		except:
			print('Set newPath  FAILED.\n')


	def _get_Folder_contentList(self):
		#print('FOLD Get contentList of "{}".'.format(self.name))

		try:
			return self._contentList
		except:
			print('Get contentList FAILED.\n')

	def _set_Folder_contentList(self, newContentList):
		#print('FOLD Set contentList of "{}".'.format(self.name))

		try :
			self._contentList = newContentList
		except:
			print('Set contentList FAILED.\n')





	path = property(_get_Folder_path, _set_Folder_path)
	contentList = property(_get_Folder_contentList, _set_Folder_contentList)
	



