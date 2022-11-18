# 雙北旅遊推薦系統
## 一、動機

網路資訊百百種，我們常常到了一個景點，卻不清楚下一站能去哪裡。若爬取部落格的推薦文章，或一則則的 Google map 評論，就貿然前去，容易因資訊不完全而失望，將每則評論讀完卻過於費時，且無法掌握所有評論重點。

使用雙北景點資料庫，爬取 Google map 評論，判斷景點的正負向評論，透過 `jieba` 中文斷詞，使用 `wordcloud` 生成文字雲圖片，能夠讓使用者在眾多評論內快速找出有用資訊。
</br></br>

### 使用的程式語言、工具
- Python 3.7.9 , Flask ( 架設與 LINE Message API 的網站 )
- LINE Message API
- Paas : 雲端主機，部署機器人用 ( Adaptable.io )
- MySQL：雲端資料庫 ( Heroku --ClearDB MySQL )

## 二、 流程
## 1. 取得資料
>使用雙北景點資料庫，爬取每個景點分類為最新，前 1700 筆評論不為空的 Google map 評論，在爬蟲時同時處理文字與表情符號，寫入 MySQL。    
>[爬取 Google map 評論程式碼連結](https://colab.research.google.com/drive/15nG7SovZizJstNjHAIyxPERWrnSPVH6w?usp=share_link)

## 2. NLP
1. 使用 jieba 中文斷詞，使用 `wordcloud` 生成文字雲圖片
2. 使用正負向字典，判斷景點的正負向評論，與評論星等加權後的分數排序，推薦給使用者。

## 3. LINEBOT
使用者選擇地理位置，chatbot 會推薦該區域 3 - 6 個正負向分數與評論星等加權後的景點，選擇景點後，即可得景點連結與文字雲，找出每個景點的關鍵字。
</br></br>
### 主程式說明
使用 flask架設與 LINE Message API 的網站， chatbot 回覆與資料庫連線，都是在這處理。
```!
│  app.py  
│  config.py
│  Procfile
│  requirements.txt
│  sql_conn.py
└─ template_message.py
```
1. `app.py` 用 flask 架設與 LINE Message API 連線的網站，與設定 chatbot 功能
2. `config.py` 放入與 LINE BOT 連線的 `Chennel access token` 與 `Channel secret`
3. `Procfile`  在 Adaptable 雲端部署平台起動網站(`app.py`)的指令
4. `sql_conn.py` 與 MySQL 連線，取回傳給使用者的景點資訊

    1.景點名稱
    
    2.文字雲圖片連結
    
    3.gmap 連結
5. `template_message.py` chatbot 的回覆模板

### 流程
使用者輸入訊息，觸發 callback 函數，透過webhook URL 連線雲端伺服器，將訊息回傳給使用者。

<img src="https://i.imgur.com/NWX7RMx.png" width = "487" height = "200" alt="webhook 說明" align=center />


1. 創立 LINE 官方帳號
2. 在 `app.py` 內，定義一個 callback 的函數，當使用者發送訊息時，此函數會被呼叫使用，要觸發函數，需使用 webhook URL (HTTPS 的網域)
3. 將主程式上傳 GitHub，與 Paas 連動並部署啟用 web(`app.py`)產生 webhook URL，讓 LINE BOT 一收到使用者訊息，就能透過 webhook URL 連線至主程式。

### 使用者介面
**三種選擇方式**

* 直接選擇縣市推薦 – ex: 選擇臺北市
* 選擇區域推薦 – ex: 選擇士林、大同區
* 選擇區推薦 – ex: 選擇士林區

<br/>

### 使用者操作流程 --以士林區為例
選擇臺北市>> 士林、大同區 >> 士林區

從推薦的 3 個景點內選擇 --林語堂故居

**取得林語堂故居**
1. 景點連結
2. Google map 評論的文字雲

![](https://i.imgur.com/YQwTRZM.gif)










