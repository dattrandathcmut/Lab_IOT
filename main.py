import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *


AIO_FEED_ID = ["nutnhan" , "nutnhan2"] # Feed ID
AIO_USERNAME = "emcutene"
AIO_KEY = "aio_eeDD07wO3q3JcK2Lnfel0vmzhRVI"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " tu " + feed_id)
    if feed_id == "nutnhan":
        print("Xu ly nut nhan 1")
        if payload == "1":
            print("Bat den")
            writeSerial("1")
        elif payload == "0":
            print("Tat den")
            writeSerial("0")
    elif feed_id == "nutnhan2":
        print("Xu ly nut nhan 2")
        if payload == "1":
            print("Bat may bom")
            writeSerial("3")
        elif payload == "0":
            print("Tat may bom") 
            writeSerial('4')

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensorcounter = 0
counter_ai = 5
while True:
    # counter = counter - 1
    # if counter <=0:
    #     counter = 10
    #     print("Publish du lieu ...")
    #     if sensorcounter == 0:
    #         sensorcounter = 1
    #         print("Publish du lieu nhiet do...")
    #         temp = random.randint(20 , 40)
    #         client.publish("cambien" , temp)
    #     elif sensorcounter == 1:
    #         sensorcounter = 2
    #         print("Publish du lieu do am...")
    #         humidity = random.randint(50 , 100)
    #         client.publish("cambien2" , humidity)
    #     elif sensorcounter == 2:
    #         sensorcounter = 0
    #         print("Publish du lieu do sang...")
    #         light = random.randint(0 , 100)
    #         client.publish("cambien3" , light)       

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detection()
        print("AI Output: ",ai_result)
        client.publish("ai" , ai_result[0] + " " + str(ai_result[1]))
    readSerial(client)
    time.sleep(1)
    pass