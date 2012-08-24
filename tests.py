#!/usr/bin/env python

from StringIO import StringIO

from parameterizedtestcase import ParameterizedTestCase


def square(x):
    return x * x


class MyTests(ParameterizedTestCase):
    stringio = StringIO()

    @ParameterizedTestCase.parameterize(("input", "expected_output"), [(1, 1), (2, 4), (3, 9), (4, 16)])
    def test_square(self, input, expected_output):
        # print("test_square: input = %r; expected_output = %r" % (input, expected_output))
        self.log_message("test_square: input = %r; expected_output = %r\n" % (input, expected_output))
        self.assertEqual(square(input), expected_output)

    def test_zzz_right_stuff_called(self):
        """Check that test_square was called multiple times with correct parameters.

        """

        self.assertEqual(
            self.get_log_output(),
            "\n".join([
                "test_square: input = 1; expected_output = 1",
                "test_square: input = 2; expected_output = 4",
                "test_square: input = 3; expected_output = 9",
                "test_square: input = 4; expected_output = 16"]) + "\n")

    def log_message(self, msg):
        self.stringio.write(msg)

    def get_log_output(self):
        return self.stringio.getvalue()

