# web server

from flask import Flask, request, make_response
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index() :
    formData = request.args['mode']    # request 傳來的 mode 值 (關鍵字)
    print(formData)

    myKeyWord(formData)

    return make_response('OK', 200)

# myKeyWord(): 將傳來的關鍵字轉傳到開燈的程式(lightMode.py)
# formdata: request 的關鍵字
def myKeyWord(formData) :
    global p

    # result: 關鍵字清單
    result = ["creepy", "relax", "party", "startWerewolf", "sleep", 
              "Christmas", "NewYear", "thePurge", "fu-chou-gui", "pao", 
              "clap", "Birthday", "conan", "so", "music",
              "turnOff", "WTM", "werewolf", "witch", "predictor",
              "breakingDawn"]

    # 如果前面還有 process, 先暫停(kill)它
    if p != None :
        p.kill()
        p = None
    
    # 將關鍵字傳到 lightMode.py 點亮對應的燈光模式
    # result.index(formData): 關鍵字編號
    p = Popen(["python3", "lightMode.py", str(result.index(formData))], stdout=PIPE, stderr=STDOUT)

# 開燈的 process
p = None

if __name__ == "__main__":
    # 啟動 server
    app.run(host='0.0.0.0', port=8081, threaded=True, debug=True)