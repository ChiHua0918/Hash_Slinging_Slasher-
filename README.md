# Hash_Slinging_Slasher-
## 發展理念
考完期末考後熱愛狼人殺的大馬達想要辦個期末派對，邀請朋友們來家裡開趴，但是卻沒有甚麼東西能拿來布置，又覺得disco燈太過普通不想買，眼看著期末已經到來，苦無對策之下她找了LSA的助教們求救，最後在漢偉、蔣媽和BT的建議下想出了嗷嗚嗷嗚氣氛燈，並找了采禎、琪樺、亮亮來製作。

## 硬體設備
|設備名|圖片|來源
|-|-|-|
|樹梅派 Pi4|![line_20220113_175633](https://user-images.githubusercontent.com/82037691/149307980-c5d3bf63-8d61-42cb-8f9f-f6b718e01248.png)|柏瑋友情贊助
|USB全指向降噪麥克風(MIC-026)|![line_20220113_180207](https://user-images.githubusercontent.com/82037691/149308887-82bdc620-7907-4313-914e-660195fb562e.png)|欣華電子
|杜邦線<br/>1. 公對公<br/>2. 公對母<br/>3. 母對母|![line_20220113_180335](https://user-images.githubusercontent.com/82037691/149309132-00318bd0-60d0-4e21-9df2-3e78e46fc205.png)|今華電子
|5V 滴膠燈條 --- 型號(WS2812B)+控制器|![line_20220113_180502](https://user-images.githubusercontent.com/82037691/149309498-93166e59-4ddb-4cfe-a813-310b756eb80b.png)
|[蝦皮](https://shopee.tw/%E3%80%90%E4%B8%AD%E9%83%A8%E7%8F%BE%E8%B2%A8%E3%80%91%E7%8F%BE%E8%B2%A8-WS2812B-%E5%B9%BB%E5%BD%A9-%E5%85%A8%E5%BD%A9-%E7%87%88%E6%A2%9D-5V-%E6%BB%B4%E8%86%A0-%E5%BE%AE%E7%AC%91%E7%87%88-%E6%B0%A3%E5%A3%A9%E7%87%88-%E5%B0%BE%E7%AE%B1%E7%87%88-%E7%87%88%E6%A2%9D-%E8%B7%91%E9%A6%AC-%E6%B5%81%E6%B0%B4-WS2811-i.97901339.1600691516?gclid=Cj0KCQiAt8WOBhDbARIsANQLp97byEoNNos5V1EgUVSeY3ZC25vHB5ACzIDCwE-j21K9fjI-OGeNf4kaAri6EALw_wcB)
|一台裝有 Linux 的電腦 ||
## 如何進行
telegram bot
    用 telegram bot 玩狼人殺，所有玩家要先將機器人 @Hash_Slinging_Slasher_bot 加為好友，玩家們再創一個群組並將機器人加進群組，開始遊戲前，請先打 /prepare 準備，若要取消準備請打 /cancel ，遊戲開始請打 /start，如果想中止遊戲請打 /stop。
神職角色可以在個人與bot的聊天室中選擇使用技能與對象

## 套件
    語音辨識部分
    sudo apt install vlc
    cat /proc/asound/cards
    sudo vim /usr/share/alsa/alsa.conf
    pip3 install mutagen
    pip3 install pafy
    pip3 install youtube_dl
    pip3 install python-vlc
    pip3 install youtube-search
    pip3 install SpeechRecognition
    pip3 install python-vlc
    pip3 install python-pyaudio python3-pyaudio

    telegram bot
    pip3 install python-telegram-bot telegram bot
    pip3 install python-telegram-bot telegram bot
    pip3 install gtts 文字轉音檔
    pip3 install python-vlc apt install vlc 播放音檔
    pip3 install os 執行

    燈
    sudo apt -y install scons swig
    pip3 install rpi_ws281x
    git clone https://github.com/jgarff/rpi_ws281x.git
    sudo python ./python/setup.py install

## 參考資料
**telegram bot**
- [telegram bot 生成步驟](https://ithelp.ithome.com.tw/articles/10245264)
- [code 範例 --- python](https://www.programcreek.com/python/example/93148/telegram.Update)
- [漢偉撥放音樂](https://github.com/NCNU-OpenSource/MOLi-PA-Bot/blob/master/PABot.py)
- [InlineKeyboardButton 文件](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardbutton.html)
- [InlineKeyboardButton 按鈕點擊回應](https://hackmd.io/@truckski/HkgaMUc24)
- [set a poll 設投票](https://github.com/python-telegram-bot/python-telegram-bot/blob/ade1529986f5b6d394a65372d6a27045a70725b2/examples/pollbot.py#L134)
**燈**
- [哼歌也能带气氛的彩灯条](https://www.youtube.com/watch?v=XNWpQZbgFx0)
- [樹莓派LED像素屏 #1 - 介紹與驅動【明富其識】](https://www.youtube.com/watch?v=bAXOTc3Whzo&t=302s)
**語音辨識**
- [柏瑋組專題](https://github.com/NCNU-OpenSource/LSA_Project)
- [用Python來做 "聲音轉文字"](https://markjong001.pixnet.net/blog/post/246140004)
- [pyaudio 安裝](https://www.howtoinstall.me/ubuntu/18-04/python3-pyaudio/)
- [mp3play 無法使用](https://github.com/michaelgundlach/mp3play/issues/6)
- [播放以及暫停mp3檔](https://www.py4u.net/discuss/12316)
- [mpg123](https://askubuntu.com/questions/383014/stop-mpg123-without-being-in-its-shell)
- [漢偉組專題](https://github.com/NCNU-OpenSource/MOLi-PA-Bot)
- [python-threading 寫法](https://medium.com/ching-i/%E5%A4%9A%E5%9F%B7%E8%A1%8C%E7%B7%92-python-threading-52e1dfb3d5c9)
- [音頻長度](https://dev.to/konyu/how-to-get-mp3-file-s-durations-with-python-42p)
## 感謝名單
> 照片拍攝 --- 蔣媽
> LED燈連接問題 --- 蔡琳瀠
> 燈條焊接、telegram bot 問題詢問 --- 漢偉
> 關鍵字、有趣靈感來源 --- 學而
> 器材提供 --- 蓬萊人偶
> 代買器材 --- 嚴彥婷
