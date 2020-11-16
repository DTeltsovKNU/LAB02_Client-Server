import socket
import time
def writefile(l):
    f = open('testtorecv.txt', 'wb+')
    f.write(l)
    print(l)
    f.close()

def log(m):
    f = open('log.txt', 'a+')
    f.write('Time: {0}\nEvent:\n {1}'.format(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()), m))
    f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1027
s.bind((host, port))
s.listen(1)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    m = 'Got connection from {0}\n'.format(addr)
    print(c.recv(1024))
    print("Receiving...")
    m += "Receiving...\n"
    l = c.recv(1024)
    writefile(l)
    print("Done Receiving")
    m += "Done Receiving\n"
    c.send('Thank you for connecting'.encode('utf-8'))
    m +='Thank you for connecting\n\n\n\n\n'
    c.close()  # Close the connection
    log(m)
