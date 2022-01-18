import threading
import time
import pafy
import speech_recognition
import vlc
from youtube_search import YoutubeSearch
import subprocess

# 播歌
def play(type, url) :
    global playStatus, playing_thread
    # 音樂在本地電腦
    if type == 'local' :
        player = vlc.MediaPlayer('./'+url)
    # 到 youtube 上搜尋
    else :
        url = "https://www.youtube.com" + url
        # 找該 youtube 影片的資訊
        video = pafy.new(url)
        # 用最好的流量方式播放
        best = video.getbestaudio()
        playurl = best.url
        # 把網址加入 vlc 播放等候清單
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
    # 播放
    player.play()
    # 等待播放
    time.sleep(5)
    playStatus = 'play'
    # 如果沒有按停止或是歌曲還沒播放完畢
    while playStatus != 'stop' and (player.is_playing() == 1) :
        pass
    # 停止播放
    player.stop()
    # 把播放狀態換成停止
    playStatus = 'stop'
    # 把 thread 關掉
    playing_thread = None
    return

# 找歌 
def search(msg) :
    # 在 youtube 上搜尋 msg 並回傳第一個結果
    result = YoutubeSearch(msg, max_results=1).to_dict()[0]
    # 印出找到的網址
    print("https://www.youtube.com" + result['url_suffix'])
    return result['url_suffix']

# 檢查關鍵字
def checkKeyword(mySentence) :
    global playStatus, msg, pre_msg
    # 關鍵詞
    type = ["鬼故事", "放鬆", "派對", "狼人殺", "睡覺",
            "聖誕", "新年", "延畢", "夜光閃亮亮復仇鬼", "打*", 
            "激烈做愛", "生日", "真相永遠只有一個", "紅鯉魚與綠鯉魚與驢", "音樂",
            "關燈", "重灌"] 
    # mp3 音檔名稱
    result = ["creepy", "relax", "party", "startWerewolf", "sleep", 
              "Christmas", "NewYear", "thePurge", "fu-chou-gui", "pao", 
              "clap", "Birthday", "conan", "so", "music",
              "turnOff", "WTM"]
    # 如果關鍵詞是'音樂'
    if pre_msg == '音樂' :
        searchResult = search(mySentence)
        # print(searchResult)
        # 另開一個 thread 來執行播放音樂這個 function
        playing_thread = threading.Thread(target=play, args=('YT', searchResult))
        playing_thread.start()
        pre_msg = None
        # 開啟副執行續傳送 request
        command = "python3 sendRequest.py music"
        subprocess.Popen(command, shell=True)
        return
    # 關鍵詞為"暫停"
    if ("暫停" in mySentence) :
        # 把播放狀態換成停止
        playStatus = 'stop'
        # 開啟副執行續傳送 request
        command = "python3 sendRequest.py turnOff"
        subprocess.Popen(command, shell=True)
        # 關閉播放音樂的 thread
        playing_thread = None
        return

    # 如果語句中有關鍵詞
    for i in range(len(type)) :
        if (type[i] in mySentence) :
            # print("bingo" + result[i])
            playStatus = 'stop'
            playing_thread = None
            playing_thread = threading.Thread(target=play, args=('local', result[i]+'.mp3'))
            playing_thread.start()
            command = "python3 sendRequest.py " + result[i]
            subprocess.Popen(command, shell=True)
            # 防止重複的傳入音樂兩次搜尋歌名
            if pre_msg != '音樂' and type[i] == '音樂' :
                pre_msg = '音樂'

# 語音辨識
def Voice_To_Text():
    rr = speech_recognition
    r = rr.Recognizer()
    with speech_recognition.Microphone() as source:
        print("請開始說話:") 
        # 函數調整麥克風的噪音
        r.adjust_for_ambient_noise(source)
        # 凝聽聲音
        audio = r.listen(source)
    try:
        # 辨識語言設為中文
        Text = r.recognize_google(audio, language="zh-TW")
    except rr.UnknownValueError:
        Text = "無法翻譯"
        time.sleep(2)
    except rr.RequestError as e:
        Text = "無法翻譯" 
        # 兩個 except 是當語音辨識不出來的時候防呆用的
    # 回傳辨識出的文字
    return Text

def main() :
    # 每完成一個辨識後，休息 0.5 秒後重新辨識
    while(True) :
        msg = str(Voice_To_Text())
        print(msg)
        if (msg != "無法翻譯") :
            # 檢查語句中是否有關鍵詞
            checkKeyword(msg)
        time.sleep(0.5)

# 儲存上次的辨識訊息(專門記錄有沒有重複說出"音樂")
pre_msg = None
# 儲存播放狀態
playStatus = None
# 儲存 thread
playing_thread = None

main()