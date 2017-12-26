#coding:utf-8
import os

def mkdir_me(path):
	
	isExists=os.path.exists(path)

	# 判断结果
	if not isExists:
		os.makedirs(path) 
		print path+' 创建成功'
		return True
	else:
		# 如果目录存在则不创建，并提示目录已存在
		print path+' 目录已存在'
		return False
if __name__ == '__main__':
	mkdir_me('pic')
