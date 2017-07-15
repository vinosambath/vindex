import pickle

from collections import defaultdict
from schema import Schema;

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InMemoryIndex():

	__metaclass__ = Singleton

	def __init__(self):
		self._inMemoryIndex = defaultdict(list);

	def addWordsToIndex(self, words, documentId, lineNo, position):
		self._inMemoryIndex[words].append(Schema(documentId, lineNo, position));

	def pickleIndexFile(self):
		with open(r"file.txt","wb") as file:
			pickle.dump(self._inMemoryIndex, file);

	def unpickleFileToIndex(self):
		with open(r"file.txt", "rb") as file:
			self._inMemoryIndex = pickle.load(file);

		print self._inMemoryIndex;

	def searchWordsFromIndex(self, wordToBeSearched):
		return self._inMemoryIndex[wordToBeSearched];