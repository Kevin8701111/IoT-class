# IoT-class
# Arduino Nano & Raspi4 教學

- 課程目的
- MCU基本介紹
- Sensor介紹

## 課程目的

藉由這堂課讓大家了解 Sensor 與 MCU 之間如何交流 , 並教導如何去了解Sensor整個工作原理 , 並使用熟悉的程式語言做到資料處理及通訊

## MCU基本介紹
Arduino Nano , 比起Uno板 體積小 , 比起Pro mini 提供的電源較方便 , 且內建TTL晶片燒入
- 為何選Nano http://web.unumobile.com/unu/?p=77
- Pro mini燒入方式 http://mix-cat.blogspot.com/2016/02/arduino-mini-pro-tx-rx-5vgnd-reset.html
- Nano 的腳位介紹

## Sensor介紹
![](https://i.imgur.com/3Fcj43p.png)

- DHT22 AM2302 電容式溫濕度感測 由 熱敏電阻和濕度感測器 組成
- 熱敏電阻 由於溫度變化而變化, NTC 為負溫度係數
- 濕度感測器 由2個電極中間帶著濕度介質 當空氣中濕度變化 就會改變存電量 影響電阻的大小 (導電率) 
![](https://i.imgur.com/3BgPTeY.jpg)



## linux環境部屬 & 權限問題
1 .Arduino IDE https://www.arduino.cc/en/Main/Donate
1.2 .安裝教學 https://www.arduino.cc/en/Guide/Linux
2 .Raspi4 2G 
- 開機後 請切出terminal (ctrl + alt + T)
- 設定Taipei , chinese , us鍵盤 都打勾
- 設定密碼 請全部使用 iotclass
- sudo apt-get update
- sudo apt-get install ssh 
- sudo service ssh status
- sudo service ssh start

2.1 .Linux Port permission https://arduino.stackexchange.com/questions/21215/first-time-set-up-permission-denied-to-usb-port-ubuntu-14-04

 1 .`ls -l /dev/tty*`
 2 .`sudo usermod -a -G dialout kevin(你自己的username)`
 3 .`sudo chmod a+rw /dev/ttyUSB0`
 4 .`SUBSYSTEMS=="usb-serial", TAG+="uaccess"`
 5 .即可正常燒入
 - 測試 file -> Examples -> 01Basic ->Blink
 - 加入 library DHT22 -> Sketch -> include Library -> Add .ZIP Library -> 選擇你的library.zip檔
 - 自定義tty https://www.twblogs.net/a/5bc10f2f2b717711c92423c3

## 實做Arduino sensor AM2302 DHT22
 - 使用 剛剛匯入的 arduino-DHT-master 範例
 - 並完成溫濕度感測電路 ![](https://i.imgur.com/TGW4rNE.jpg)

 - 將資料改成json格式
 - json 格式檢查 http://json.parser.online.fr/
 - 使用 \跳多字元 完成下面的格式
 - {"Humidity":65,"temperature":21}
 
## MQTT 安裝
 - sudo apt-get install mosquitto
 - sudo apt-get install mosquitto-clients
 - service mosquitto status
 - mosquitto_sub -t KK
 - mosquitto_pub -t KK -m "KK"

## MQTT DATA get
 - 直接找python mqtt 範例code 複製貼上 https://pypi.org/project/paho-mqtt/
 - 留下 on_connect , on_message 2個funtion
 - 加上client.loop_forever()讓程式永遠執行
 - 測試後可以知道 port的權限需要設定
 - sudo usermod -aG dialout username
