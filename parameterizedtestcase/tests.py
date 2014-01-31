#!/usr/bin/env python

from __future__ import with_statement

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO as StringIO  # Python 3

from parameterizedtestcase import ParameterizedTestMixin, ParameterizedTestCase


class BaseTestParameterizedTestCase(ParameterizedTestCase):
    lst = []

    def log_message(self, msg):
        self.lst.append(msg)

    def get_log_output(self):
        return self.lst


class MyParameterizedTestCase1(BaseTestParameterizedTestCase):
    @ParameterizedTestCase.parameterize(
        ("input", "expected_output"),
        [("2+4", 6),
         ("3+5", 8),
         ("6*9", 54)])
    def test_eval(self, input, expected_output):
        self.log_message(
            "test_eval: input = %r; expected_output = %r" % (
                input, expected_output))
        self.assertEqual(eval(input), expected_output)

    def test_eval_zzz(self):
        self.assertEqual(
            sorted(self.get_log_output()),
            sorted([
                "test_eval: input = '2+4'; expected_output = 6",
                "test_eval: input = '3+5'; expected_output = 8",
                "test_eval: input = '6*9'; expected_output = 54"]))


class MyParameterizedTestCase2(BaseTestParameterizedTestCase):
    @ParameterizedTestCase.parameterize(
        ("input_dict", "expected_output"),
        [({'num1': 2, 'num2': 4, 'sum': 6}, 6),
         ({'num1': 3, 'num2': 5, 'sum': 8}, 8),
         ({'num1': 4, 'num2': 6, 'sum': 10}, 10)])
    def test_with_dict_args(self, input_dict, expected_output):
        self.log_message(
            "test_with_dict_args: num1 = %d; num2 = %d;"
            " expected_output = %r" % (
                input_dict['num1'], input_dict['num2'], expected_output))
        self.assertEqual(
            input_dict['num1'] + input_dict['num2'],
            expected_output)

    def test_with_dict_args_zzz(self):
        self.assertEqual(
            sorted(self.get_log_output()),
            sorted([
                "test_with_dict_args: num1 = 2; num2 = 4;"
                " expected_output = 6",
                "test_with_dict_args: num1 = 3; num2 = 5;"
                " expected_output = 8",
                "test_with_dict_args: num1 = 4; num2 = 6;"
                " expected_output = 10"]))


class MyParameterizedTestCase2(unittest.TestCase, ParameterizedTestMixin):

    @ParameterizedTestMixin.parameterize(("numerator",), [(1,), (2,), (3,)])
    def test_assertRaises(self, numerator):
        """Test assertRaises with a context manager

        `assertRaises` is not present in `unittest.TestCase` in Python 2.5,
        2.6, or 3.0, but it is present in unittest2.TestCase

        """
        with self.assertRaises(ZeroDivisionError):
            numerator / 0


if __name__ == '__main__':
    unittest.main()
