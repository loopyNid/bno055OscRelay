import time
import board
import busio
import adafruit_bno055
import argparse
import random
from pythonosc import osc_message_builder
from pythonosc import udp_client
time.sleep(1)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

client = udp_client.SimpleUDPClient("10.3.141.100", 57120)

while True:
        accel = sensor.accelerometer
        time.sleep(0.0025)
        magn= sensor.magnetometer
        time.sleep(0.0025)
        gyro = sensor.gyroscope
        time.sleep(0.0025)
        client.send_message("/pi3", accel + magn + gyro) # change pi3 to the desired address/"pi id"
