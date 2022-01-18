import requests
import sys

def main(argv):
    #讀入需要的參數
    mode = argv[0]   #發光模式
    ip = '192.168.1.82'   #IP


    #發出request
    command = 'http://' + ip + ':8081/?mode=' + mode
    requests.get(command)
    # print('Pi server response :', r.text)

if __name__ == '__main__':
    main(sys.argv[1:])
