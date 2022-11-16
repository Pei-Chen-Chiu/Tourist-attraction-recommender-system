from linebot.models import *

#   1-1 選擇新北旅遊區域
def newtaipei():

    newtaipei_list = []
    text = TextSendMessage("請選擇旅遊區域")
    image_carousel_template_message = TemplateSendMessage(
        alt_text='選擇新北旅遊區域',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/0MYdht4.jpg',
                    action= MessageAction(
                        label="請直接推薦我新北市景點", text="Newtaipei")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/hkEMReL.jpg',
                    action= MessageAction(
                        label="選擇此區", text="五股、泰山、新莊、蘆洲、三重")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/pUzn8Op.jpg',
                    action= MessageAction(
                        label= "選擇此區", text= "石門、三芝、淡水、八里、林口")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/k5JdoAw.jpg',
                    action= MessageAction(
                        label= "選擇此區", text= "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮"))]))
    
    image_carousel_template_message2 = TemplateSendMessage(
        alt_text='選擇新北旅遊區域',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/kh4euBi.jpg',
                    action= MessageAction(
                        label="選擇此區", text="板橋、永和、中和")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/17c0gjw.jpg',
                    action= MessageAction(
                        label= "選擇此區", text= "深坑、三峽、石碇、烏來、坪林")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/amWKZU0.jpg',
                    action= MessageAction(
                        label= "選擇此區", text= "鶯歌、三峽、土城、樹林"))]))
    newtaipei_list.append(text)
    newtaipei_list.append(image_carousel_template_message)
    newtaipei_list.append(image_carousel_template_message2) 
    return  newtaipei_list

#   1-2 選擇新北市 --Nsblue 五股、泰山、新莊、蘆洲、三重區
def Nsblue():

    Nsblue_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇五股、泰山、新莊、蘆洲、三重區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/hkEMReL.jpg",
                            title = "五股、泰山、新莊、蘆洲、三重區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "五股、泰山、新莊、蘆洲、三重區"),
                                MessageAction(label= "五股區",text= "五股區"),
                                MessageAction(label= "泰山區",text= "泰山區")
                                ]),
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/hkEMReL.jpg",
                            title = "五股、泰山、新莊、蘆洲、三重區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "新莊區",text= "新莊區"),
                                MessageAction(label= "蘆洲區",text= "蘆洲區"),
                                MessageAction(label= "三重區",text= "三重區")
                                ])]))

    return Nsblue_buttons_template_message

#   1-3 選擇新北市 --Npink 石門、三芝、淡水、八里、林口  
def Npink():

    Npink_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇石門、三芝、淡水、八里、林口區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/pUzn8Op.jpg",
                            title = "石門、三芝、淡水、八里、林口區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "石門、三芝、淡水、八里、林口區"),
                                MessageAction(label= "石門區",text= "石門區"),
                                MessageAction(label= "三芝區",text= "三芝區")

                                ]),
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/pUzn8Op.jpg",
                            title = "石門、三芝、淡水、八里、林口區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "淡水區",text= "淡水區"),
                                MessageAction(label= "八里區",text= "八里區"),
                                MessageAction(label= "林口區",text= "林口區")
                                ])]))
    
    return Npink_buttons_template_message

#   1-4 選擇新北市 --Nblue 汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區
def Nblue():

    Nblue_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/k5JdoAw.jpg",
                            title = "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我此區",text= "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區"),
                                MessageAction(label= "汐止區",text= "汐止區"),
                                MessageAction(label= "金山區",text= "金山區"),
                                ]),
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/k5JdoAw.jpg",
                            title = "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "萬里區",text= "萬里區"),
                                MessageAction(label= "瑞芳區",text= "瑞芳區"),
                                MessageAction(label= "平溪區",text= "平溪區")
                                ]),
                            CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/k5JdoAw.jpg",
                            title = "汐止、金山、萬里、瑞芳、平溪、雙溪、貢寮區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "雙溪區",text= "雙溪區"),
                                MessageAction(label= "貢寮區",text= "貢寮區"),
                                MessageAction(label= " ",text= " ")
                                ])]))
    
    
    return Nblue_buttons_template_message

#   1-5 選擇新北市 --Nyellow 板橋、永和、中和區
def Nyellow():

    Nyellow_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇板橋 永和 中和區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/kh4euBi.jpg",
                            title = "板橋、永和、中和區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "板橋、永和、中和區"),
                                MessageAction(label= "板橋區",text= "板橋區"),
                                MessageAction(label= "永和區",text= "永和區")
                                ]),
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/kh4euBi.jpg",
                            title = "板橋、永和、中和區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "中和區",text= "中和區"),
                                MessageAction(label= " ",text= " "),
                                MessageAction(label= " ",text= " ")
                                ])]))

    return Nyellow_buttons_template_message

#   1-6 選擇新北市 --Norange 深坑、三峽、石碇、烏來、坪林
def Norange():

    Norange_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇深坑、三峽、石碇、烏來、坪林區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/17c0gjw.jpg",
                            title = "深坑、新店、石碇、烏來、坪林區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "深坑、新店、石碇、烏來、坪林區"),                          
                                MessageAction(label= "深坑區",text= "深坑區"),
                                MessageAction(label= "新店區",text= "新店區")
                                ]),
                            CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/17c0gjw.jpg",
                            title = "深坑、新店、石碇、烏來、坪林區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "石碇區",text= "石碇區"),
                                MessageAction(label= "烏來區",text= "烏來區"),
                                MessageAction(label= "坪林區",text= "坪林區")
                                ])]))

    return Norange_buttons_template_message

#   1-7 選擇新北市 --Ngreen 鶯歌、三峽、土城、樹林
def Ngreen():

    Ngreen_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇鶯歌、三峽、土城、樹林區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/amWKZU0.jpg",
                            title = "鶯歌、三峽、土城、樹林區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "鶯歌、三峽、土城、樹林區"),                          
                                MessageAction(label= "鶯歌區",text= "鶯歌區"),
                                MessageAction(label= "三峽區",text= "三峽區")
                                ]),
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/amWKZU0.jpg",
                            title = "鶯歌、三峽、土城、樹林區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "土城區",text= "土城區"),
                                MessageAction(label= "樹林區",text= "樹林區"),
                                MessageAction(label= " ",text= " ")
                                ])]))

    return Ngreen_buttons_template_message

#   ======================================================================================
#   2-2 選擇臺北市旅遊區域
def taipei():

    taipei_list = []
    text = TextSendMessage("請選擇旅遊區域")

    image_carousel_template_message = TemplateSendMessage(
        alt_text='選擇臺北旅遊區域',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/XtMN535.jpg',
                    action= MessageAction(
                        label="請直接推薦我臺北市景點", text="taipei")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/zjVDild.jpg',
                    action= MessageAction(
                        label="選擇中山、松山區", text="中山、松山")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/wd3Leae.jpg',
                    action= MessageAction(
                        label= "選擇中正、萬華區", text= "中正、萬華")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/iUBauEA.jpg',
                    action= MessageAction(
                        label= "選擇內湖、南港區", text= "港湖"))]))
    
    image_carousel_template_message2 = TemplateSendMessage(
        alt_text='選擇臺北旅遊區域',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/3tuaieW.jpg',
                    action= MessageAction(
                        label= "選擇士林、大同區", text= "士林、大同")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/MrGPYoG.jpg',
                    action= MessageAction(
                        label="選擇大安、信義區", text="大安、信義")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/IRvYUEQ.jpg',
                    action= MessageAction(
                        label= "選擇文山區", text= "文山區")),
                ImageCarouselColumn( 
                    image_url='https://i.imgur.com/cVtq4Ep.jpg',
                    action= MessageAction(
                        label= "選擇北投區", text= "北投區"))]))
    taipei_list.append(text)
    taipei_list.append(image_carousel_template_message)
    taipei_list.append(image_carousel_template_message2) 
    return taipei_list


#   2-2-1 選擇臺北市 --green 中山、松山區
def green():

    green_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇中山、松山區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/zjVDild.jpg",
                            title = "中山、松山區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "中山、松山區"),
                                MessageAction(label= "中山區",text= "中山區"),
                                MessageAction(label= "松山區",text= "松山區")
                                ])]))
      
    return green_buttons_template_message

#   2-2-2 選擇臺北市 --pink 中正、萬華區
def pink():

    pink_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇中正、萬華區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/wd3Leae.jpg",
                            title = "中正、萬華區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "中正、萬華區"),
                                MessageAction(label= "中正區",text= "中正區"),
                                MessageAction(label= "萬華區",text= "萬華區")
                                ])]))
    
    return pink_buttons_template_message

#   2-2-3 選擇臺北市 --sblue 港湖區
def sblue ():

    sblue_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇港湖區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/iUBauEA.jpg",
                            title = "港湖區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "港湖區"),
                                MessageAction(label= "內湖區",text= "內湖區"),
                                MessageAction(label= "南港區",text= "南港區"),
                                ])]))
   
    return sblue_buttons_template_message

#   2-2-4 選擇臺北市 --orange 士林、大同區
def orange():

    orange_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇士林、大同區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/3tuaieW.jpg",
                            title = " 士林、大同區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "士林、大同區"),
                                MessageAction(label= "士林區",text= "士林區"),
                                MessageAction(label= "大同區",text= "大同區")
                                ])]))
    
    return orange_buttons_template_message
    
#   2-2-5 選擇臺北市 --purple 大安、信義區
def purple():

    purple_buttons_template_message = TemplateSendMessage(
        alt_text = "選擇大安、信義區",
        template=CarouselTemplate( 
            columns=[
                        CarouselColumn( 
                            thumbnail_image_url = "https://i.imgur.com/MrGPYoG.jpg",
                            title = "大安、信義區", 
                            text ="請選擇旅遊區域", 
                            actions =[
                                MessageAction(label= "請直接推薦我全區",text= "大安、信義區"),
                                MessageAction(label= "大安區",text= "大安區"),
                                MessageAction(label= "信義區",text= "信義區")
                                ])]))
    
    return purple_buttons_template_message




