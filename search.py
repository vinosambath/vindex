import os
import sys

from filenametodocidmapper import FileNameToDocIdMapper
from indexreader import IndexReader

class Searcher:

	def __init__(self, wordToBeSearched, indexStorageDirectory):
		self._indexStorageDirectory = indexStorageDirectory
		self._wordToBeSearched = wordToBeSearched
		self._ir = IndexReader(indexStorageDirectory);
		self._fileNameToDocMapper = FileNameToDocIdMapper();
		self._fileNameToDocMapper.unpickleFileNameToDocMapper(self._indexStorageDirectory);

	def searchWordFromIndex(self, wordToBeSearched):
		results = self._ir.readWordSchemaFromIndex(wordToBeSearched);
		for result in results:
			print self._fileNameToDocMapper.retrieveFileAssociatedWithDocId(result._documentId)


if 	__name__ == "__main__":
	try:
		wordToBeSearched = sys.argv[1];
	except:
		raise Exception('Please specify the word to be searched!');

	try:
		indexStorageDirectory = sys.argv[2];
	except:
		indexStorageDirectory = os.getcwd();

	searcher = Searcher(wordToBeSearched, indexStorageDirectory);
	searcher.searchWordFromIndex(wordToBeSearched);