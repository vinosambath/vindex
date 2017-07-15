from schema import Schema;
from inmemoryindex import InMemoryIndex;

class IndexReader:

	def __init__(self):
		self._imx = InMemoryIndex();
		self._imx.unpickleFileToIndex();

	def readWordSchemaFromIndex(self, wordToBeSearched):
		return self._imx.searchWordsFromIndex(wordToBeSearched)