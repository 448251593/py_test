import os;

def err_log(log_data):
	with open("err_log_caijiqqlog.log",'a') as f:
		f.write(log_data+'\n')	

if __name__ == '__main__':
	file_append("111");
