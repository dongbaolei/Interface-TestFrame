# -*- coding:utf-8 -*-
"""
@Time:2018-04-02 18:40
@Author:dongbaolei
"""
import json
import unittest

import requests


class PushApplyLoan(unittest.TestCase):
    def setUp(self):
        pass

    def test_pushApplyLoan(self):
        url = "http://192.168.2.26:9090/lzfinance/loan/pushApplyLoan"

        payload = {
            "carDto": {
                "carBrand": "C 长安汽车",
                "carColor": "白色",
                "carDisTon": "1.0L",
                "carFirstRigistDate": "2016-08-08",
                "carGearBox": "手动",
                "carIdentify": "LS4AAB2D4FA565546",
                "carMiles": "35556",
                "carSeries": "长安之星Ⅱ",
                "carStyles": "2012款 长安之星2 1.0L 手动 基本型 SC6399D 5座 手动 1.0L 市场价 31900.0",
                "carType": "0",
                "carYear": "2015",
                "engineNo": "F69T055339",
                "estimatePrice": "31900.00",
                "firstLicensePlateDate": "2015-10-08",
                "isOld": "1",
                "priceNew": "31900.00",
                "salePrice": "31900.00"
            },
            "contact1Dto": {
                "contactMobile": "13795363735",
                "contactName": "赵昭鑫",
                "relationship": "兄弟姐妹"
            },
            "contact2Dto": {
                "contactMobile2": "13795363735",
                "contactName2": "张三",
                "relationship2": "朋友"
            },
            "creditDto": {
                "accountFee": "0.00",
                "appTime": "2017-10-31 12:30:30",
                "carLoanAmount": "31900.00",
                "createTime": "2017-10-31 12:10:30",
                "discountFee": "0.00",
                "flowType": "1",
                "gpsRebate": "0.00",
                "initPaymentAmount": "10000.00",
                "initPaymentRate": "0.11",
                "loanAmount": "31900.00",
                "loanPeriods": "12",
                "remark": "1000",
                "repayType": "等额本息",
                "secureFee": "0.00",
                "serFinRebate": "0.00"
            },
            "jobDto": {
                "jobNature": "自雇",
                "nowDuties": "员工",
                "nowIndustry": "金融/经济",
                "nowUnitAddress": "上海浦东南路1118号1901室",
                "nowUnitCity": "021",
                "nowUnitCityName": "上海",
                "nowUnitDistCode": "021",
                "nowUnitKind": "私营企业",
                "nowUnitMobile": "13795363735",
                "nowUnitName": "曌扬汽车服务有限公司",
                "nowUnitNature": "私营企业",
                "nowUnitPostCode": "111111",
                "nowUnitProvince": "21",
                "nowUnitProvinceName": "上海",
                "nowUnitScale": "11~50",
                "nowUnitTel": "89078966",
                "nowUnitTelAreaCode": "021",
                "nowUnitWorkAge": "3",
                "workTime": "2010-09-10"
            },
            "loanDto": {
                "accountType": "0",
                "bankName": "中国银行",
                "bankSubName": "中国银行上海九亭支行",
                "borrCardCity": "021",
                "borrCardCityName": "上海市",
                "borrCardProvince": "21",
                "borrCardProvinceName": "上海",
                "borrCardRealName": "张三",
                "borrCardReserveMobile": "13795363735",
                "borrIdno": "430321199005180563",
                "cardNo": "6225212603655555"
            },
            "personalDto": {
                "applyCity": "021",
                "applyProvince": "21",
                "birth": "1987-10-11",
                "childrenNum": "1",
                "education": "博士",
                "email": "zhaozhaoxin1209@163.com",
                "gender": "M",
                "hasChild": "有",
                "hasMarried": "已婚",
                "homeAddress": "虹梅路269号1102室",
                "homeCity": "021",
                "homeCityName": "上海市",
                "homeProvice": "21",
                "homeProviceName": "上海",
                "houseNum": "1",
                "houseStatus": "2",
                "idno": "430321199005181234",
                "incomeMonth": "50000",
                "incomeOth": "0",
                "incomeYear": "600000",
                "mobile": "13795363735",
                "nowAddress": "虹梅路269号1102室",
                "nowCity": "021",
                "nowCityName": "上海市",
                "nowDistCode": "111111",
                "nowPosition": "工薪",
                "nowPostCode": "432112",
                "nowProviceName": "上海市",
                "nowProvince": "21",
                "proppserName": "张三",
                "residenceNature": "4"
            },
            "repaymentDto": {
                "repAccountType": "1",
                "repBankName": "中国银行",
                "repBankSubName": "中国银行上海九亭支行",
                "repCardCity": "021",
                "repCardNo": "6225212603655555",
                "repCardProvince": "21",
                "repCardRealName": "张三",
                "repCardReserveMobile": "13795363735",
                "repIdno": "430321199005181234"
            },
            "sysBaseInfoDto": {
                "appCode": "L18032111001001001",
                "appType": "PC",
                "deviceId": "127.0.0.1",
                "fundCode": "DIANRONG",
                "hasAgain": "0",
                "source": "ZY",
                "sysBaseRemark": "zydr3ad00342604046c78ee874610da690d9"
            }
        }

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
