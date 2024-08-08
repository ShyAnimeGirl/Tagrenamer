import os
import sys
from tinytag import TinyTag

if len(sys.argv) != 2:
	print("Please provide a path to a file as a command line argument.")
	quit()

	
file = sys.argv[1]
	
	
if not os.path.isfile(file):
	print(file,"not found")
	quit()
	

if not TinyTag.is_supported(file):
	print(file, "not supported by tinytag")
	quit()
	

tag = TinyTag.get(file)

if tag.title == None:
	print(file,"has no title tag")
	quit()

	
#split the file extension off the end
basepath, file_ext = os.path.splitext(file)


#split the path off the filename
path, filename = os.path.split(basepath)

if tag.title == filename:
	print(file,"tag is same as filename")
	quit()

new_filename = tag.title + file_ext

#combines the old path with the new filename
newpath = os.path.join(path, new_filename)

print("renaming",file,"to",new_filename) 

os.rename(file,newpath)