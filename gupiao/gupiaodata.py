#coding:utf-8
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys
import sqlite3;
import imghdr;
import json;

reload(sys)
sys.setdefaultencoding( "utf-8" );




pathfile = 'MEIZITU/';
		

	
def exe_main(count):


	
	with open("gupiao.txt",'r') as f:
		str_txt=f.read()
	if (len(str_txt) ==0):
		print("data is null");
		return ;
	

	try:
		text = json.loads(str_txt);
		# print(text["dates"]);
		over_price = [];
		price_arr = text["price"].split(",");
		for i in range(0,len(price_arr)):
			if(i % 4 == 0):
				# over_price = over_price + str(int(price_arr[i])+int(price_arr[i+3])) +"\n";
				over_price.append( str(int(price_arr[i])+int(price_arr[i+3])));
		
		# with open("over_price.txt",'w') as f:
		# 	f.write(over_price);
		
							
		year_all = "";
		year_index = 0;

		data_arr = text["dates"].split(",");

		for j in range(0, len(text["sortYear"])):
			for i in range(0, int(text["sortYear"][j][1])):
				month_t = str(data_arr[year_index]);
				if (int(month_t[0:2]) == 1 or int(month_t[0:2]) == 12):
					year_all = year_all + str(text["sortYear"][j][0]) +"/"+ month_t[0:2] +"/" + month_t[2:4]+ ","+over_price[year_index]+"\n";
				year_index = year_index + 1;
	
		print(year_all);
		with open("year.txt",'w') as f:
			f.write(year_all);


	except:
		print("json load err");
	

if __name__ == '__main__':
	# test_s = '12134567';
	# print(test_s[2:4]);
	# print(test_s[2:2]);
	exe_main(2);

