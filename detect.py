import cv2
from cv2 import aruco
from picamera2 import Picamera2
import math


dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

detector = aruco.ArucoDetector(dictionary, parameters)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (1024, 768)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()


def calculate_center(corner):
    x1, y1 = corner[0]
    x2, y2 = corner[1]
    x3, y3 = corner[2]
    x4, y4 = corner[3]
    center_x = (x1 + x2 + x3 + x4) / 4
    center_y = (y1 + y2 + y3 + y4) / 4
    return (center_x, center_y)

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def calculate_diagonal_length(corner):
    if len(corner) < 4:
        return None  
    point1 = corner[0]
    point2 = corner[2]
    diagonal_length = calculate_distance(point1, point2)
    return diagonal_length

def ar_info():
    frame = picam2.capture_array()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedCandidates = detector.detectMarkers(gray)
    if ids is not None:
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        for i, corner in enumerate(corners):
            center = calculate_center(corner[0])
            xy = ids[i][0]
            diagonal_length = calculate_diagonal_length(corner[0])
            return ids[i][0],center[0],center[1],diagonal_length
