import unicodedata

from hypothesis import strategies as st
from hypothesis import strategy
from hypothesis.searchstrategy.strings import OneCharStringStrategy
from functools import wraps


class MySQLOneCharStringStrategy(OneCharStringStrategy):

    def simplifiers(self, random, template):
        def filter_bad_chars(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return (c for c in fn(*args, **kwargs) if self.is_good(c))
            return wrapper

        return (filter_bad_chars(simplifiers)
                for simplifiers in
                super().simplifiers(random, template))

    def is_good(self, char):
        try:
            encoded = char.encode('utf-8')
        except UnicodeEncodeError:
            can_encode = False
            encoded = b''
        else:
            can_encode = True
        finally:
            is_surrogate = unicodedata.category(char) == 'Cs'

        return can_encode and len(encoded) <= 3 and not is_surrogate


def mysql_utf8(min_size=None, average_size=None, max_size=None):

    from hypothesis.searchstrategy.strings import StringStrategy

    return StringStrategy(st.lists(
        MySQLOneCharStringStrategy(),
        average_size=average_size,
        min_size=min_size,
        max_size=max_size
    ))
