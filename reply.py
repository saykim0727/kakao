d1 = "YJ"
d2 = "Pretty and cute"
d3 = "https://github.com/saykim0727/temp/blob/master/test.jpeg?raw=true"
d4 = "https://github.com/saykim0727/temp/blob/master/test.jpeg?raw=true"
d = ("dummy",d1,d2,d3,d4)

class basicCard:
  res = {}
  def __init__(self):
    self.res = {"version" : "2.0",
                "template" : {"outputs": [{'basicCard': {"title" : "YG",
                                                         "description": "Pretty and cute",
                                                         "thumbnail" : {"imageUrl": "https://github.com/saykim0727/temp/blob/master/test.jpeg?raw=true" },
                                                         "buttons": [
                                                                     {
                                                                        "action": "webLink",
                                                                        "label": "Link",
                                                                        "webLinkUrl": "https://www.naver.com"
                                                                     }
                                                                     ]
                                                                     }}]}} 
                                                                      
                                                                      

  def setTitle(self, title):
    None
  

class simpleCard:
  res = {}
  def __init__(self, text) :
   self.res = {"version" : "2.0", 
               "template" : {
                  "outputs": [
                    { "simpleText": { "text": text } } ] }}


class listCard:
  res = {}
  def __init__(self, title, obj, typ, num):
    for i in range(0,5-len(obj)):
      obj.append(d)
    num = int(num)
    prev_num = 0 if num == 0 else num-1
    next_num = 1 if num == 0 else num+1

    self.res =  {
                  "version": "2.0",
                  "template": {
                    "outputs": [
                      {
                        "listCard": {
                          "header": {
                            "title": title #강남 맛집
                          },
                          "items": [
                            {
                              "title": obj[0][1],
                              "description": obj[0][2],
                              "imageUrl": obj[0][3],
                              "link": {
                                "web": obj[0][4]
                              }
                            },
                            {
                              "title": obj[1][1],
                              "description": obj[1][2],
                              "imageUrl": obj[1][3],
                              "link": {
                                "web": obj[1][4]
                              }
                            },
                            {
                              "title": obj[2][1],
                              "description": obj[2][2],
                              "imageUrl": obj[2][3],
                              "link": {
                                "web": obj[2][4]
                              }
                            },
                            {
                              "title": obj[3][1],
                              "description": obj[3][2],
                              "imageUrl": obj[3][3],
                              "link": {
                                "web": obj[3][4]
                              }
                            },
                            {
                              "title": obj[4][1],
                              "description": obj[4][2],
                              "imageUrl": obj[4][3],
                              "link": {
                                "web": obj[4][4]
                              }
                            }
                          ],
                          "buttons": [
                            {
                              "label": "이전",
                              "action": "message",
                              "messageText" : "%s-%d" % (title, prev_num) 
                            },
                            {
                              "label": "다음",
                              "action": "message",
                              "messageText" : "%s-%d" % (title, next_num) 
                            }
                          ]
                        }
                      }
                    ]
                  }
              }
