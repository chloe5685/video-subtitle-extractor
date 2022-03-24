# -*- coding: utf-8 -*-
import cv2

from celery import Celery
from celery import group
from celery import Task
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import celeryconfig
import os
from main import OcrRecogniser
import numpy as np

app = Celery('hello', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.config_from_object(celeryconfig)
sys.argv = [""]
text_recogniser = OcrRecogniser()

@app.task(autoretry_for=(Exception,))
def predict1(frame_output_dir, frame):
    print(frame)
    # 读取视频帧
    img = cv2.imread(os.path.join(frame_output_dir, frame))
    # 获取检测结果
    dt_box, rec_res = text_recogniser.predict(img)
    # print(dt_box, rec_res)
    return dt_box, np.array(rec_res).tolist()


