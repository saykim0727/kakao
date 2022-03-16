from reply import *
import sqlite3
import os


class Cafe:
  def __init__(self):
    db_path = "./database/cafe.db"
    self.db = sqlite3.connect(db_path)
    self.c = self.db.cursor()
    self.c.execute("CREATE TABLE IF NOT EXISTS cafe (region text, title text, desc text, image text, link text)")

  def get_cafes(self):
    t = ""
    self.c.execute("SELECT region FROM cafe")
    data = list(set(self.c.fetchall()))
    for i in data : t = " ".join(i) + ", " + t
    return simpleCard("---cafe list ---\n" + t[:-2])

  def add_cafe(self, t, d, l):
    com = "INSERT INTO cafe VALUES ('%s', '%s', '%s', '%s', '%s')" % (t[2], t[3], d, l[0], l[1])
    self.c.execute(com)
    return simpleCard("카페 목록에 %s %s가 추가되었습니다" % (t[2], t[3]))

  def del_cafe(self, name):
    com = "DELETE FROM cafe WHERE title='%s'" % name
    self.c.execute(com)
    return simpleCard("카페 목록에 %s가 삭제되었습니다" % name)

  def sel_cafe_real(self, r, num):
    com = "SELECT * FROM cafe WHERE region='%s'" % r
    self.c.execute(com)
    data = self.c.fetchall()
    data.reverse()
    data = data[5*num:5*(num+1)]
    return data

  def sel_cafe(self, r): # region select and show cafe list
    r_list = r.split("-")
    data = self.sel_cafe_real(r, 0) if len(r_list)==1 else self.sel_cafe_real(r_list[0], int(r_list[1]))
    num = 0 if len(r_list)==1 else r_list[1]
    title = "카페 %s" % r_list[0]
    return listCard(title, data, "cafe", num)
