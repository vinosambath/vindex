from indexwriter import IndexWriter;

class Tokenizer:

	def __init__(self):
		self._iw = IndexWriter()

	def tokenizeFiles(self, filepath):
		self.tokenizeFilesToLines(filepath)
		#self.iw.addDocumentsToIndex();

	def tokenizeFilesToLines(self, filepath):
		lineNo = 1
		file_content = open(filepath);
		file_content = file_content.readlines();
		for lines in file_content:
			self.tokenizeLinesToWords(lines, lineNo);
			lineNo += 1;

	def tokenizeLinesToWords(self, lines, lineNo):
		for words in lines.split(" "):
			words = words.strip();
			if words:
				self._iw.addDocumentsToIndex(words, 1, lineNo, 0);