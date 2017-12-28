# -*- coding: utf-8 -*-
import os,re;

def debug_test():
	with open("【十张内涵图 3月1日】妹子急了，啥事都能做得出来啊！.html",'r') as f:
		
		
		
		
		
		
		
		str_txt = str_txt=f.read();
		str_arr = str_txt.split('.jpg');
		print(len(str_arr));
		for i in range(0,len(str_arr)-1) :
			elem = str_arr[i];
			elem_str = elem.decode('utf-8')+'.jpg';
			strinfo = re.compile(r'<(.|\n)*?>');
			elem_str = strinfo.sub('', elem_str);
			elem_str = elem_str.replace('&nbsp;','');
			elem_str = elem_str.strip();
			pic_arr = re.findall(r'[A-Za-z0-9]+\.jpg',str_txt)
			
			text = elem_str.split('<img')[0];
			text = text[1:len(text)];
			strinfo = re.compile(r'style=\".*?\">');
			text = strinfo.sub('',text);
			print(text);
			print(pic_arr[0])
		
		#urlarr = re.findall(r'<img\b.*?data-src=\".*?>',str_txt)
		#for  elem in urlarr:			
		#	tmp_url_arr = re.findall(r'\ssrc=\".*?\"',elem);
		#	tmp_url = tmp_url_arr[0].strip()
		#	tmp_url = tmp_url[len('src="'):len(tmp_url)-1]
		#	print(tmp_url);
		#	print('----------');
		#	str_txt = str_txt.replace(tmp_url,str(count)+'.jpeg');
		#strinfo = re.compile(r'data-src=\".*?\"')
		#str_txt = strinfo.sub('', str_txt)
		#strinfo = re.compile(r'<script(.|\n)*?</script>')
		#str_txt = strinfo.sub('', str_txt)
		
		#title_str = title_arr[0]
		#print(str_txt)
		#str_txt = str_txt.strip()
		#print('stripe->'+str_txt)
		#try:
		#	with open(str_txt+".html",'wb') as f:
		#		f.write(str_txt)
		#except:
		#	print('save err')
			
			
if __name__ == '__main__':
	debug_test();

	
	
	
	
	
	
	
	
	