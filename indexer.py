import os
import pickle
import sys

from filenametodocidmapper import FileNameToDocIdMapper
from filestorage import FileStorage
from tokenizer import Tokenizer
from inmemoryindex import InMemoryIndex

class Indexer:

	def __init__(self, directoryToBeIndexed, indexStorageDirectory):
		self._directory = directoryToBeIndexed
		self._indexStorageDirectory = indexStorageDirectory
		self._filestorage = FileStorage();
		self._fileNameToDocIdMapper = FileNameToDocIdMapper()
		self._tokenizer = Tokenizer()

	def iterateThroughFilesInDirectory(self):

		docId = 1
		for subdir, dirs, files in os.walk(self._directory):
			for file in files:
				filepath = subdir + os.sep + file

				self._tokenizer.tokenizeFiles(filepath, docId);
				self._fileNameToDocIdMapper.storeFileNameToDictId(filepath, docId)
				docId += 1

		self._filestorage.pickleIndexFile(self._indexStorageDirectory);
		self._fileNameToDocIdMapper.pickleFileNameToDocMapper(self._indexStorageDirectory)



if __name__ == "__main__":

	try:
		directoryToBeIndexed = sys.argv[1];
	except:
		raise Exception('Please specify the directory to be indexed');

	try:
		indexStorageDirectory = sys.argv[2]
	except:
		indexStorageDirectory = os.getcwd();

	indexer = Indexer(directoryToBeIndexed, indexStorageDirectory);
	indexer.iterateThroughFilesInDirectory();