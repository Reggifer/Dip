# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:35:36 2023

@author: user
"""

import sqlite3
con = sqlite3.connect("sensor.db")
cur = con.cursor()

cur.execute("""create table if not exists `sensor` ( 
  date_created datetime default current_timestamp, 
  temperature float,
  humidity float)""")

temperature = 24
humidity = 82
cur.execute("insert into sensor (temperature, humidity) values (%d, %d)" % (temperature, humidity))
con.commit()

from datetime import datetime

date_from = datetime.fromisoformat('2023-05-26 08:18:30')
date_to = datetime.fromisoformat('2023-05-26 08:20:00')

res = cur.execute("select * from sensor where date_created > '%s' and date_created < '%s'"% (date_from, date_to))
res.fetchall()

con.close()