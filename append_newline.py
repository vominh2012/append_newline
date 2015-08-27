import os
import sys

def PrintUsage():
	print 'Append newline in all files match pattern'
	print 'app <pattern> <inputdir> <outdir>'
	print 'example:'
	print ' app.py .cpp /home/myproject'
	sys.exit(2)

def Process(inputFile, outDir):
	with open(inputFile, 'rb+') as filehandle:
    		filehandle.seek(-1, os.SEEK_END)
		c = filehandle.read(1)
		print ord(c)
		if c == "\n":
			print inputFile
			print outDir

def main(argv):
	if len(argv) < 3:
		PrintUsage()

	for root, dirs, files in os.walk(argv[1]):
    		for file in files:
        		if file.endswith(argv[0]):
				inputFile = os.path.join(root, file)
				outputFile = os.path.join(argv[2], file)
				Process(inputFile, outputFile)
if __name__ == "__main__":
   main(sys.argv[1:])
