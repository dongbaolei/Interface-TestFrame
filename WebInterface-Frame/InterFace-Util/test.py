# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 14:18
@Author:dongbaolei
"""
from nose.tools import assert_equal
from parameterized import parameterized

import unittest
import math

@parameterized([
    (2, 2, 4),
    (2, 3, 8),
    (1, 9, 1),
    (0, 9, 0),
])
def test_pow(base, exponent, expected):
    assert_equal(math.pow(base, exponent), expected)

class TestMathUnitTest(unittest.TestCase):
    @parameterized.expand([
        ("negative", -1.5, -2.0),
        ("integer", 1, 1.0),
        ("large fraction", 1.6, 1),
    ])
    def test_floor(self, name, input, expected):
        assert_equal(math.floor(input), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)