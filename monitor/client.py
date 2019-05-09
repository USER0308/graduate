import socket
import time

def networking(command):
	sk = socket.socket()
	server_ip = '192.168.99.100'
	sk.connect((server_ip, 1347))

	#time.sleep(5)
	res = ''
	sk.sendall(bytes(command, encoding='utf-8'))
	server_reply = sk.recv(1024)
	res += server_reply.decode()
	while server_reply != 'end':
		# print 'recving...'
		print(server_reply)
		server_reply = sk.recv(1024)
		server_reply = server_reply.decode()
		res += server_reply
	sk.close()
	return res

if __name__ == '__main__':
	networking()
