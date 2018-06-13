# -*- coding:utf-8 -*-
"""
@Time:2018-03-06 17:23
@Author:dongbaolei
"""
import json

from requests_toolbelt import MultipartEncoder


class UploadFiles():
    def SingleUpload(self, data, token, filepath):
        # salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        # randomInt = ''.join([random.choice(string.digits) for _ in range(8)])

        # 使用requests_toolbelt中的MultipartEncoder进行form-data大文件数据上传
        # data={'imgType': '1', 'imgTypeName': 'jpg', 'imgCode': randomInt, 'showType': '1',
        #             'hasHome': '0', 'token': token}
        # filepath='E:\\test\\11111.jpg'

        params = MultipartEncoder(
            fields={'params': data, 'token': token, 'file': ('filename', open(filepath, 'rb'), 'image/jpg')}
        )
        return params

    def multiplyUpload(self,data,token,filepaths):
        # datarray = [{"imgType": "0", "imgTypeName": "影像件名称", "imgCode": "10010111"},
        #             {"imgType": "1", "imgTypeName": "影像件名称2", "imgCode": "10010111"}]
        # 因为使用数组，需要转码json
        jsonarray = json.dumps(data)
        params = MultipartEncoder(
            fields={'params': jsonarray, 'token': token,
                    'file': ('filename', open(filepaths[0], 'rb'), 'image/jpg'),
                    'file': ('filename', open(filepaths[1], 'rb'), 'image/jpg')}
        )
        return params