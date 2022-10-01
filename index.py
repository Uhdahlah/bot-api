# module monitoring
import requests
import json
from pythonping import ping
from time import sleep


true = 1 < 2
while(true):
    p = ping('20.187.144.40')
    print(p.rtt_avg_ms)
    sleep(15)
    if p.rtt_avg_ms > 200:
     stat = requests.get('https://api.mcsrvstat.us/2/20.187.144.40:19132')
     status = json.loads(stat.text)
     if status['online'] == False:
        url = "http://127.0.0.1:8000/send-message?number=085749435535&message=*==SERVER ALERT==*\n *IP :* play.7togkmc.my.id\n *PORT :* 19132\n *SOFTWARE :* Pocketmine-MP\n *STATUS :* *IS DOWN*\n"
        #url += " *VERSION* : no trace\n *reason* :", status["error"]["query"] ,"\n\n *please contact your provider*"
        payload={}
        files=[]
        headers = {}
        #response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(status['online'], " problem")
        sleep(86400)

     elif status['online'] == True:
        url = "http://127.0.0.1:8000/send-message?number=085749435535&message=*==SERVER MONITORING==*\n *IP :* ", status['ip'] ,"\n *PORT :* ", status['port'] ,"\n *SOFTWARE :* ", status['software'] ,"\n *STATUS :* *ONLINE*\n"
        url += " *VERSION* : ", status['version'] ,"\n\n *Anda akan menerima pesan ini setiap 1 jam*"
        payload={}
        files=[]
        headers = {}
        #response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(status['online'], " no problem")
        sleep(3600)


