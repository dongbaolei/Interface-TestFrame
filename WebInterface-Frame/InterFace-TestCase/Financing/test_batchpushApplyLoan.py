# -*- coding:utf-8 -*-
"""
@Time:2018-04-02 18:40
@Author:dongbaolei
"""
import json
import unittest

import requests


class BatchPushApplyLoan(unittest.TestCase):
    def setUp(self):
        pass

    def test_batchpushApplyLoan(self):
        url = "http://192.168.2.26:9090/lzfinance/loan/batchPushApplyLoan"

        payload = "[{\r\n\t\"carDto\": {\r\n\t\t\"carBrand\": \"C 长安汽车\",\r\n\t\t\"carColor\": \"白色\",\r\n\t\t\"carDisTon\": \"1.0L\",\r\n\t\t\"carFirstRigistDate\": \"2016-08-08\",\r\n\t\t\"carGearBox\": \"手动\",\r\n\t\t\"carIdentify\": \"LS4AAB2D4FA565546\",\r\n\t\t\"carMiles\": \"35556\",\r\n\t\t\"carSeries\": \"长安之星Ⅱ\",\r\n\t\t\"carStyles\": \"2012款 长安之星2 1.0L 手动 基本型 SC6399D 5座 手动 1.0L 市场价 31900.0\",\r\n\t\t\"carType\": \"0\",\r\n\t\t\"carYear\": \"2015\",\r\n\t\t\"engineNo\": \"F69T055339\",\r\n\t\t\"estimatePrice\": \"31900.00\",\r\n\t\t\"firstLicensePlateDate\": \"2015-10-08\",\r\n\t\t\"isOld\": \"1\",\r\n\t\t\"priceNew\": \"31900.00\",\r\n\t\t\"salePrice\": \"31900.00\"\r\n\t},\r\n\t\"contact1Dto\": {\r\n\t\t\"contactMobile\": \"13795363735\",\r\n\t\t\"contactName\": \"赵昭鑫\",\r\n\t\t\"relationship\": \"兄弟姐妹\"\r\n\t},\r\n\t\"contact2Dto\": {\r\n\t\t\"contactMobile2\": \"13795363735\",\r\n\t\t\"contactName2\": \"张三\",\r\n\t\t\"relationship2\": \"朋友\"\r\n\t},\r\n\t\"creditDto\": {\r\n\t\t\"accountFee\": \"0.00\",\r\n\t\t\"appTime\": \"2017-10-31 12:30:30\",\r\n\t\t\"carLoanAmount\": \"31900.00\",\r\n\t\t\"createTime\": \"2017-10-31 12:10:30\",\r\n\t\t\"discountFee\": \"0.00\",\r\n\t\t\"flowType\": \"1\",\r\n\t\t\"gpsRebate\": \"0.00\",\r\n\t\t\"initPaymentAmount\": \"10000.00\",\r\n\t\t\"initPaymentRate\": \"0.11\",\r\n\t\t\"loanAmount\": \"31900.00\",\r\n\t\t\"loanPeriods\": \"12\",\r\n\t\t\"remark\": \"1000\",\r\n\t\t\"repayType\": \"等额本息\",\r\n\t\t\"secureFee\": \"0.00\",\r\n\t\t\"serFinRebate\": \"0.00\"\r\n\t},\r\n\t\"jobDto\": {\r\n\t\t\"jobNature\": \"自雇\",\r\n\t\t\"nowDuties\": \"员工\",\r\n\t\t\"nowIndustry\": \"金融/经济\",\r\n\t\t\"nowUnitAddress\": \"上海浦东南路1118号1901室\",\r\n\t\t\"nowUnitCity\": \"021\",\r\n\t\t\"nowUnitCityName\": \"上海\",\r\n\t\t\"nowUnitDistCode\": \"021\",\r\n\t\t\"nowUnitKind\": \"私营企业\",\r\n\t\t\"nowUnitMobile\": \"13795363735\",\r\n\t\t\"nowUnitName\": \"曌扬汽车服务有限公司\",\r\n\t\t\"nowUnitNature\": \"私营企业\",\r\n\t\t\"nowUnitPostCode\": \"111111\",\r\n\t\t\"nowUnitProvince\": \"21\",\r\n\t\t\"nowUnitProvinceName\": \"上海\",\r\n\t\t\"nowUnitScale\": \"11~50\",\r\n\t\t\"nowUnitTel\": \"89078966\",\r\n\t\t\"nowUnitTelAreaCode\": \"021\",\r\n\t\t\"nowUnitWorkAge\": \"3\",\r\n\t\t\"workTime\": \"2010-09-10\"\r\n\t},\r\n\t\"loanDto\": {\r\n\t\t\"accountType\": \"0\",\r\n\t\t\"bankName\": \"中国银行\",\r\n\t\t\"bankSubName\": \"中国银行上海九亭支行\",\r\n\t\t\"borrCardCity\": \"021\",\r\n\t\t\"borrCardCityName\": \"上海市\",\r\n\t\t\"borrCardProvince\": \"21\",\r\n\t\t\"borrCardProvinceName\": \"上海\",\r\n\t\t\"borrCardRealName\": \"张三\",\r\n\t\t\"borrCardReserveMobile\": \"13795363735\",\r\n\t\t\"borrIdno\": \"430321199005180563\",\r\n\t\t\"cardNo\": \"6225212603655555\"\r\n\t},\r\n\t\"personalDto\": {\r\n\t\t\"applyCity\": \"021\",\r\n\t\t\"applyProvince\": \"21\",\r\n\t\t\"birth\": \"1987-10-11\",\r\n\t\t\"childrenNum\": \"1\",\r\n\t\t\"education\": \"博士\",\r\n\t\t\"email\": \"zhaozhaoxin1209@163.com\",\r\n\t\t\"gender\": \"M\",\r\n\t\t\"hasChild\": \"有\",\r\n\t\t\"hasMarried\": \"已婚\",\r\n\t\t\"homeAddress\": \"虹梅路269号1102室\",\r\n\t\t\"homeCity\": \"021\",\r\n\t\t\"homeCityName\": \"上海市\",\r\n\t\t\"homeProvice\": \"21\",\r\n\t\t\"homeProviceName\": \"上海\",\r\n\t\t\"houseNum\": \"1\",\r\n\t\t\"houseStatus\": \"2\",\r\n\t\t\"idno\": \"430321199005181234\",\r\n\t\t\"incomeMonth\": \"50000\",\r\n\t\t\"incomeOth\": \"0\",\r\n\t\t\"incomeYear\": \"600000\",\r\n\t\t\"mobile\": \"13795363735\",\r\n\t\t\"nowAddress\": \"虹梅路269号1102室\",\r\n\t\t\"nowCity\": \"021\",\r\n\t\t\"nowCityName\": \"上海市\",\r\n\t\t\"nowDistCode\": \"111111\",\r\n\t\t\"nowPosition\": \"工薪\",\r\n\t\t\"nowPostCode\": \"432112\",\r\n\t\t\"nowProviceName\": \"上海市\",\r\n\t\t\"nowProvince\": \"21\",\r\n\t\t\"proppserName\": \"张三\",\r\n\t\t\"residenceNature\": \"4\"\r\n\t},\r\n\t\"repaymentDto\": {\r\n\t\t\"repAccountType\": \"1\",\r\n\t\t\"repBankName\": \"中国银行\",\r\n\t\t\"repBankSubName\": \"中国银行上海九亭支行\",\r\n\t\t\"repCardCity\": \"021\",\r\n\t\t\"repCardNo\": \"6225212603655555\",\r\n\t\t\"repCardProvince\": \"21\",\r\n\t\t\"repCardRealName\": \"张三\",\r\n\t\t\"repCardReserveMobile\": \"13795363735\",\r\n\t\t\"repIdno\": \"430321199005181234\"\r\n\t},\r\n\t\"sysBaseInfoDto\": {\r\n\t\t\"appCode\": \"L18032111001001001\",\r\n\t\t\"appType\": \"PC\",\r\n\t\t\"deviceId\": \"127.0.0.1\",\r\n\t\t\"fundCode\": \"DIANRONG\",\r\n\t\t\"hasAgain\": \"0\",\r\n\t\t\"source\": \"ZY\",\r\n\t\t\"sysBaseRemark\": \"zydr3ad00342604046c78ee874610da690d12\"\r\n\t}\r\n}]"

        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        print(json.dumps(payload))
        response = requests.request("POST", url, data=payload.encode('utf-8').decode('latin-1'), headers=headers)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
