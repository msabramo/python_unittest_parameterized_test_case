try:
    import unittest2 as unittest
except ImportError:
    import unittest

from functools import wraps


def get_decorated_method_name(method_name, param_names, param_values):
    name_components = []

    for k, v in zip(param_names, param_values):
        name_components.append(str(k))
        name_components.append(str(v))

    return '%s_%s' % (method_name, '_'.join(name_components))


def augment_method_docstring(method, new_class_dict, classname,
                             param_names, param_values, new_method):
    param_assignments_str = '; '.join(
        ['%s = %s' % (k, v) for (k, v) in zip(param_names, param_values)])
    extra_doc = "%s (%s.%s) [with %s] " % (
        method.__name__, new_class_dict.get('__module__', '<module>'),
        classname, param_assignments_str)

    try:
        new_method.__doc__ = extra_doc + new_method.__doc__
    except TypeError:  # Catches when new_method.__doc__ is None
        new_method.__doc__ = extra_doc


class ParameterizedTestCaseMetaClass(type):

    def __new__(meta, classname, bases, class_dict):
        new_class_dict = {}

        for attr_name, attr_value in class_dict.items():
            if callable(attr_value) and hasattr(attr_value, 'param_names'):
                # print("Processing attr_name = %r; attr_value = %r" % (
                #     attr_name, attr_value))

                method = attr_value
                param_names = attr_value.param_names
                data = attr_value.data

                meta.process_method(
                    classname, method, param_names, data, new_class_dict)
            else:
                new_class_dict[attr_name] = attr_value

        return type.__new__(meta, classname, bases, new_class_dict)

    @classmethod
    def process_method(
            cls, classname, method, param_names, data, new_class_dict):
        for param_values in data:
            new_method = cls.new_method(method, param_values)
            new_method.__name__ = get_decorated_method_name(
                method.__name__, param_names, param_values)
            augment_method_docstring(
                method, new_class_dict, classname,
                param_names, param_values, new_method)
            new_class_dict[new_method.__name__] = new_method

    @classmethod
    def new_method(cls, method, param_values):
        @wraps(method)
        def new_method(self):
            return method(self, *param_values)

        return new_method


class ParameterizedTestMixin(object):
    __metaclass__ = ParameterizedTestCaseMetaClass

    @classmethod
    def parameterize(cls, param_names, data):
        """Decorator for parameterizing a test method - example:

        @ParameterizedTestCase.parameterize(
            ("isbn", "expected_title"), [
                ("0262033844", "Introduction to Algorithms"),
                ("0321558146", "Campbell Essential Biology")])

        """

        def decorator(func):
            @wraps(func)
            def newfunc(*arg, **kwargs):
                return func(*arg, **kwargs)

            newfunc.param_names = param_names
            newfunc.data = data

            return newfunc

        return decorator


class ParameterizedTestCase(unittest.TestCase, ParameterizedTestMixin):
    __metaclass__ = ParameterizedTestCaseMetaClass
