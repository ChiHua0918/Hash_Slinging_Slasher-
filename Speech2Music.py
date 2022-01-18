import threading
import time
import pafy
import speech_recognition
import vlc
from youtube_search import YoutubeSearch
import subprocess


# play song
def play(type, url) :
    global playStatus, playing_thread
    print("come in play")
    if type == 'local' :
        player = vlc.MediaPlayer('./'+url)
    else :
        url = "https://www.youtube.com" + url
        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl() 
        player.set_media(Media)
    player.play()
    # wait for play
    time.sleep(5)
    playStatus = 'play'
    # if the song end (player.is_playing() will become 0)
    while playStatus != 'stop' and (player.is_playing() == 1) :
        pass
    player.stop()
    playStatus = 'stop'
    playing_thread = None
    return

# find song 
def search(msg) :
    print("找歌名")
    result = YoutubeSearch(msg, max_results=1).to_dict()[0]
    print("https://www.youtube.com" + result['url_suffix'])
    return result['url_suffix']

def checkKeyword(mySentence) :
    global playStatus, msg, pre_msg
    type = ["鬼故事", "放鬆", "派對", "狼人殺", "睡覺",
            "聖誕", "新年", "延畢", "夜光閃亮亮復仇鬼", "打*", 
            "激烈做愛", "生日", "真相永遠只有一個", "紅鯉魚與綠鯉魚與驢", "音樂",
            "關燈", "重灌"] # 音樂
    result = ["creepy", "relax", "party", "startWerewolf", "sleep", 
              "Christmas", "NewYear", "thePurge", "fu-chou-gui", "pao", 
              "clap", "Birthday", "conan", "so", "music",
              "turnOff", "WTM"]
    if pre_msg == '音樂' :
        searchResult = search(mySentence)
        print(searchResult)
        playing_thread = threading.Thread(target=play, args=('YT', searchResult))
        playing_thread.start()
        pre_msg = None
        command = "python3 sendRequest.py music"
        subprocess.Popen(command, shell=True)
        return
    if ("暫停" in mySentence) :
        playStatus = 'stop'
        command = "python3 sendRequest.py turnOff"
        subprocess.Popen(command, shell=True)

        playing_thread = None
        return

    for i in range(len(type)) :
        if (type[i] in mySentence) :
            print("bingo" + result[i])
            playStatus = 'stop'
            playing_thread = None
            playing_thread = threading.Thread(target=play, args=('local', result[i]+'.mp3'))
            playing_thread.start()
            print("76行")
            # send request
            command = "python3 sendRequest.py " + result[i]
            subprocess.Popen(command, shell=True)
            if pre_msg != '音樂' and type[i] == '音樂' :
                # set pre_msg to MUSIC
                pre_msg = '音樂'
 
 

def Voice_To_Text():
    print("get in voice")
    rr = speech_recognition
    r = rr.Recognizer()
    with speech_recognition.Microphone() as source:
        print("請開始說話:") 
        r.adjust_for_ambient_noise(source)     # 函數調整麥克風的噪音:
        audio = r.listen(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")
    except rr.UnknownValueError:
        Text = "無法翻譯"
        time.sleep(2)
    except rr.RequestError as e:
        Text = "無法翻譯" # {0}".format(e)
        # 兩個 except 是當語音辨識不出來的時候 防呆用的
    return Text

def main() :
    print ('Listening ...')
    while(True) :
        msg = str(Voice_To_Text())
        print(msg)
        if (msg != "無法翻譯") :
            checkKeyword(msg)
        time.sleep(0.5)


pre_msg = None
playStatus = None
playing_thread = None

main()