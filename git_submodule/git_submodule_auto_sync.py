#coding:utf-8
import os
import platform 
import time, re,urllib,hashlib,sys;
def git_get_diff_commit_id():
	str_txt = '';
	with open("git_diff.txt",'r') as f:
		str_txt=f.read()
	if (len(str_txt) == 0):
		print("start url is null");
		return "";
		
	try:
		
		urlarr = re.findall(r'-Subproject\s.+\n', str_txt)
		#print(urlarr);
		for  elem in urlarr:	
			picurl_str		= elem[len('-Subproject commit'):len(elem)];
			picurl_str = picurl_str.replace(" ", "");
			print(picurl_str)
			return picurl_str;
		
		return  "";
	except:
		print("git status result find err");	
		return  "";
	
def git_cmd_check():#使用 git status 检查 submoudle是否存在改动
	#os.system('git status -uno > git_status.txt');
	#time.sleep(1);
	str_txt = '';
	with open("git_status.txt",'r') as f:
		str_txt=f.read()
	if (len(str_txt) == 0):
		print("start url is null");
		return 1;
		
	try:
		#正则匹配改动
		urlarr = re.findall(r'modified\W.+new commits', str_txt)
		#print(urlarr);
		for  elem in urlarr:	
			
			picurl_str		= elem[len('modified:'):len(elem)-len('(new commits)')];
			#print(picurl_str)
			
			if picurl_str.find("api", 0, len(picurl_str)) > 0:
				print("path->"+picurl_str)
				os.system('git diff ' + picurl_str + ' > git_diff.txt');
				time.sleep(1);
				commit_id = git_get_diff_commit_id();
				print("commit_id = " + commit_id);
				#进入目录执行git check
				
				current_path = os.getcwd().replace(" ", "");
				picurl_str = picurl_str.replace("/","\\");
				picurl_str = picurl_str[3:len(picurl_str)];
				

				picurl_str.lstrip();
				print(current_path+"\\"+picurl_str+"\\");
				os.chdir(picurl_str);
				os.system('git checkout '+ commit_id);
				time.sleep(1);
				os.chdir(current_path);

			if picurl_str.find("libs", 0, len(picurl_str)) > 0:
				print("path->"+picurl_str)
				os.system('git diff ' + picurl_str + ' > git_diff.txt');
				time.sleep(1);
				commit_id = git_get_diff_commit_id();
				print("commit_id = " + commit_id);
				#进入目录执行git check
				
				current_path = os.getcwd().replace(" ", "");
				picurl_str = picurl_str.replace("/","\\");
				picurl_str = picurl_str[3:len(picurl_str)];
				

				picurl_str.lstrip();
				print(current_path+"\\"+picurl_str+"\\");
				os.chdir(picurl_str);
				os.system('git checkout '+ commit_id);
				time.sleep(1);
				os.chdir(current_path);
			
	except:
		print("git status result find err");
	

if __name__ == '__main__':
	git_cmd_check()

