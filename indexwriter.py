from schema import Schema;
from inmemoryindex import InMemoryIndex;

class IndexWriter:

	def __init__(self):
		self._imx = InMemoryIndex()

	def addDocumentsToIndex(self, words, documentId, lineNo, position):
		self._imx.addWordsToIndex(words, documentId, lineNo, position);