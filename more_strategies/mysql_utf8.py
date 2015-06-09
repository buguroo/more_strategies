from hypothesis import strategies as st
from hypothesis import strategy
from hypothesis.searchstrategy.strings import OneCharStringStrategy


class MySQLOneCharStringStrategy(OneCharStringStrategy):

    def is_good(self, char):
        return super().is_good(char) and len(char.encode('utf-8')) <= 3


def mysql_utf8(min_size=None, average_size=None, max_size=None):

    from hypothesis.searchstrategy.strings import StringStrategy

    return StringStrategy(st.lists(
        MySQLOneCharStringStrategy(),
        average_size=average_size,
        min_size=min_size,
        max_size=max_size
    ))
