from string import ascii_lowercase, digits
from urllib import parse
import random

from hypothesis import strategies as st
from hypothesis import strategy


def to_url(kwargs):
    user = kwargs.get("user", "")
    passwd = kwargs.get("passwd", "")
    port = kwargs.get("port")
    url = '/'.join(map(parse.quote, kwargs.get('url', [])))
    params = ""
    query_map = kwargs.get("query", [])
    fragment = parse.quote(kwargs.get("fragment", ""))

    query = '&'.join(["%s=%s" % (k, str(v)) for k, v in query_map])
        
    netloc = "{userpass}{domain}{port}".format(
        userpass="%s:%s@" % (user, passwd) if user and passwd else "",
        domain='.'.join(kwargs["domain"]) + '.' + kwargs["tld"],
        port=':%s' % str(port) if port is not None else "")

    return parse.urlparse(parse.urlunparse(
        (kwargs['scheme'], netloc, url, params, query, fragment)))


def url(schemes=[], userpass=False, port=False, url=False, query=False,
        fragment=False):

    if schemes:
        scheme = st.just(random.choice(schemes))
    else:
        scheme = st.text(alphabet=ascii_lowercase+digits, min_size=2)

    d = {'scheme': scheme,
         'domain': st.lists(
             st.text(
                 alphabet=ascii_lowercase + digits,
                 min_size=1,
                 max_size=63),
             min_size=1,
             max_size=3),
         'tld': st.text(alphabet=ascii_lowercase, min_size=2, max_size=63)}

    if userpass:
        d['user'] = st.text(alphabet=ascii_lowercase + digits)
        d['passwd'] = st.text(alphabet=ascii_lowercase + digits)
    if port:
        d['port'] = st.integers(min_value=0, max_value=65535)
    if url:
        d['url'] = st.lists(st.text())
    if query:
        d['query'] = st.lists(st.tuples(
            st.text(alphabet=ascii_lowercase, min_size=1),
            st.text(alphabet=ascii_lowercase + digits, min_size=1)))
    if fragment:
        d['fragment'] = st.text()

    urlst = strategy(st.fixed_dictionaries(d))

    return urlst.map(to_url)
