import cv2
import io
import requests
import json
import numpy as np

# https://github.com/alisen39/TrWebOCR/wiki/%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3
class OcrRecogniser:
    # def __init__(self):
    #     pass

    def predict(self, image, sub_area):
        self.height, self.width = image.shape[0:2]
        font_size = int(min(self.height, self.width) / 5)
        sub_area = np.array(sub_area)
        sub_area_fix = sub_area + (-font_size, +font_size, -font_size, +font_size)
        f_ymin, f_ymax, f_xmin, f_xmax = sub_area_fix
        f_ymin = max(f_ymin, 0)
        f_xmin = max(f_xmin, 0)
        f_ymax = min(f_ymax, self.height)
        f_xmax = min(f_xmax, self.width)
        is_success, buffer = cv2.imencode(".jpg", image[f_ymin:f_ymax, f_xmin:f_xmax])
        url = 'http://127.0.0.1:18089/api/tr-run/'
        res = requests.post(url=url, data={'compress': 0, 'is_draw': 0}, files={'file': io.BytesIO(buffer)})
        # result = res.content.decode('unicode-escape')
        # print(result)
        res = json.loads(res.text)
        # print(res['data']['raw_out'])
        rec_res = list()
        dt_box = list()
        for it in res['data']['raw_out']:
            rec_res.append([it[1], it[2]])
            x, y, width, height, angle = it[0]
            x = x + f_xmin
            y = y + f_ymin
            width_half = width / 2
            height_half = height / 2
            xmin = max(int(x - width_half - 0.5), 0)
            ymin = max(int(y - height_half - 0.5), 0)
            xmax = min(int(x + width_half + 0.5), self.width)
            ymax = min(int(y + height_half + 0.5), self.height)
            dt_box.append((xmin, xmax, ymin, ymax))
        return dt_box, rec_res

    def get_coordinates(self, dt_box):
        return dt_box