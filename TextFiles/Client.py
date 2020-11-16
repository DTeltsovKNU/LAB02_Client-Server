import socket
import time

def log(m):
    log = open('log.txt', 'a+')
    log.write('Time: {0}\n{1}'.format(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()), m))
    log.close()

def sendtextfile(a):
    start_time = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 1027
    s.connect((host, port))
    m = 'Command: {0}\n'.format(a)
    s.send('Hello, server'.encode('utf-8'))
    m += 'Hello, server\n'
    f = open('testtosend.txt', 'rb')
    print('Sending...')
    m += 'Sending...\n'
    l = f.read(1024)
    print('Sending...')
    m += 'Sending...\n'
    s.send(l)
    f.close()
    print("Done Sending")
    m += 'Done Sending\n'
    print(s.recv(1024))
    s.close
    duration = time.time() - start_time  # время работы в секундах,
    print('Duration of operation: {0} seconds'.format(duration))
    m += 'Duration of operation: {0} seconds'.format(duration)
    log(m)

print("Hello, user. Please write command.\nCommand List:\n   Who\n   Upload\n   List\n   Bye")
while True:
    a = input()
    if a == 'Upload':
        sendtextfile(a)
    elif a == 'Who':
        print('Created by Dima Teltsov from K-27\nVariant 2:Text Files')
    elif a == 'List':
        print('Command List:\n   Who\n   Upload\n   List\n   Bye')
    elif a == 'Bye':
        exit()
    else:
        print('Hey, type commands from list')
    l = 'Command: {0}\n\n\n\n\n'.format(a)
