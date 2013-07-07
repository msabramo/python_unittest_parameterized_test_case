python_unittest_parameterized_test_case
=======================================

.. image:: https://secure.travis-ci.org/msabramo/python_unittest_parameterized_test_case.png?branch=master
   :target: http://travis-ci.org/msabramo/python_unittest_parameterized_test_case

Parameterized tests for Python's unittest module

This was inspired by the `parameterized tests
feature <http://pytest.org/latest/example/parametrize.html>`_ in
`py.test <http://pytest.org/>`_. I had been using py.test for the
particular test that motivated this, but my colleague had some
reservations about using py.test and all I really needed was the
parameterized tests so I whipped this up with a bit of metaclass
hackery.


Example usage
-------------

.. code-block:: python

    from parameterizedtestcase import ParameterizedTestCase

    class MyTests(ParameterizedTestCase):
        @ParameterizedTestCase.parameterize(
            ("input", "expected_output"),
            [
                ("2+4", 6),
                ("3+5", 8),
                ("6*9", 54),
            ]
        )
        def test_eval(self, input, expected_output):
            self.assertEqual(eval(input), expected_output)

Result of running this::

    ~/dev/git-repos/python_unittest_parameterized_test_case$ python -m unittest -v tests
    test_eval_input_2+4_expected_output_6 (tests.MyTests) ... ok
    test_eval_input_3+5_expected_output_8 (tests.MyTests) ... ok
    test_eval_input_6*9_expected_output_54 (tests.MyTests) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK


Supported Python versions
-------------------------

- Python 2.5
- Python 2.6
- Python 2.7
- Python 3.1
- Python 3.2
- Python 3.3
- PyPy 1.9
- Jython 2.5

or says `tox <http://tox.testrun.org/>`_::

    ~/dev/git-repos/python_unittest_parameterized_test_case$ tox
    ...
      py25: commands succeeded
      py26: commands succeeded
      py27: commands succeeded
      py31: commands succeeded
      py32: commands succeeded
      py33: commands succeeded
      jython: commands succeeded
      pypy: commands succeeded
      congratulations :)

You also can check the `latest Travis CI results
<http://travis-ci.org/msabramo/python_unittest_parameterized_test_case>`_, but
Travis doesn't build all of the above platforms.


Issues
------

Send your bug reports and feature requests to https://github.com/msabramo/python_unittest_parameterized_test_case/issues

