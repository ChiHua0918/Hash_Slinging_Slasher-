# README

## Concept Development 理念
熱愛狼人殺的大馬達想要在考完期末考後辦個期末派對，邀請朋友們來家裡開趴，但是卻沒有甚麼東西能拿來布置 QAQ
眼看著期末已經到來，苦無對策之下她找了 LSA 的助教們求救，最後在漢偉、蔣媽和BT的建議下想出了**嗷嗚嗷嗚氣氛燈**，並找了采禎、琪樺、亮亮來製作。

## Implementation Resources 設備資源

|設備名|來源|
|-|-|
|樹梅派 Pi4|柏瑋友情贊助|
|USB全指向降噪麥克風(MIC-026)|欣華電子|
|杜邦線<br/>1. 公對公<br/>2. 公對母<br/>3. 母對母|今華電子|
|5V 滴膠燈條 --- 型號(WS2812B)+控制器|[蝦皮](https://reurl.cc/rQRDoN)
|一台裝有類 Linux 的電腦，並且可以錄音及收音 | 自己的電腦 |

## Implementation Process 實作過程
- 本次實作分為三部分來解說過程：燈光、語音辨識播音樂、Telegram bot
### installation 安裝套件
**安裝 pip3**
```terminal=
sudo apt install python3-pip
```
**下載 git**
```rerminal=
sudo apt install git
```
**clone 燈條套件**
- python 沒有內建 ws281x 的套件，所以要用樹莓派點亮 
- 之後安裝套件和執行程式都在`/rpi_ws281x/python/examples/`這個目錄下進行
```terminel=
clone https://github.com/jgarff/rpi_ws281x.git`
```
**語音辨識部分**
```terminal=
sudo apt install vlc
pip3 install mutagen
pip3 install pafy
pip3 install youtube_dl
pip3 install python-vlc
pip3 install youtube-search
pip3 install SpeechRecognition
```
**telegram bot**
```terminal=
pip3 install python-telegram-bot
pip3 install gtts
pip3 install python-vlc 
sudo apt install vlc
```
**燈光**
```terminal=
pip3 install rpi_ws281x
sudo python ./python/setup.py install
```

### 【燈光】
- 由樹莓派控制燈號。
- 樹莓派是 server 負責接收語音辨識程式或 telegram bot 傳送過來的燈光 requests。
#### 接線
- 由於樹莓派 GPIO 供電不足以點亮整座燈條，需要外接電源。
- 將 5 條電線焊接到燈條的輸入端。
    - 2 條紅色電線：供電
    - 2 條黑色電線：接地
    - 1 條綠色電線：傳送訊號
- 將 5 條電線分別插到對應的位置。
    - 1 條紅線接4號(正極、5v Power)
    - 1 條黑線接6號(接地)
    - 1 條綠線接12號(DataIn、GPIO 18)
    - 剩下 1 條紅線和 1 條黑線接到 5V2A 的供電器
    <img src = "https://i.imgur.com/0ydY6td.png" width = "400px">
- 測試套件是否安裝成功。
    - 把`strandtest.py` 的 `LED_COUNT` 改成自己的燈條上的單元數量。
    - 執行這個檔案，若可以點亮燈光代表安裝成功。
    ```terminal=
    sudo python3 strandtest.py
    ```
    <img src = "https://i.imgur.com/gM87SWb.png" width = "200px">
- 啟動 server。
    - 把 `lightServer.py` 和 `lightMode.py` 放到此目錄下
    ```terminal=
    sudo python3 lightServer.py
    ```
### 【語音辨識 & 音樂】
- 程式偵測在語句中提到關鍵詞，會播放相對應的音樂(.mp3)，並傳送亮燈的 requests 給樹莓派
    - 如果一句內有2個以上的關鍵詞，會以程式碼中排列順序覆蓋前面的音樂和 request
- 在 linux 系統電腦下載以下幾個檔案後放到一目錄下
     - `Speech2Music.py`
     - `bot.py`
     - `sendRequest.py`
     - 所有 mp3 檔
- 設定關鍵字
    - 有三個地方分別儲存執行程式所需的關鍵字，請自行設定新的關鍵字、mp3 檔、燈光模式，三者在各 list 的位置必須相同

| 所在檔案 | 變數名 | 儲存資料 |
| ---- | ---- | ----- |
|`Speech2Music.py` | `type` | 語音關鍵字 |
|`Speech2Music.py` | `result` | mp3 檔名 (不用打.mp3) |
|`lightServer.py` | `lightMode` | 燈光模式  (Function name) |
- 執行程式
```terminal=
python3 Speech2Music.py
```

### 【Telegram Bot】
- 這是一個半自動的狼人殺 bot，由 bot 當主持人主持狼人殺遊戲，並且適時播放聲音、向 server 發切換燈光模式的 requests。
- 遊戲進行時，依序進入到各個模式（狼人、女巫、預言家），發出**主持語音**、**音效**及燈光模式的 request。
- 狼人殺中每一種模式都有：
    - 對應音效
    - 對應語音
    - 對應燈光模式
#### 生成 telegram bot 
- 到 telegram 搜尋 @BotFather 
- 然後按 `/start`
- 創造機器人 `/newbot`
- 輸入要創建機器人的名字
- 輸入要創建機器人的 username
- 成功後即可獲得機器人的連結 & token
<img src = "https://i.imgur.com/cuWVSpH.jpg" width = "300px">
  > 紅色框框中為 token
- 將 token 儲存到 token.txt ， 並移動到和`bot.py`相同資料夾內
#### telegram bot 增加 command
- 查詢創建完畢的 bot `/mybots`
<img src = "https://i.imgur.com/wAmMG0Q.jpg" width = "300px">
- 點選 Edit bot
<img src = "https://i.imgur.com/aDAddd1.jpg" width = "300px">
- 點選 Edit Commands
- 輸入
    ```text＝
    introduce  介紹 telegram bot 的作用
    listprepare  列出所有準備中的玩家
    prepare  玩家準備
    cancel  取消準備
    start  遊戲開始
    stop  遊戲中止
    poll   玩家白天投票選項
    ```

#### 在 telegram bot 上的指令
-  機器人名字: @Hash_Slinging_Slasher_bot
`/introduce` 介紹創造 telegram bot 的動機
`/listprepare` 列出所有準備中的玩家
`/prepare` 玩家準備
`/cancel` 取消準備
`/start_game` 遊戲開始
`/stop_game` 遊戲中止
`/poll` 玩家白天投票選項

### 執行準備
1. 樹莓派和電腦連線到同一個網域
2. 樹莓派執行 `lightServer.py`
2. `sendRequest.py` 中的 ip 設定成 pi 的 ip 
3. 類 linux 電腦執行 `bot.py` 或 `Speech2Music.py`
    - `lightServer.py`：控制燈光模式的 server
    - `bot.py`：執行 Telegram Bot
    - `Speech2Music.py`：語音辨識播放音樂
4. 如果要玩狼人殺,請**先將 @Hash_Slinging_Slasher_bot 加為好友**，並自行創立群組遊玩

### 執行
#### 玩狼人殺
- 玩家用這個程式玩狼人殺需要在 2 個聊天室切換
    - 一是單一玩家和 Telegram bot 各自的私人聊天室，用來執行各個角色所需的工作，以下簡稱【私聊】。
    - 二是所有玩家和 Telegram bot 共組的群組聊天室，以下簡稱【遊戲群】。

1. 玩家們需先將機器人 @Hash_Slinging_Slasher_bot 加為好友，並另外建立遊戲群加入機器人。
2. 【遊戲群】玩家們已經準備好開始遊戲後，各自在聊天室輸入`/prepare`。
    - 若要取消準備，輸入 `/cancel`。
3. 【遊戲群】所有玩家都準備好後，其中一位玩家打`/start`，遊戲即開始進行。
    - 此時程式會依玩家輸入`/prepare`的順序決定玩家編號並確認遊玩人數後，隨機分配角色。
    - 如果想中止遊戲請打 `/stop`。
4. 【私聊】各個玩家到私人聊天室確認身分。
5. 【私聊】天黑後，玩家依各自身分在聊天室中點選按鍵已執行所需要動作(殺人、預言、投毒等)。
6. 【遊戲群】天亮後，由一位玩家輸入`/poll`發起投票，得票數多的玩家被淘汰。
7. 依 1. ~ 6. 的步驟循環，直至好人或壞人其中一方獲勝，遊戲結束。
#### 語音辨識播放音樂
1. Terminal 出現`請開始說話:`的文字後。使用者可以對電腦收音裝置說已設定好的「關鍵字」或「一段含有關鍵字的句子」。
2. 電腦會播放出對應音樂、樹莓派會亮起對應的燈光。
3. 若想中斷現在撥放中的音樂及燈光，直接說下一個關鍵字即可。

## Job Assignment（工作分配）
- 柯予亮 : 狼人殺(telegram bot)、焊接
- 王婷誼 : 語音辨識 & 撥放音樂 
- 陳琪樺 : 狼人殺(telegram bot)
- 鄭采禎 : 燈條 & 色彩

## References 文獻資料
### 資料來源
#### telegram bot
- [telegram bot 生成步驟](https://ithelp.ithome.com.tw/articles/10245264)
- [code 範例 --- python](https://www.programcreek.com/python/example/93148/telegram.Update)
- [漢偉撥放音樂](https://github.com/NCNU-OpenSource/MOLi-PA-Bot/blob/master/PABot.py)
- [InlineKeyboardButton 文件](https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardbutton.html)
- [InlineKeyboardButton 按鈕點擊回應](https://hackmd.io/@truckski/HkgaMUc24)
- [set a poll 設投票](https://github.com/python-telegram-bot/python-telegram-bot/blob/ade1529986f5b6d394a65372d6a27045a70725b2/examples/pollbot.py#L134)
#### 燈
- [哼歌也能带气氛的彩灯条](https://www.youtube.com/watch?v=XNWpQZbgFx0)
- [樹莓派LED像素屏 #1 - 介紹與驅動【明富其識】](https://www.youtube.com/watch?v=bAXOTc3Whzo&t=302s)
- [GPIO](https://pinout.xyz/)


## 感謝名單
- 蔣媽：照片拍攝
- 蔡琳瀠：LED燈連接問題 
- 漢偉：燈條焊接、各種問題詢問
- 學而姐姐：關鍵字、有趣靈感來源
- 蓬萊人偶：器材提供
- 嚴彥婷：代買器材

## 實作影片
- [語音辨識和氣氛燈](https://www.youtube.com/watch?v=thVm5X8Rec8)
- [狼人殺bot遊戲過程](https://www.youtube.com/watch?v=GnFAuDYYw5I)
- [狼人殺 Demo](https://youtu.be/sHKFE53tmeg)



