#coding:utf-8
import time,os,re,urllib,urllib2,hashlib,sys
import os;
reload(sys)
sys.setdefaultencoding( "utf-8" );
def  creat_index():

	
	for page_num in range(139,149):
		creat_page_index(page_num);
		pathstr='blog/page'+str(page_num)+'/';
		
		page_txt = ''
		with open(pathstr+'page.index','r') as f:
			page_txt = f.read();
		with open('blog/index.data','a') as f:
			f.write(page_txt);
	#print('pathstr->'+pathstr);
	
	

def  creat_page_index(pagenum):

	pathstr='blog/page'+str(pagenum)+'/';
	print('pathstr->'+pathstr);
	
	isExists=os.path.exists(pathstr)
	if isExists:
		#print('exist');
		cmd = "find "+pathstr+' -name \"*.html\" | xargs ls -rt > '+ pathstr+'page.index';
		#print("cmd->"+cmd);
		os.system(cmd);
		#return 0;
	else:
		print('not exist');
		#os.system("mkdir -p "+pathfile)
		#os.makedirs(pathfile);
		
def err_log(dd):
	str_context='';
	with open("index.data",'r') as f:
		#f.write(log_data+'\n')	
		str_context = f.read();
		
	title_arr = str_context.split('\n');
	print('len='+str(len(title_arr)));
	
	html_str = '';
	html_str = html_str + '<html><body>'
	for elem in title_arr:
		if(len(elem) > 5):
			title_str = elem.split('/');
			#print(title_str[3][0:len(title_str[3])-5]);
			elem_str='';
			try:
				elem_str = '<a href=\"'+elem+'\">'+title_str[3][0:len(title_str[3])-5]+'</a>';
				elem_str = elem_str + '<br>';
			except:
				print(title_str);
				print('elem->'+elem);
				
			html_str=html_str+elem_str;

	html_str = html_str + '</body></html>';
	
	with open("blog_index.data",'w') as f:
		f.write(html_str)	
		
	#print(html_str);
if __name__ == '__main__':
	#err_log("111");
	
	for page_num in range(139,149):
		creat_page_index(page_num);
	
	creat_index();
	
	
	
	
	
	
	
	
	
	
	
	
	
	