from picamera2 import Picamera2
from time import sleep
from flask import Flask, send_file
import threading

app = Flask(__name__)
picam2 = Picamera2()

def capture_image():
    while True:
        picam2.capture_file('/home/raspi5/image.jpg')
        sleep(1)  # 2秒ごとに撮影

@app.route('/image')
def image():
    return send_file('/home/raspi5/image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    threading.Thread(target=capture_image).start()
    app.run(host='0.0.0.0', port=5000)
