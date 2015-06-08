import ipaddress

from hypothesis import strategies as st
from hypothesis import strategy


def to_ip(un32):
    return ipaddress.ip_address(un32)


def IP():
    ipst = strategy(st.integers(min_value=0, max_value=int(0xffffffff)))
    return ipst.map(to_ip)
