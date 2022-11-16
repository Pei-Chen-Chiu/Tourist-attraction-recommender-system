# -*- coding:utf-8 -*-
from config import *

import pymysql
import pandas as pd

'''縣市推薦 --取出縣市排序後景點'''
def recom_city(region_name):
    # 縣市名稱
    region_name = str(region_name)  
    
    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE city='{region_name}'"
    data = pd.read_sql(sql, conn)

    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data


'''2大區推薦 --取出區域排序後景點'''
def recom_b2town( town_name1, town_name2):
    # 區域名稱
    town_name1 = str(town_name1)
    town_name2 = str(town_name2)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE `town` in ('{town_name1}','{town_name2}')"
    data = pd.read_sql(sql, conn)

    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data

'''3大區推薦'''
def recom_b3town( town_name1, town_name2, town_name3):

    town_name1 = str(town_name1)
    town_name2 = str(town_name2)
    town_name3 = str(town_name3)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE `town` in ('{town_name1}','{town_name2}','{town_name3}')"
    data = pd.read_sql(sql, conn)

    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data

'''4大區推薦'''
def recom_b4town( town_name1, town_name2, town_name3, town_name4):

    town_name1 = str(town_name1)
    town_name2 = str(town_name2)
    town_name3 = str(town_name3)
    town_name4 = str(town_name4)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE `town` in ('{town_name1}','{town_name2}','{town_name3}','{town_name4}')"
    data = pd.read_sql(sql, conn)
    
    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data

'''5大區推薦'''
def recom_b5town( town_name1, town_name2, town_name3, town_name4, town_name5):

    town_name1 = str(town_name1)
    town_name2 = str(town_name2)
    town_name3 = str(town_name3)
    town_name4 = str(town_name4)
    town_name5 = str(town_name5)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)

    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE `town` in ('{town_name1}','{town_name2}','{town_name3}','{town_name4}','{town_name5}')"
    data = pd.read_sql(sql, conn)
    
    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data

'''6大區推薦''' # LINE API 有回傳時間限制(10秒)，資料若直接在API處理，超過 10 秒 token 會失效
def recom_b6town():

    town_name1 = str('汐止區')
    town_name2 = str('萬里區')
    town_name3 = str('瑞芳區')
    town_name4 = str('平溪區')
    town_name5 = str('雙溪區')
    town_name6 = str('貢寮區')

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE `town` in ('{town_name1}','{town_name2}','{town_name3}','{town_name4}','{town_name5}','{town_name6}')"
    data = pd.read_sql(sql, conn)
    
    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    data = data[0:int(data.shape[0]/2)]
    data = data.drop_duplicates(subset=['tourist_name'])
    p = data['tourist_name'].tolist()

    return p

'''單區域薦  --取出單區排序後景點'''
def recom_town(town_name):
    
    town_name = str(town_name)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset)
    
    sql = f"SELECT tourist_name, result_avg FROM `{db}`.`{table}` WHERE town='{town_name}'"
    data = pd.read_sql(sql, conn)
    
    data['result_avg'] = data['result_avg'].astype(float)
    data = data.sort_values(['result_avg'],ascending=False)

    return data 

'''輸入景點名稱，取出景點id (button action(text))'''
def recom_id(tourist_name):
    # 景點名稱
    tourist_name=str(tourist_name)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset )
     
    try:
        sql = f"SELECT tourist_id FROM `{db}`.`{table}` WHERE tourist_name = '{tourist_name}'"
        data = pd.read_sql(sql, conn)
        tourist_id = data['tourist_id'][0]

    except Exception as e:
        print ("Exception")
        print (e)
        conn.rollback()

    conn.close()

    return(tourist_id)

'''輸入景點id 取出景點名稱、gmap url'''
def recom_result(tourist_id):
    # 景點 id
    tourist_id = str(tourist_id)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset )

    sql = f"SELECT tourist_name, gmap_url FROM `{db}`.`{table}` WHERE tourist_id = {tourist_id}"
    data = pd.read_sql(sql, conn)

    conn.close()

    tourist_name = data['tourist_name'][0]
    gmap_url = data['gmap_url'][0]

    return (f'{tourist_name}\n{gmap_url}')

'''輸入景點id 取出單一景點的文字雲圖片'''
def recom_pic(tourist_id):
    # 景點 id
    tourist_id=str(tourist_id)

    conn = pymysql.connect(
        user=user , 
        port=port,
        passwd=passwd,
        db=db,
        host=host, 
        charset=charset )
     
    try:
        sql = f"SELECT word_cloud FROM `{db}`.`{table}` WHERE tourist_id = '{tourist_id}'"
        data = pd.read_sql(sql, conn)

        word_cloud = data['word_cloud'][0]

    except Exception as e:
        print ("Exception")
        print (e)
        conn.rollback()
    
    conn.close()

    return(f'{word_cloud}')
