#!env python
#coding=utf-8
# 
# Author:       liaoxinxi
# 
# Created Time: Mon 16 Mar 2015 04:35:17 PM GMT-8
# 
# FileName:     test_wvss.py
# 
# Description:  
# 
# ChangeLog:
def get_ws_plgs( parent_id = 0, type_id = 0 ):
    '''
    get count webscan plugin categories
    '''
    #本身有问题
    if not isInteger( parent_id ) or not isInteger( type_id ):
        return []

    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT * from plugin where plugin_id=1000000 and categories[" + str(parent_id) + "]=" + str(type_id))
    # row = cursor.fetchone()
    rows = cursor.fetchall()
    cursor.close()
    return rows

