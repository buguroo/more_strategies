from ipaddress import ip_address

from hypothesis import strategies as st
from hypothesis import strategy


def to_ip(args):
    ip = '.'.join([str(p) for p in args])
    return ip_address(ip)


def IP():
    part = st.integers(min_value=0, max_value=255)
    ipst = strategy(st.lists(part, min_size=4, max_size=4))

    return ipst.map(to_ip)
