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


class MyParameterizedTestCase1(ParameterizedTestCase):
    stringio = StringIO()

    @ParameterizedTestCase.parameterize(("input", "expected_output"), [
        ("2+4", 6),
        ("3+5", 8),
        ("6*9", 54),
    ])
    def test_eval(self, input, expected_output):
        self.log_message(
            "test_eval: input = %r; expected_output = %r\n" % (
                input, expected_output))
        self.assertEqual(eval(input), expected_output)

    def test_zzz_test_eval_called_multiple_times_with_correct_params(self):
        self.assertEqual(
            self.get_log_output(),
            "\n".join([
                "test_eval: input = '2+4'; expected_output = 6",
                "test_eval: input = '3+5'; expected_output = 8",
                "test_eval: input = '6*9'; expected_output = 54"]) + "\n")

    def log_message(self, msg):
        self.stringio.write(msg)

    def get_log_output(self):
        return self.stringio.getvalue()


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
