from inmemoryindex import InMemoryIndex

class FileStorage:

	def __init__(self):
		self._imx = InMemoryIndex()

	def pickleIndexFile(self):
		self._imx.pickleIndexFile();

