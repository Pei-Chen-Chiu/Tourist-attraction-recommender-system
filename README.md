# 雙北旅遊推薦系統
## 動機

網路資訊百百種，我們常常到了一個景點，卻不清楚下一站能去哪裡。若爬取部落格的推薦文章，或一則則的google map評論，就貿然前去，容易因資訊不完全而失望，將每則評論讀完卻過於費時，且無法掌握所有評論重點。

使用雙北景點資料庫，爬取 google map 評論，判斷景點的正負向評論，透過 jieba 中文斷詞生成文字雲圖片，能夠讓使用者在眾多評論內快速找出有用資訊。
</br></br>

## LINE BOT

使用者選擇地理位置，chatbot 會推薦該區域 3 - 6 個景點正負向分數與評論星等加權過後的景點，選擇景點後，將景點地名與文字雲回傳給使用者，幫助使用者找出每個景點的關鍵字。
</br></br>

### 使用到的程式語言、工具
- Python 3.7.9 、Flask(開發框架)
- LINE Message API
- Paas: 雲端主機，部署機器人用 (使用 adaptable.io )
- MySQL：雲端資料庫 (使用 Heroku )

