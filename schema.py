class Schema:

	'''
		documentId - the id of the document where the word was found.
		lineNo - the line no where the word was found in the document.
		position - the position where the word is found.
		functionORvariableORparameter - flag to define whether this token is function or variable or parameter.
			function  - 1
			variable  - 2
			parameter - 3
			default value will be 0
	'''
	def __init__(self, documentId, lineNo, position, functionORvariableORparameter = 0):

		self._documentId = documentId;
		self._lineNo = lineNo;
		self._position = position;
		self._functionORvariableORparameter = functionORvariableORparameter;