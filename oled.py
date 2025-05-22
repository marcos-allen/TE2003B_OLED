#Actividad I2C

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height



def imprimeNombres():
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.rectangle((200,200,width,height), outline=300, fill=270)
    
    time.sleep(2)
    draw.text((15, 20), 'Marcos\nTania\nJosé', font=font, fill=270)
    disp.image(image)
    disp.show()
    
def imprimeMensaje():
    mensaje = input("Ingresa un mensaje (no mayor a 50 caracteres):")
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    time.sleep(2)
    draw.text((15, 20), mensaje, font=font, fill=270)
    disp.image(image)
    disp.show()
    
imprimeNombres()
imprimeMensaje()

