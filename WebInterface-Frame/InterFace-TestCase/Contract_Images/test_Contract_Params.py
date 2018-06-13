# -*- coding:utf-8 -*-
"""
@Time:2018-03-22 18:38
@Author:dongbaolei
"""
import random
import string
import unittest

from requests_toolbelt import MultipartEncoder

import ID_Card


class ContractParams():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    salt2 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    salt3 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    salt4 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    salt5 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    salt6 = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
    id_number = ID_Card.gen_id_card(int(area_code), 22, 1)
    randomPhone = ''.join([random.choice(string.digits) for _ in range(11)])
    randomseqNo = ''.join([random.choice(string.digits) for _ in range(12)])
    list = ["139", "188", "185", "136", "152", "158", "177"]
    str = "0123456789"

    def modify_generate_params(self):
        params = {"signIdNo": "371322199012200238", "privateKey": "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE",
                  "seqNo": self.salt, "protocolCode": "L1803271000100102002",
                  "signUserName": "下一步保存", "signType": "1", "signMobile": "15201884579",
                  "applyInfoDTO": {
                      "appInfo": {"companyCode": 10002, "comeSource": "1", "dealerName": "厦门动力原汽车服务有限公司代理店",
                                  "dealerCode": 10002005, "createTime": "2018-03-27 07:01:49", "appType": "01",
                                  "companyName": "厦门动力原汽车服务有限公司", "updateTime": "2018-03-27 15:01:49",
                                  "appCode": "L1803271000100102002", "userName": "销售测试用户", "userId": "1000100102",
                                  "status": "11200"}, "consumerInfos": [
                          {"consumerType": "01", "idType": "15", "sex": "3", "name": "下一步保存", "mobile": "15201884579",
                           "id": 198644, "appCode": "L1803271000100102002", "idno": "371322199012200238"}]
                      , "loanInfo": {
                          "replyLoanAmount": 50000.0,
                          "replyLoanPeriods": 24
                      }, "carInfo": {
                          "carBrand": "奥迪",
                          "carIdentify": "LGWEFEA53CB001039"
                      }, "bankCardInfo": {
                          "accountBank": "中国银行",
                          "accountNo": "62148508999828822",
                          "accountName": "王五",
                          "accountIdno": "343032319910819931",
                          "mobile": "18266271890"
                      }
                  },
                  "busiSysCode": "loanApply",
                  "contractCodes": ["DR_00001", "DR_00002", "DR_00003", "DR_00004", "DR_00005"]

                  }
        return params

    def modify_upload_params(self):
        params = MultipartEncoder(
            fields={'privateKey': "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE", 'seqNo': self.salt2, 'busiSysCode': 'loanApply',
                    'fileContent': '1111',
                    'file': (open('E:\\test\\11111.jpg', 'rb'), 'image/jpeg')}
        )
        return params

    def modify_geturl_params(self):
        params = {
            "privateKey": "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE",
            "busiSysCode": "loanApply",
            "seqNo": self.salt3,
            "keys": "d44347f2-6d77-41c7-9ae6-b24505a12752"

        }
        return params

    def modify_getThumurl_params(self):
        params = {
            "privateKey": "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE",
            "busiSysCode": "loanApply",
            "seqNo": self.salt4,
            "width": 100,
            "hight": 100,
            "keys": "111"

        }
        return params

    def modify_sign_params(self):
        params = {
            "busiSysCode": "loanApply",
            "privateKey": "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE",
            "seqNo": self.salt5,
            "protocolCode": "L1709011001700101002",
            "signUserName": "张三",
            "signIdNo": "340323199108191313",
            "signMobile": "18255171225",
            "signType": "1",
            "contractInfos": [{
                "contractCode": "DR_00001",
                "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c787",
                "pageNum": 1,
                "signDate": "2018-03-19"
            }, {
                "contractCode": "DR_00001",
                "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c788",
                "pageNum": 2,
                "signDate": "2018-03-19"
            },
                {
                    "contractCode": "DR_00002",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 1,
                    "signDate": "2018-03-19"
                },
                {
                    "contractCode": "DR_00002",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 2,
                    "signDate": "2018-03-19"
                },
                {
                    "contractCode": "DR_00002",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 3,
                    "signDate": "2018-03-19"
                },
                {
                    "contractCode": "DR_00003",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 1,
                    "signDate": "2018-03-19"
                },
                {
                    "contractCode": "DR_00004",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 1,
                    "signDate": "2018-03-19"
                }, {
                    "contractCode": "DR_00005",
                    "key": "83f6861e-05a6-4fc5-b1ce-3892ecd3c789",
                    "pageNum": 1,
                    "signDate": "2018-03-19"
                }],
            "appInfo": {
                "appCode": "L1709011001700101002"
            },
            "consumerInfos": [{
                "consumerType": "2",
                "name": "李四",
                "idno": "340323199108191314"
            }],
            "applyInfoDTO": {
                "appInfo": {"companyCode": 10002, "comeSource": "1", "dealerName": "厦门动力原汽车服务有限公司代理店",
                            "dealerCode": 10002005, "createTime": "2018-03-27 07:01:49", "appType": "01",
                            "companyName": "厦门动力原汽车服务有限公司", "updateTime": "2018-03-27 15:01:49",
                            "appCode": "L1803271000100102002", "userName": "销售测试用户", "userId": "1000100102",
                            "status": "11200"}, "consumerInfos": [
                    {"consumerType": "01", "idType": "15", "sex": "3", "name": "下一步保存", "mobile": "15201884579",
                     "id": 198644, "appCode": "L1803271000100102002", "idno": "371322199012200238"}]
                , "loanInfo": {
                    "replyLoanAmount": 50000.0,
                    "replyLoanPeriods": 24
                }, "carInfo": {
                    "carBrand": "奥迪",
                    "carIdentify": "LGWEFEA53CB001039"
                }, "bankCardInfo": {
                    "accountBank": "中国银行",
                    "accountNo": "62148508999828822",
                    "accountName": "王五",
                    "accountIdno": "343032319910819931",
                    "mobile": "18266271890"
                }
            }
        }
        return params

    def modify_anxinq_registerparams(self):
        params = {
            "busiSysCode": "loanApply",
            "privateKey": "17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE",
            "seqNo": self.salt6,
            "userName": "张三",
            "idNo": self.id_number,
            "mobile": self.randomPhone,
            "protocolCode": "F123232123422112",
            "userType": "01",
            "ip": "192.168.2.116"
        }
        return params


if __name__ == '__main__':
    unittest.main
