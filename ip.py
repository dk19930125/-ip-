#-*- coding: utf-8 -*- 
import threading
import socket
import time
routes = []
lock = threading.Lock()
class GetIp:
	@staticmethod
	def search_routers(PORT=80):
		local_ips = socket.gethostbyname_ex(socket.gethostname())[2]
		print local_ips
		all_threads = []
		for ip in local_ips:
			for i in range(1,255):
				array= ip.split(".")
				array[3] = str(i)
				new_ip = ".".join(array)
				# print new_ip
				t = threading.Thread(target=GetIp.check_ip,args=(new_ip,PORT))
				t.start()
				all_threads.append(t)
			for t in all_threads:
				t.join()
	@staticmethod
	def check_ip(new_ip,PORT=80):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(1)
		# PORT =80
		result = s.connect_ex((new_ip,PORT))
		if result == 0:
			lock.acquire()
			print "new_ip",new_ip
			lock.release()

if __name__ == "__main__":

	GetIp.search_routers(PORT=22)