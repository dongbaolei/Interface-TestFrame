# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 16:15
@Author:dongbaolei
"""
import json
import requests
import Get_Token
import getSubImageDict
import tools_params
from Json_loop import Json_Loop
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')

class saveUpload():
    def save_Upload(self):
        self.appcode_data = tools_params.tools_params().get_SubImageDict()
        data = getSubImageDict.getSubImageDict().get_SubImageDict()
        level4_Name=Json_Loop().get_target_value('level4Name', data, [])
        annex_MaxSize = Json_Loop().get_target_value('annexMaxSize', data, [])
        level4_Code=Json_Loop().get_target_value('level4Code', data, [])
        print(level4_Name[0])
        print(tools_params.tools_params().getCarID)
        self.headers= Get_Token.Get_Token().get_headers()
        self.url = "http://192.168.2.26:8080/lease/image/saveUpload"
        for i in range(0,len(level4_Name)):
            payload = {
                "appCode": self.appcode_data['appCode'],
                "imgKey": "fef25fe1-92e5-4cbc-ada6-414aa7260074",
                "carId": tools_params.tools_params().getCarID,
                "level1Type": "01",
                "imgSeq": annex_MaxSize[i],
                "imgCode": level4_Code[i],
                "level4Name": level4_Name[i]
            }
            print(payload)
            response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
            print(response.json())




if __name__ == '__main__':
    saveUpload().save_Upload()
