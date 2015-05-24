import optparse

def analyze(inputText):
	values = {'a':0,'b':0,'c':0,'d':0,
			 'e':0,'f':0,'g':0,'h':0,
			 'i':0,'j':0,'k':0,'l':0,
			 'm':0,'n':0,'o':0,'p':0,
			 'q':0,'r':0,'s':0,'t':0,
			 'u':0,'v':0,'w':0,'x':0,
			 'y':0,'z':0}
	
	for line in inputText:		
		for char in line:
			for key, value in values.iteritems():
				if char == key:
					values[key] = value + 1
					break
	
	
	for key, value in values.iteritems():
				if not value == 0:
					print '[+]Letter ' + str(key) + ' found ' + str(values.get(key)) + ' times\n'
				else:
					print '[-]Letter ' + str(key) + ' was not found anytime\n'	
	
	return

def main():

	parser = optparse.OptionParser('usage%prog'+\
		'-f <input file>')
	parser.add_option('-f', dest='tgtFile', type='string',\
		help='specify the name of the input file')
		
	(options, args) = parser.parse_args()
	tgtFile = options.tgtFile
		
	if tgtFile == None:
		print parser.usage
		exit(0)
		
	with open(tgtFile, 'r') as inputFile:
		print '[*]Input file was: ' + str(tgtFile) + '\n'		 
		analyze(inputFile.readlines())
		

if __name__=='__main__':
	main()