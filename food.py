from reply import *
import sqlite3
import os


class Food:
  def __init__(self):
    db_path = "./database/food.db"
    self.db = sqlite3.connect(db_path)
    self.c = self.db.cursor()
    self.c.execute("CREATE TABLE IF NOT EXISTS food (region text, title text, desc text, image text, link text)")

  def get_foods(self):
    t = ""
    self.c.execute("SELECT region FROM food")
    data = list(set(self.c.fetchall()))
    for i in data : t = " ".join(i) + ", " + t
    return simpleCard("---food list ---\n" + t[:-2])

  def add_food(self, t, d, l):
    com = "INSERT INTO food VALUES ('%s', '%s', '%s', '%s', '%s')" % (t[2], t[3], d, l[0], l[1])
    self.c.execute(com)
    return simpleCard("맛집 목록에 %s %s가 추가되었습니다" % (t[2], t[3]))

  def del_food(self, name):
    com = "DELETE FROM food WHERE title='%s'" % name
    self.c.execute(com)
    return simpleCard("맛집 목록에 %s가 삭제되었습니다" % name)

  def sel_food_real(self, r, num):
    com = "SELECT * FROM food WHERE region='%s'" % r
    self.c.execute(com)
    data = self.c.fetchall()
    data.reverse()
    data = data[5*num:5*(num+1)]
    return data

  def sel_food(self, r): # region select and show food list
    r_list = r.split("-")
    data = self.sel_food_real(r, 0) if len(r_list)==1 else self.sel_food_real(r_list[0], int(r_list[1]))
    num = 0 if len(r_list)==1 else r_list[1]
    title = "맛집 %s" % r_list[0]
    return listCard(title, data, "food", num)
