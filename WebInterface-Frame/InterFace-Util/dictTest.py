# -*- coding:utf-8 -*-
"""
@Time:2018/2/8 19:05
@Author:dongbaolei
"""

CASEINFO_OUTPUT_TMPL = r"""%(caseinfo)s"""

hhh=r"""%(caseinfo)s""" % dict(
                caseinfo="123345",
            )

print(hhh)