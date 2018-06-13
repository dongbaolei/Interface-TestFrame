# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 16:15
@Author:dongbaolei
"""
import getSubImageDict


class Json_Loop():
    def get_target_value(self, key, dic, tmp_list):

        if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
            return 'argv[1] not an dict or argv[-1] not an list '

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    self.get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
                elif isinstance(value, (list, tuple)):
                    self._get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
        return tmp_list

    def _get_value(self, key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
            elif isinstance(val_, (list, tuple)):
                self._get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身


if __name__ == '__main__':
    data = getSubImageDict.getSubImageDict().get_SubImageDict()
    print(Json_Loop().get_target_value('level4Name', data, []))
    # print(Json_Loop().get_target_value('annexMaxSize', data, []))
    #
    # print(Json_Loop().get_target_value('level4Code', data, []))
