import sys

from indexreader import IndexReader

class Searcher:

	def __init__(self, wordToBeSearched):
		self._wordToBeSearched = wordToBeSearched
		self._ir = IndexReader();

	def searchWordFromIndex(self, wordToBeSearched):
		print self._ir.readWordSchemaFromIndex(wordToBeSearched)._documentId;


if 	__name__ == "__main__":
	try:
		wordToBeSearched = sys.argv[1];
	except:
		raise Exception('Please specify the word to be searched!');

	searcher = Searcher(wordToBeSearched);
	searcher.searchWordFromIndex(wordToBeSearched);