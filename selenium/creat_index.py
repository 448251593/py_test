#coding:utf-8
import time,os,re,urllib,urllib2,hashlib,sys
import os;
reload(sys)
sys.setdefaultencoding( "utf-8" );

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
	err_log("111");