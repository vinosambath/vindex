from indexwriter import IndexWriter;

class Tokenizer:

	def __init__(self):
		self._iw = IndexWriter()

	def tokenizeFiles(self, filepath, docId):
		self.tokenizeFilesToLines(filepath, docId)

	def tokenizeFilesToLines(self, filepath, docId):
		lineNo = 1
		file_content = open(filepath);
		file_content = file_content.readlines();
		for lines in file_content:
			self.tokenizeLinesToWords(lines, lineNo, docId);
			lineNo += 1;

	def tokenizeLinesToWords(self, lines, lineNo, docId):
		for words in lines.split(" "):
			words = words.strip(" \(\),;{}");
			if words:
				self._iw.addDocumentsToIndex(words, docId, lineNo, 0);