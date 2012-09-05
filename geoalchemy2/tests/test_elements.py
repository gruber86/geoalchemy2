import unittest
import re

from nose.tools import eq_


def eq_sql(a, b, msg=None):
    a = re.sub(r'[\n\t]', '', str(a))
    eq_(a, b, msg)


class TestWKTElement(unittest.TestCase):

    def test_desc(self):
        from geoalchemy2.elements import WKTElement
        e = WKTElement('POINT(1 2)')
        eq_(e.desc, 'POINT(1 2)')


class TestWKBElement(unittest.TestCase):

    def test_desc(self):
        from geoalchemy2.elements import WKBElement
        e = WKBElement('\x01\x02')
        eq_(e.desc, '0102')

    def test_function_call(self):
        from geoalchemy2.elements import WKBElement
        e = WKBElement('\x01\x02')
        f = e.ST_Buffer(2)
        eq_sql(f,
               'ST_Buffer(ST_GeomFromWKB(:ST_GeomFromWKB_1), :param_1)')
        eq_(f.compile().params,
            {u'ST_GeomFromWKB_1': '\x01\x02', u'param_1': 2})