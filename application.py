from flask import Flask, request, jsonify
import json
import requests
import sys
from reply import *
from cafe import *
from food import *
import sqlite3
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "saykim's Web Server"

def usage():
  return simpleCard("맛집 추가 region name desc imageUrl url")

@application.route("/food", methods=['POST'])
def food_main():
    data = basicCard()
    req= request.get_json()
    text = req['userRequest']['utterance'].strip()
    text = text.split(" ")
    
    food = Food()    
    if len(text) == 1:
      data = food.get_foods()
    elif len(text) == 2: 
      if "맛집" == text[1]: data = food.sel_food(text[0])
      else : data = food.sel_food(text[1])
    elif text[1] == "추가":
      t = text
      text = " ".join(text)
      desc = " ".join(text.split("http")[0].split(" ")[4:]).strip()
      l = text.split(desc)[1].strip().split(" ")
      data = food.add_food(t, desc, l)
    elif text[1] == "제거" or text[1]=='삭제':
      data = food.del_food(text[2])
    else:
      data = simpleCard("없는 cafe 명령어 입니다")

    food.db.commit()
    food.c.close()
    food.db.close()
    return jsonify(data.res)

@application.route("/cafe", methods=['POST'])
def cafe_main():
    data = basicCard()
    req= request.get_json()
    text = req['userRequest']['utterance'].strip()
    text = text.split(" ")
    
    cafe = Cafe()    
    if len(text) == 1:
      data = cafe.get_cafes()
    elif len(text) == 2: #TODO
      if "카페" == text[1]: data = cafe.sel_cafe(text[0])
      else : data = cafe.sel_cafe(text[1])
    elif text[1] == "추가":
      t = text
      text = " ".join(text)
      desc = " ".join(text.split("http")[0].split(" ")[4:]).strip()
      l = text.split(desc)[1].strip().split(" ")
      data = cafe.add_cafe(t, desc, l)
    elif text[1] == "제거" or text[1] =="삭제":
      data = cafe.del_cafe(text[2])
    else:
      data = simpleCard("없는 cafe 명령어 입니다")

    cafe.db.commit()
    cafe.c.close()
    cafe.db.close()
    return jsonify(data.res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5555,threaded=True)
