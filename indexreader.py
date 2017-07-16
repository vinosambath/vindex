from schema import Schema;
from inmemoryindex import InMemoryIndex;

class IndexReader:

	def __init__(self, indexStorageDirectory):
		self._imx = InMemoryIndex();
		self._imx.unpickleFileToIndex(indexStorageDirectory);

	def readWordSchemaFromIndex(self, wordToBeSearched):
		return self._imx.searchWordsFromIndex(wordToBeSearched)