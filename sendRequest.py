import requests
import sys

def main(argv):
    #讀入需要的參數
    mode = argv[0]   #發光模式
    file = open("server_ip.txt", mode='r')
    ip = file.read().strip()    #IP


    #發出request
    command = 'http://' + ip + ':8081/?mode=' + mode
    r= requests.get(command)
    print('Pi server response :', r.text)

if __name__ == '__main__':
    main(sys.argv[1:])
