import os; #os -> operating system used for function os.listdir() -> lists everything in the directory


def renameFile():
	#print(os.listdir("./prank")); # prints all the files in the prank directory 

#step1
	file_list=os.listdir("./prank");		#get list of files
	path=os.getcwd();				#get current directory
	os.chdir("./prank");				#change directory
#step 2
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"));  #rename filenames which have numbers
	os.chdir(path);					#change to root


renameFile();	#function Called
