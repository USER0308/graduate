import socket
import time

def networking(command):
	sk = socket.socket()
	server_ip = '192.168.99.100'
	sk.connect((server_ip, 1347))

	#time.sleep(5)
	#command = input('command:')
	b = 'blockHash'
	h = '\355\315\245\013\260\335\001\333@f\314)\273\021\322#V\243\352)X\024\326\020\363\300\343\267TR.5'
	#command = 'queryInfo'
	sk.sendall(bytes(command, encoding='utf-8'))
	server_reply = sk.recv(1024)
	while server_reply != 'end' and server_reply != '':
		# print 'recving...'
		print(server_reply)
		server_reply = sk.recv(1024)
		server_reply = server_reply.decode()
	sk.close()

if __name__ == '__main__':
	networking()
