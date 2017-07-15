from indexwriter import IndexWriter;

class Tokenizer:

	def __init__(self):
		self.iw = IndexWriter()

	def tokenizeFiles(self):
		self.iw.addDocumentsToIndex();