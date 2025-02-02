# ar_car
ARを見つけ自動でそれに向かうプログラムです
# 仕組み
car.pyが中心です。→car.pyで実行できます
car→detect.pyを呼び出し、検出→carがgpiopinに命令
これの繰り返しです
# 仕様モジュール
(必要に応じて --break-system-packages などのオプションをつけてください)
picamera2
```
pip3 install picamera2
```
numpy
```
pip3 install numpy
```
open-cv系
import cv2
from cv2 import aruco
```
pip install opencv-python
```
RPi.GPIOです
# 動作環境
・RPi5 2GB
・Python3（おそらくどれでも）
# テスト用
app.pyでwebでのカメラ動作確認ができます。
localhost:5000にポート開放されます
flaskが必要です
# 詳細
Qiita

https://qiita.com/raspico/items/50ba9787cbc863f6d63b
