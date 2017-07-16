import os
import pickle

class FileNameToDocIdMapper:

	def __init__(self):
		self._fileToDocIdDict = {}

	def storeFileNameToDictId(self, filePath, docId):
		self._fileToDocIdDict[docId] = filePath;

	def pickleFileNameToDocMapper(self, directoryToStoreMapper):
		filePath = directoryToStoreMapper + os.sep + "mapperindex.pickle"
		with open(filePath,"wb") as file:
			pickle.dump(self._fileToDocIdDict, file);

	def retrieveFileAssociatedWithDocId(self, docId):
		return self._fileToDocIdDict[docId];

	def unpickleFileNameToDocMapper(self, directoryToStoreMapper):
		filePath = directoryToStoreMapper + os.sep + "mapperindex.pickle"
		with open(filePath,"rb") as file:
			self._fileToDocIdDict = pickle.load(file);