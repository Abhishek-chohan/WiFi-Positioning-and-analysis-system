import speedtest,time 
from random import randint
st = speedtest.Speedtest()

def getDownloadSpeed():
	speed=st.download()
	speed=speed/8388608
	return [speed,time.time()]
	

def getUploadSpeed():
	speed=st.upload()
	speed=speed/8388608
	return [speed,time.time()]

def getPing():
	return st.results.ping


def getServer():
	servernames =[] 
	servers=st.get_servers() 
	print("===Server Info===")
	config=st.get_config()
	x=config.get("client")
	return x
