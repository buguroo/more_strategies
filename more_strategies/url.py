from string import ascii_lowercase, digits
from urllib.parse import quote, urlunparse

from hypothesis import strategies as st
from hypothesis import strategy


def to_url(kwargs):
    user = kwargs.get("user", "")
    passwd = kwargs.get("passwd", "")
    port = kwargs.get("port")
    url = '/'.join(map(quote, kwargs.get('url', [])))
    params = ""
    fragment = kwargs.get('fragment', '')

    q_keys = kwargs.get('keys', [])
    q_values = kwargs.get('values', [])
    if q_keys and q_values:
        kv = zip(q_keys, q_values)
        query = '&'.join("%s=%s" % (k, v) for k, v in kv)
    else:
        query = ""
        
    netloc = "{userpass}{domain}{port}".format(
        userpass="%s:%s@" % (user, passwd) if user and passwd else "",
        domain='.'.join(kwargs["domain"]),
        port=':%s' % str(port) if port is not None else "")

    return urlunparse((kwargs['scheme'], netloc, url, params, query, fragment))


def URL(userpass=False, port=False, url=False, query=False, fragment=False):

    d = {'scheme': st.text(alphabet=ascii_lowercase+digits, min_size=2),
         'domain': st.lists(st.text(alphabet=ascii_lowercase + digits,
                                    min_size=1), min_size=1)}

    if userpass:
        d['user'] = st.text(alphabet=ascii_lowercase + digits)
        d['passwd'] = st.text(alphabet=ascii_lowercase + digits)
    if port:
        d['port'] = st.integers(min_value=0, max_value=65535)
    if url:
        d['url'] = st.lists(st.text())
    if query:
        d['keys'] = st.lists(st.text(alphabet=ascii_lowercase))
        d['values'] = st.lists(st.text(alphabet=ascii_lowercase + digits))
    if fragment:
        d['fragment'] = st.text()

    urlst = strategy(st.fixed_dictionaries(d))

    return urlst.map(to_url)
