import urllib;

def read_text():
	text=open("./text.txt"); #open file
	file_text=text.read(); #read the text	
	check_words(file_text);
	
	text.close(); #close file

def check_words(text):
	check=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text);
	output=check.read();
	print(output);
	check.close();
read_text();
