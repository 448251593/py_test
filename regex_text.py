#coding:utf-8
import os,re
import mkdir

def regular_me(path):
	strid = re.findall(r'/blog/[0-9]*',path)
	path = strid[0][1:len(strid[0])-1]
	return path
if __name__ == '__main__':
	path = regular_me('https://user.qzone.qq.com/822989010/blog/1488525103')
	
	
	print (path)
	#os.makedirs(strid[0]+'/')
	os.system("mkdir -p "+path)	
