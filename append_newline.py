import os
import sys
import shutil

NEWLINE_STR = "\r\n"

def PrintUsage():
	print 'Find and append newline(\\r\\n) in all files match pattern'
	print 'append_newline.py <pattern> <input_dir> <out_dir>'
	print 'example:'
	print ' append_newline.py .cpp /home/myproject /home/outdir'
	sys.exit(2)

def Process(src, curDir, curFile, des):
	inFile = os.path.join(curDir, curFile)
	
	with open(inFile, 'rb+') as filehandle:
    		filehandle.seek(-1, os.SEEK_END)
		c = filehandle.read(1)
		if c != '\n':
			outDir = curDir.replace(src, des, 1)
			
			if not os.path.exists(outDir):
				os.makedirs(outDir)
			
			outFile = inFile.replace(src, des, 1)
			shutil.copy2(inFile, outFile)
			print outFile
			with open(outFile,'ab') as f: f.write(NEWLINE_STR)

def main(argv):
	if len(argv) < 3:
		PrintUsage()
	
	pattern = argv[0]; # eg: .txt
	inDir = os.path.normpath(argv[1])
	outDir = os.path.normpath(argv[2])
	
	for root, dirs, files in os.walk(inDir):
    		for file in files:
        		if file.endswith(pattern):
					Process(inDir, root, file, outDir)
					
if __name__ == "__main__":
   main(sys.argv[1:])
