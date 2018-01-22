#coding:utf-8
#-*-coding:utf-8-*-
import time,os,re,urllib,urllib2,hashlib,sys
import os;
import imghdr;
reload(sys)
sys.setdefaultencoding( "utf-8" );

		
def creat_html():
	str_context='';
	with open("blog/picindex.data",'r') as f:
		#f.write(log_data+'\n')	
		str_context = f.read();
		
	title_arr = str_context.split('\n');
	print('len='+str(len(title_arr)));
	
	html_str = '';
	#html_str = html_str + '<html><body>'
	for elem in title_arr:
		if(len(elem) > 5):
			
			#title_str = elem.split('/');
			#print(title_str[3][0:len(title_str[3])-5]);
			#path_str=title_str[0]+'/'+title_str[1]+'/'+title_str[2]+'/';
			
			path_str='blog/'+elem[2:len(elem)];
			result = imghdr.what(path_str);
			print(result);
			#html_str = html_str +elem +';'+result+'\n'
			#print(elem);
			#elem_str='';
			#try:
			#	elem_str = '<a href=\"'+elem+'\">'+title_str[3][0:len(title_str[3])-5]+'</a>';
			#	elem_str = elem_str + '<br>';
			#except:
			#	print(title_str);
			#	print('elem->'+elem);
			#	
			#html_str=html_str+elem_str;

	#html_str = html_str + '</body></html>';
	
	#with open("blog_index.html",'a') as f:
	#	f.write(html_str)
		
	#print(html_str);
def  scan_html():
	str_context='';
	with open("blog/index.data",'r') as f:
		#f.write(log_data+'\n')	
		str_context = f.read();
		
	title_arr = str_context.split('\n');
	print('len='+str(len(title_arr)));
	
	html_str = '';
	#html_str = html_str + '<html><body>'
	for elem in title_arr:
		if(len(elem) > 5):
			
			title_str_arr = elem.split('/');

			path_str = title_str_arr[0]+'/'+title_str_arr[1]+'/'+title_str_arr[2]+'/';
			html_path_file = elem;
			
			print(html_path_file);
			
			orig_txt = '';
			with open(html_path_file.decode('utf-8'),'r') as f:
				orig_txt = f.read();
			
			
			pic_name_arr=re.findall(r'[0-9]{2}_.+?jpg',orig_txt);
			for  pic_path in pic_name_arr:
				try:
					result = imghdr.what(path_str+pic_path);
					new_filename=pic_path.replace('jpg',result);
					mv_cmd = 'mv ' + path_str+pic_path + ' ' +path_str+new_filename;
					os.system(mv_cmd);
					#orig_txt .replace();
					orig_txt  = orig_txt.replace(pic_path, new_filename);
				except:
					print('imghdr err');
				#print(path_str+pic_path);
				
				
				#print(path_str+new_filename);
				
				# mv							
			with open(html_path_file.decode('utf-8'),'w') as f:
				f.write(orig_txt);
			#break;
			#path_str=title_str[0]+'/'+title_str[1]+'/'+title_str[2]+'/';
			

			#html_str = html_str +elem +';'+result+'\n'
			#print(elem);
			#elem_str='';
			#try:
			#	elem_str = '<a href=\"'+elem+'\">'+title_str[3][0:len(title_str[3])-5]+'</a>';
			#	elem_str = elem_str + '<br>';
			#except:
			#	print(title_str);
			#	print('elem->'+elem);
			#	
			#html_str=html_str+elem_str;

	#html_str = html_str + '</body></html>';
	
	#with open("blog_index.html",'a') as f:
	#	f.write(html_str)
		
	#print(html_str);	
if __name__ == '__main__':
	
	scan_html();
	
	
	
	
	
	
	
	