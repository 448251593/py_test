#coding:utf-8
import os
import platform  
def mkdir_me(path):
	sortid = 1;
	print(str(sortid).zfill(3));	
	print (platform.python_version() );
if __name__ == '__main__':
	mkdir_me('pic')
