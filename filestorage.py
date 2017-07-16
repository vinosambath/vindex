from inmemoryindex import InMemoryIndex

class FileStorage:

	def __init__(self):
		self._imx = InMemoryIndex()

	def pickleIndexFile(self, indexStorageDirectory):
		self._imx.pickleIndexFile(indexStorageDirectory);

