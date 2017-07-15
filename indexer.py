import os
import sys

from tokenizer import Tokenizer;

class Indexer:

	def __init__(self, directoryToBeIndexed):
		self._directory = directoryToBeIndexed
		self.tokenizer = Tokenizer()

	def tokenizeFilesInDirectory(self):
		self.tokenizer.tokenizeFiles();


if __name__ == "__main__":
	try:
		directoryToBeIndexed = sys.argv[1];
	except:
		raise Exception('Please specify the directory to be indexed');

	indexer = Indexer(sys.argv[0]);
	indexer.tokenizeFilesInDirectory();