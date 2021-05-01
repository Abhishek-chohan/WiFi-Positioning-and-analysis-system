import speedtest,time 
from random import randint
#st = speedtest.Speedtest()

def getDownloadSpeed():
	#speed=st.download()
	#speed=speed/8388608
	return [randint(1,50),time.time()]
	

def getUploadSpeed():
	speed=st.upload()
	speed=speed/8388608
	return [randint(1,50),time.time()]

def getPing():
	return randint(1,30)


def getServer():
	servernames =[] 
	#servers=st.get_servers() 
	print("===Server Info===")
	#config=st.get_config()
	#x=config.get("client")
	x={
	'ip' : 10,
	'lat' : 20,
	'lon' : 20,
	'isp' : 'isp',
	'isprating' : 3.7,
	'country' : 'IN'
	}
	return x
