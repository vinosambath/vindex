import os
import pickle
import sys

from filestorage import FileStorage
from tokenizer import Tokenizer
from inmemoryindex import InMemoryIndex

class Indexer:

	def __init__(self, directoryToBeIndexed):
		self._directory = directoryToBeIndexed
		self._filestorage = FileStorage();
		self._tokenizer = Tokenizer()

	def iterateThroughFilesInDirectory(self):

		for subdir, dirs, files in os.walk(self._directory):
			for file in files:
				filepath = subdir + os.sep + file

				self._tokenizer.tokenizeFiles(filepath);

		self._filestorage.pickleIndexFile();


if __name__ == "__main__":
	try:
		directoryToBeIndexed = sys.argv[1];
	except:
		raise Exception('Please specify the directory to be indexed');

	indexer = Indexer(directoryToBeIndexed);
	indexer.iterateThroughFilesInDirectory();