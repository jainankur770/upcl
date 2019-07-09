from flask import Flask,request,redirect,jsonify
import json
import datetime
import pymysql
import requests
import sys
#database connection

connection = pymysql.connect(host="upcl-db.c6l1gncuxvii.us-east-1.rds.amazonaws.com", user="valiance", password="valiance", database="upcl", port =3306)
cursor = connection.cursor()

ank = Flask(__name__)

@ank.route('/',methods = ['GET','POST'])
def index():  
   user = str(request.args.get('query'))
   id = str(request.args.get('tid'))
   print("id is"+id)
   CT = datetime.datetime.now()
   d=str(CT.day)+str(CT.month)+str(CT.year)+str(CT.hour)+str(CT.minute)+str(CT.second)
   print(d)
   sql = "INSERT INTO chat_data (Session_id, Query_Data,Tracking_id) VALUES (%s, %s,%s)"
   val = (d, str(user),id)
   cursor.execute(sql, val)

   connection.commit()
   
   var = user.split()
   var1 = [int(elem) for elem in var if elem.isdigit()]
   print(var1)
   for data in var1:
      if (data>0) and (data<16):
         print(data)
         dl="DELETE FROM `chat_data` WHERE Session_id"+'='+d
         cursor.execute(dl)
         connection.commit()
         sql = "INSERT INTO chat_data (Session_id,Customer_id,Query_Data,Tracking_id) VALUES (%s, %s,%s,%s)"
         val = (d,str(data),str(user),id)
         cursor.execute(sql, val)
         connection.commit()
         retrive = "Select Amount from bill_amount WHERE Customer_id"+ "=" +str(data) +";"
         #executing the queries
         cursor.execute(retrive)
         rows = list(cursor.fetchone())
         print(rows)
         for row in rows:
            row1="Your bill amount is RS."+str(row)+".Please make your payment before due date to avoid any extra charges"
            
            print(row1)#insert row1 into response data
            users=jsonify(row1)
            r='UPDATE chat_data SET Response_Data'+'="'+str(row1)+ '" WHERE Session_id'+ '='+ d+';'
            print(r)
            cursor.execute(r)
            connection.commit()
            users.headers["Access-Control-Allow-Origin"] = '*'
            return (users)


         #commiting the connection then closing it.
         connection.commit()
         connection.close()
      elif (data>999999999):
         q=user
         accessToken = "f79640eac50e45eabe89a8e0c22ef8df"
         headers = {'Content-Type': 'application/json',  
            'Authorization': 'Bearer' + accessToken,
            'dataType': 'json'
           }
         URL = "https://console.dialogflow.com/api-client/demo/embedded/9bdc0ca2-ace4-4e0d-8437-58fcb6ed9186/demoQuery?q="+q+"&sessionId=8dbe3dc0-68f9-87c2-3bcc-c98dac27e42b"
         r = requests.get(url = URL, headers=headers)
         users=r.json()
         result=users.get('result')
         fulfillment=result.get('fulfillment')
         speech = fulfillment.get('speech')
         print(speech)#enter speech into response data
         retrive1 = "Select Data from chat WHERE Chat_id"+ "=" +speech +";"
         print(retrive1)
   #executing the queries
         cursor.execute(retrive1)
         data1 = list(cursor.fetchone())
         print(data1)
         for data2 in data1:
            sp='UPDATE chat_data SET Response_Data'+'="'+str(data2)+ '"WHERE Session_id'+ '='+ d+';'
            cursor.execute(sp)
            connection.commit()
            i = "INSERT INTO callback (Session_id,Mobile_number) VALUES (%s,%s)"
            v = (id,q)
            cursor.execute(i, v)
            connection.commit()
            users=jsonify(data2)
            users.headers["Access-Control-Allow-Origin"]='*'
            return (users)
      elif (data>999) and (data<999999999): 
         s='please enter a valid 10 digit mobile number'
         row2='UPDATE chat_data SET Response_Data'+'="'+str(s)+ '"WHERE Session_id'+ '='+ d+';'
         cursor.execute(row2)
         connection.commit()
         v=jsonify(s)#enter s into response data
         v.headers["Access-Control-Allow-Origin"] = '*'
         return (v)   

      else:   
         s='please enter a valid customer id between 1 to 15'
         row2='UPDATE chat_data SET Response_Data'+'="'+str(s)+ '"WHERE Session_id'+ '='+ d+';'
         cursor.execute(row2)
         connection.commit()
         v=jsonify(s)#enter s into response data
         v.headers["Access-Control-Allow-Origin"] = '*'
         return (v)
         
   q=user
   if (q=="Morning") or (q=="MORNING") or (q=="morning") or (q=="Afternoon") or (q=="AFTERNOON") or (q=="afternoon") or (q=="Evening") or (q=="EVENING") or (q=="evening"):

      p='UPDATE callback SET Preferred_time'+'="'+str(q)+ '"WHERE Session_id'+ '='+str(id)+';'
      print(p)
      cursor.execute(p)
      connection.commit()
      accessToken = "f79640eac50e45eabe89a8e0c22ef8df"
      headers = {'Content-Type': 'application/json',  
        'Authorization': 'Bearer' + accessToken,
        'dataType': 'json'
           }
      URL = "https://console.dialogflow.com/api-client/demo/embedded/9bdc0ca2-ace4-4e0d-8437-58fcb6ed9186/demoQuery?q="+q+"&sessionId=8dbe3dc0-68f9-87c2-3bcc-c98dac27e42b"
      r = requests.get(url = URL, headers=headers)
      users=r.json()
      result=users.get('result')
      fulfillment=result.get('fulfillment')
      speech = fulfillment.get('speech')
      print(speech)#enter speech into response data
      retrive1 = "Select Data from chat WHERE Chat_id"+ "=" +speech +";"
      print(retrive1)
      #executing the queries
      cursor.execute(retrive1)
      data1 = list(cursor.fetchone())
      print(data1)
      for data2 in data1:
         sp='UPDATE chat_data SET Response_Data'+'="'+str(data2)+ '"WHERE Session_id'+ '='+ d+';'
         cursor.execute(sp)
         connection.commit()
         users=jsonify(data2)
         users.headers["Access-Control-Allow-Origin"]='*'
         return (users)
   else:
      accessToken = "f79640eac50e45eabe89a8e0c22ef8df"
      headers = {'Content-Type': 'application/json',  
        'Authorization': 'Bearer' + accessToken,
        'dataType': 'json'
           }
      URL = "https://console.dialogflow.com/api-client/demo/embedded/9bdc0ca2-ace4-4e0d-8437-58fcb6ed9186/demoQuery?q="+q+"&sessionId=8dbe3dc0-68f9-87c2-3bcc-c98dac27e42b"
      r = requests.get(url = URL, headers=headers)
      users=r.json()
      result=users.get('result')
      fulfillment=result.get('fulfillment')
      speech = fulfillment.get('speech')
      print(speech)#enter speech into response data
      retrive1 = "Select Data from chat WHERE Chat_id"+ "=" +speech +";"
      print(retrive1)
      #executing the queries
      cursor.execute(retrive1)
      data1 = list(cursor.fetchone())
      print(data1)
      for data2 in data1:
      
         sp='UPDATE chat_data SET Response_Data'+'="'+str(data2)+ '"WHERE Session_id'+ '='+ d+';'
         cursor.execute(sp)
         connection.commit()
         users=jsonify(data2)
         users.headers["Access-Control-Allow-Origin"]='*'
         return (users)

if __name__ == "__main__":
    ank.run(debug=True)