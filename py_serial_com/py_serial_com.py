# -*- coding: utf-8 -*-
import os,re;
import serial
import serial.tools.list_ports
import tkinter
from tkinter import messagebox
import py_windows
plist_com = list(serial.tools.list_ports.comports())
# serial_g_hd  ;
def serial_com_list():
	# serial.tools
	if len(plist_com) <= 0:
		print ("The Serial port can't find!")
	else:
		for e in plist_com:
			print(e)
		# plist_0 =list(plist[0])
		# serialName = plist_0[0]
		# serialFd = serial.Serial(serialName,9600,timeout = 60)
		# print ("check which port was really used >",serialFd.name)
	return 0;
MAX_BUF_SIZE = 100
def open_com_read_data():

	try:
		read_data = bytearray(MAX_BUF_SIZE)
		read_len = 0;
		#端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
		portx="COM8"
		#波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
		bps=115200
		#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
		timex=1
		# 打开串口，并得到串口对象
		serial_g_hd=serial.Serial(portx,bps,timeout=timex)

		# print("串口详情参数：", serial_g_hd)
		print(serial_g_hd.port)#获取到当前打开的串口名
		print(serial_g_hd.baudrate)#获取波特率
		# 写数据
		# result=serial_g_hd.write("我是东小东".encode("gbk"))
		# print("写总字节数:",result)

		# while True:
		# 	if(read_len < 5):
		# 		# read_data.append (int(serial_g_hd.read(1).decode("int")))
		# 		b_temp = serial_g_hd.read(MAX_BUF_SIZE);

		# 		read_len = read_len + 1;
		# 		print(b_temp);

		# 	else:
		# 		break;

		read_data = serial_g_hd.read(MAX_BUF_SIZE);
		data_parse(read_data)
		# print(read_data)

		serial_g_hd.close()#关闭串口

	except Exception as e:
		print("---异常---：",e)
		serial_g_hd.close()#关闭串口


	return 0;


list_lock_type = ["单密码用户 开锁", "单指纹用户  开锁", "一次性密码用户 开锁", "密码+密码 开锁",
                  "密码+指纹  开锁", "指纹+指纹 开锁", "APP蓝牙 开锁", "门内开锁 开锁", "门内上锁 开锁",
                   "门外上锁 开锁",  "nfc开锁 开锁",  "nfc+指纹 开锁",  "指纹+nfc 开锁", "nfc+密码 开锁",  "密码+nfc 开锁",
                   "nfc+nfc 开锁"];
def get_lock_type(type_id):
	#锁方式描述
	print(list_lock_type[type_id]);
	return list_lock_type[type_id];



def data_parse(  bydata):
	if(bydata[0] == 0xaa and  bydata[1] == 0x01):
		print("found head aa 01")
		if(bydata[3] == 0x05 and  bydata[4] == 0x0c):
			print("cmd = 0x05 0c")
			data_seg_len = bydata[5]*256 + bydata[6];
			print("data segment len=", str(data_seg_len))

			off_set = 0;

			items_nums = 0;
			if(bydata[7] == 0x00):
				items_nums = bydata[8];

			print("共有:" + str(items_nums) + "记录");

			while True:
				if(off_set >= items_nums):
					break;
				else:
					t1 = bydata[9+(off_set*3)]#锁方式描述
					t2 = bydata[9+(off_set*3)+1]#id 1
					t3 = bydata[9+(off_set*3)+2]#id2
					print("lock_type="+str(t1)+",id1:"+str(t2)+",id2:",str(t3));
					off_set = off_set + 1;

	print(bydata);

def my_test2():
	x = bytearray(5)
	x[0] = 0x01
	print(x)
	return 0;
def my_test3():
	print("hello world3\n");
	return 0;




if __name__ == '__main__':
	# serial_com_list();
	# open_com_read_data();
	testdata = bytearray(100);
	testdata[0] = 0xaa;
	testdata[1] = 0x01;

	testdata[2] = 0xaa;

	testdata[3] = 0x05;
	testdata[4] = 0x0c;

	testdata[5] = 0x00;
	testdata[6] = 0x03;

	testdata[7] = 0x00;

	testdata[8] = 0x03;# 记录数量

	testdata[9] = 0x03;
	testdata[10] = 0x06;
	testdata[11] = 0x04;

	testdata[12] = 0x05;
	testdata[13] = 0x07;
	testdata[14] = 0x04;

	testdata[15] = 0x0a;
	testdata[16] = 0x07;
	testdata[17] = 0x04;

	data_parse(testdata);

	py_windows.window_start();


	# my_test3();








