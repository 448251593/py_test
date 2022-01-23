# -*- coding: utf-8 -*-
import os,re
from time import sleep;
import serial
import serial.tools.list_ports
import tkinter
from tkinter import messagebox
import py_windows
import threading

serial_g = serial;
# adc通道
ADC_VCC_CHANNEL_ID = 1
ADC_X_CHANNEL_ID = 2
ADC_Y_CHANNEL_ID = 3
#电机编号
MOTOR_X_ID = 1
MOTOR_Y_ID = 2
#电机动作
MOTOR_MOVE_CLOCKWISE = 1
MOTOR_MOVE_COUNTERCLOCKWISE = 2

# def rcv_data():
    # while True:
    #     rcv=serial_g.readline()
    #     rcv=rcv.decode() 
    #     print("ser_recv:"+rcv)

def bcg_shakehand_device():
	send_data = "BCG_SHAKEHAND\n"
	serial_g.write(send_data.encode())
	print("send shakehand\n")

	rcv=serial_g.readline()
	rcv=rcv.decode() 
	print("recv:", rcv)
	if rcv.find("OK") >=0 :
		print("设备通讯正常")
		return 1;
	else:
		print("设备通讯超时")
		return 0;

def  get_adc_cfg(adc_ch):
	#adc_ch 只能1, 2 , 3
	send_data = "BCG_ADC_CFG,1,"+str(adc_ch)+"\n"
	serial_g.write(send_data.encode())
	print("send "+ send_data)
	rcv=serial_g.readline()
	rcv=rcv.decode() 
	print("recv:"+str(adc_ch)+str(rcv))
	if rcv.find("OK") >=0 :
		print("ok")
		return  1;
	else:
		print("failed")
		return  0;
def  get_adc_xy(adc_ch):
	if get_adc_cfg(adc_ch) == 0:
		return  0;
	#adc_ch 只能1, 2 , 3
	send_data = "BCG_ADC_R,1,"+str(adc_ch)+"\n"
	serial_g.write(send_data.encode())
	print("send "+ send_data )

	rcv=serial_g.readline()
	rcv=rcv.decode() 
	print("recv:", rcv)
	if rcv.find("OK") >=0 :
		adc_val = rcv[rcv.find("OK,")+3:len(rcv)-1];
		print("adc"+str(adc_ch)+"=" + adc_val)
		return adc_val;
	else:
		print("设备通讯超时")
		return 0;


def  bcg_motor_move(motorx_y, direct_xy):
	if motorx_y == MOTOR_X_ID:
		if direct_xy == MOTOR_MOVE_CLOCKWISE:
			print("motorx left")

		else:
			print("motorx right")
	else:
		if direct_xy == MOTOR_MOVE_CLOCKWISE:
			print("motory left")
		else:
			print("motory right")

def  bcg_sun_trace_pro():

	while 1:
		adc_x_val = get_adc_xy(ADC_X_CHANNEL_ID);
		sleep(0.1);
		adc_y_val = get_adc_xy(ADC_Y_CHANNEL_ID);
		sleep(0.1);
		adc_x_val_f = (float(adc_x_val)/1024)*3.3
		adc_y_val_f = (float(adc_y_val)/1024)*3.3
		print("adcx="+str(adc_x_val_f)+"adcy="+str(adc_y_val_f))
		# if adc_x_val < 500 :
		# 	bcg_motor_move(1, 1)
		# 	print("水平左移动")
		# elif  adc_x_val < 600:
		# 	bcg_motor_move(1, 0)
		# 	print("水平又移动")

		# if adc_y_val < 500 :
		# 	bcg_motor_move(0, 1)
		# 	print("垂直上移动")
		# 	bcg_motor_move(0, 0)
		# elif  adc_y_val < 600:
		# 	print("垂直下移动")


		sleep(1);
if __name__=='__main__':
	port_list = list(serial.tools.list_ports.comports())
	k=0
	for i in port_list:
		print(i,k)
		k=k+1

	if len(port_list) <= 0:
		print("not find serial")
	else:
		serial_k=input("please switch serial:")
		k = int(serial_k)
		serial_list = list(port_list[k])
		serialName = serial_list[0]
		#print(serialName)
		serial_g=serial.Serial(serialName,115200,timeout=0.5)

		# th=threading.Thread(target=rcv_data)
		# th.setDaemon(True)
		# th.start()

		if serial_g.isOpen():
			print("open succeed >",serial_g.name)
		else:
			print("open failed >",serial_g.name)

		bcg_shakehand_device()
		bcg_sun_trace_pro()
		# count_g = 1
		# while True:
		# 	# send_data=input("=>")
		# 	send_data = str(count_g) +"\n"
		# 	serial_g.write(send_data.encode())
		# 	sleep(1)
		# 	count_g = count_g + 1;
        #  data=serial_g.read(1)
        #  data = (data + serial_g.read(serial_g.inWaiting())).decode()
        #  print(data)








