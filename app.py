import os

from config import *
from sql_conn import *
from template_message import *

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *

import random

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# Listen for all Post Requests from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 使用者輸入文字訊息
    message = event.message.text

#   1-1 選擇新北旅遊區域
    if "新北市" == message:         
        line_bot_api.reply_message(event.reply_token, newtaipei())
#   ======================================================================================
#   1-1-1 直接推薦新北市景點
    elif "Newtaipei" == message:
        # 縣市名稱
        region_name =  str('新北市')

        data = recom_city(region_name)[0:int(recom_city(region_name).shape[0]*0.05)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        newtaipei_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "新北市景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))
        
        line_bot_api.reply_message(event.reply_token, newtaipei_choice_buttons_template_message)

#   ======================================================================================
#   1-2 選擇新北市 --五股、泰山、新莊、蘆洲、三重區
    elif "五股、泰山、新莊、蘆洲、三重" == message:
        line_bot_api.reply_message(event.reply_token, Nsblue())

#   1-2-1 直接推薦新北市 五股、泰山、新莊、蘆洲、三重區景點
    elif "五股、泰山、新莊、蘆洲、三重區" == message:
        region_name = str('五股 泰山 新莊 蘆洲 三重區')
        town_name1 = str('五股區')
        town_name2 = str('泰山區')
        town_name3 = str('新莊區')
        town_name4 = str('蘆洲區')
        town_name5 = str('三重區')

        data = recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5)[0:int(recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        Nsblue5_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "五股 泰山 新莊 蘆洲 三重區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, Nsblue5_choice_buttons_template_message)

#   ======================================================================================
#   1-3 選擇新北市 --石門、三芝、淡水、八里、林口區  
    elif "石門、三芝、淡水、八里、林口" == message:
        line_bot_api.reply_message(event.reply_token,  Npink())

#   1-3-1 直接推薦新北市 石門、三芝、淡水、八里、林口區景點
    elif "石門、三芝、淡水、八里、林口區" == message:
        region_name = str('石門 三芝 淡水 八里 林口區')
        town_name1 = str('石門區')
        town_name2 = str('三芝區')
        town_name3 = str('淡水區')
        town_name4 = str('八里區')
        town_name5 = str('林口區')

        data = recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5)[0:int(recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        Npink5_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "石門 三芝 淡水 八里 林口區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, Npink5_choice_buttons_template_message)

#   ======================================================================================
#   1-4 選擇新北市 --汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區
    elif "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮" == message:
        line_bot_api.reply_message(event.reply_token, Nblue())

#   1-4-1 直接推薦汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區
    elif "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區" == message:
        region_name = str('汐止 金山 萬里 瑞芳 平溪 雙溪 貢寮區')
        
        random.shuffle(recom_b6town())
        result = recom_b6town()[0:6]      

        Nblue6_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "汐止 金山 萬里 瑞芳 平溪 雙溪 貢寮區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))
        
        line_bot_api.reply_message(event.reply_token, Nblue6_choice_buttons_template_message)

#   ======================================================================================
#   1-5 選擇新北市 --板橋、永和、中和區
    elif "板橋、永和、中和" == message:
        line_bot_api.reply_message(event.reply_token, Nyellow())

#   1-5-1 直接推薦板橋、永和、中和區景點
    elif "板橋、永和、中和區" == message:
        region_name = str('板橋、永和、中和區')
        town_name1 = str('板橋區')
        town_name2 = str('永和區')
        town_name3 = str('中和區')

        data = recom_b3town( town_name1, town_name2, town_name3)[0:int(recom_b3town( town_name1, town_name2, town_name3).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6] 
 

        Nyellow3_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "板橋、永和、中和區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, Nyellow3_choice_buttons_template_message)

#   ======================================================================================
#   1-6 選擇新北市 --深坑、三峽、石碇、烏來、坪林
    elif "深坑、三峽、石碇、烏來、坪林" == message:
        line_bot_api.reply_message(event.reply_token, Norange())

#   1-6-1 直接推薦新北市 深坑、三峽、石碇、烏來、坪林區景點
    elif "深坑、新店、石碇、烏來、坪林區" == message:
        region_name = str('深坑 新店 石碇 烏來 坪林區')
        town_name1 = str('深坑區')
        town_name2 = str('新店區')
        town_name3 = str('石碇區')
        town_name4 = str('烏來區')
        town_name5 = str('坪林區')

        data = recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5)[0:int(recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        Norange5_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "深坑 三峽 石碇 烏來 坪林區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, Norange5_choice_buttons_template_message)

#   ======================================================================================
#   1-7 選擇新北市 --Ngreen 鶯歌、三峽、土城、樹林
    elif "鶯歌、三峽、土城、樹林" == message:
        line_bot_api.reply_message(event.reply_token, Ngreen())

#   1-7-1 直接推薦新北市 鶯歌、三峽、土城、樹林區景點
    elif "鶯歌、三峽、土城、樹林區" == message:
        region_name = str('鶯歌 三峽 土城 樹林區')
        town_name1 = str('鶯歌區')
        town_name2 = str('三峽區')
        town_name3 = str('土城區')
        town_name4 = str('樹林區')

        data = recom_b4town( town_name1, town_name2, town_name3, town_name4)[0:int(recom_b4town( town_name1, town_name2, town_name3, town_name4).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        Ngreen4_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "鶯歌 三峽 土城 樹林區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, Ngreen4_choice_buttons_template_message)


#   ======================================================================================
#   2-1 選擇臺北旅遊區域
    elif "臺北市" == message:               
        line_bot_api.reply_message(event.reply_token, taipei())

#   2-1-1 直接推薦臺北市景點
    elif "taipei" == message:
        # 縣市名稱
        region_name =  str('臺北市')

        data = recom_city(region_name)[0:int(recom_city(region_name).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        newtaipei_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "選擇臺北市景點",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))
        
        line_bot_api.reply_message(event.reply_token, newtaipei_choice_buttons_template_message)

#   ======================================================================================
#   2-2-1 選擇臺北市 --中山、松山區
    elif "中山、松山" == message:
        line_bot_api.reply_message(event.reply_token, green())

    elif "中山、松山區" == message:
        region_name = str('中山、松山區')
        town_name1 = str('中山區')
        town_name2 = str('松山區')

        data = recom_b2town( town_name1, town_name2)[0:int(recom_b2town( town_name1, town_name2).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        green2_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "中山、松山區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))
    
        line_bot_api.reply_message(event.reply_token, green2_choice_buttons_template_message)

#   ======================================================================================
#   2-2-2 選擇臺北市 --中正、萬華區
    elif "中正、萬華" == message:
        line_bot_api.reply_message(event.reply_token, pink())

    elif "中正、萬華區" == message:
        region_name = str('中正、萬華區')
        town_name1 = str('中正區')
        town_name2 = str('萬華區')

        data = recom_b2town( town_name1, town_name2)[0:int(recom_b2town( town_name1, town_name2).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        pink2_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "中正、萬華區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, pink2_choice_buttons_template_message)

#   ======================================================================================
#   2-2-3 選擇臺北市 --港湖區
    elif "港湖" == message:
        line_bot_api.reply_message(event.reply_token, sblue())
 
    elif "港湖區" == message:
        region_name = str('港湖區')
        town_name1 = str('南港區')
        town_name2 = str('內湖區')

        data = recom_b2town( town_name1, town_name2)[0:int(recom_b2town( town_name1, town_name2).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        sblue_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "港湖區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, sblue_choice_buttons_template_message)

#   ======================================================================================
#   2-2-4 選擇臺北市 --士林、大同區
    elif "士林、大同" == message:
        line_bot_api.reply_message(event.reply_token, orange())

    elif "士林、大同區" == message:
        region_name = str('士林、大同區')
        town_name1 = str('士林區')
        town_name2 = str('大同區')

        data = recom_b2town( town_name1, town_name2)[0:int(recom_b2town( town_name1, town_name2).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        orange2_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "士林、大同區景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, orange2_choice_buttons_template_message)

#   ======================================================================================
#   2-2-5 選擇臺北市 --大安、信義
    elif "大安、信義" == message:
        line_bot_api.reply_message(event.reply_token, purple())

    elif "大安、信義區" == message:
        region_name = str('大安、信義區')
        town_name1 = str('大安區')
        town_name2 = str('信義區')

        data = recom_b2town( town_name1, town_name2)[0:int(recom_b2town( town_name1, town_name2).shape[0]/2)]
        data = data.drop_duplicates(subset=['tourist_name'])
        p = data['tourist_name'].tolist()
        random.shuffle(p)
        result = p[0:6]      

        purple2_choice_buttons_template_message = TemplateSendMessage(
            alt_text = "大安、信義景點推薦",
            template=CarouselTemplate( 
                columns=[
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                        MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                        MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')]),
                    CarouselColumn( 
                    title = f'{region_name}', 
                    text ="請選擇景點", 
                    actions =[
                        MessageAction(label= f'{result[3]}',text= f'{recom_id(result[3])}'),
                        MessageAction(label= f'{result[4]}',text= f'{recom_id(result[4])}'),
                        MessageAction(label= f'{result[5]}',text= f'{recom_id(result[5])}')])
                        ]))

        line_bot_api.reply_message(event.reply_token, purple2_choice_buttons_template_message)

#   ======================================================================================
#   單一地區推薦
    elif "區" in message:
        # 區名
        town_name =  event.message.text.replace(" ", "")

        if recom_town(town_name).shape[0] >= 5:
            data = recom_town(town_name)[0:int(recom_town(town_name).shape[0]/2)]
            data = data.drop_duplicates(subset=['tourist_name'])
            p = data['tourist_name'].tolist()
            random.shuffle(p)
            result = p[0:5]
                
        elif recom_town(town_name).shape[0] < 5:
            data = recom_town(town_name).drop_duplicates(subset=['tourist_name'])
            p = data['tourist_name'].tolist()
            random.shuffle(p)
            result = p[0:int(data.shape[0])]
 
        choice_buttons_template_message = TemplateSendMessage(
            alt_text = "區域景點推薦",
            template=CarouselTemplate( 
                columns=[
                            CarouselColumn( 
                                title = f'{town_name}', 
                                text ="請選擇景點", 
                                actions =[
                                    MessageAction(label= f'{result[0]}',text= f'{recom_id(result[0])}'),
                                    MessageAction(label= f'{result[1]}',text= f'{recom_id(result[1])}'),
                                    MessageAction(label= f'{result[2]}',text= f'{recom_id(result[2])}')
                                    ])]))
        
        line_bot_api.reply_message(event.reply_token, choice_buttons_template_message)

#   ======================================================================================
#   chatbot 回傳景點名稱、gmap url、文字雲
    elif event.message.text:
        result_list = [] # 文字 + 圖片回傳
        tourist_id =  event.message.text.replace(" ", "")

        recom_text =  recom_result(tourist_id)
        recom_wc =  recom_pic(tourist_id)
        message = ImageSendMessage(
                original_content_url=recom_wc, preview_image_url=recom_wc)
        
        result_list.append(TextSendMessage(text=recom_text))
        result_list.append(message)
        
        line_bot_api.reply_message(event.reply_token, result_list)

    else:
        line_bot_api.reply_message(event.reply_token, message)
        

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)