python_unittest_parameterized_test_case
=======================================

[![Build Status](https://secure.travis-ci.org/msabramo/python_unittest_parameterized_test_case.png?branch=master)](http://travis-ci.org/msabramo/python_unittest_parameterized_test_case)

Parameterized tests for Python's unittest module

This was inspired by the [parameterized tests
feature](http://pytest.org/latest/example/parametrize.html) in
[py.test](http://pytest.org/). I had been using py.test for the
particular test that motivated this, but my colleague had some
reservations about using py.test and all I really needed was the
parameterized tests so I whipped this up with a bit of metaclass
hackery.

Example usage:

```python
from parameterizedtestcase import ParameterizedTestCase


class MyTests(ParameterizedTestCase):
    @ParameterizedTestCase.parameterize(("input", "expected_output"), [
        ("2+4", 6),
        ("3+5", 8),
        ("6*9", 54),
    ])
    def test_eval(self, input, expected_output):
        self.assertEqual(eval(input), expected_output)
```

Result of running this:

```
~/dev/git-repos/python_unittest_parameterized_test_case$ python -m unittest -v tests
test_eval_input_2+4_expected_output_6 (tests.MyTests) ... ok
test_eval_input_3+5_expected_output_8 (tests.MyTests) ... ok
test_eval_input_6*9_expected_output_54 (tests.MyTests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
