from hypothesis import given
from more_strategies import mysql_utf8

@given(mysql_utf8())
def test_max_length_3(s):
    if len(s) > 0:
        assert max(len(c.encode('utf-8')) for c in s) < 4
