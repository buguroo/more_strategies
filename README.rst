more_strategies
===============

Extra hypothesis strategies


URL
---

.. code-block:: python

    >>> from more_strategies import URL
    
    >>> URL().example()
    'kvog210zodz9po2dqchosv3zd40vjzzc://i.1.k.m.0.r.u.z.t.7.a.h.0.i.l'

    >>> URL(userpass=True, port=True, url=True, query=True, fragment=True).example()

    'vo7yoxza3://yxndjgm8ak6:t@5.8f5.vk679v.l.2g8.7.p5u.o.8z1.m3.rhv:62010/%F0%93%AD%AC%F3%B6%83%90%F1%80%96%AE%F4%86%9C%86%F3%B6%83%90%F4%86%9C%86%F1%80%96%AE%F4%86%9C%86%F4%86%9C%86%F1%85%B3%B4%F1%85%B3%B4%F2%A0%BA%B2%F1%85%B3%B4?vgaj=vql63dyzjutfvbakalqggqgkgsl7rcmlb0gqzsiaqkpgjgv3qbikckzbrblitm05q5q0gsakvlsyy43z7qzjc9igsv5yxv3u5qcfyyvlx57cgsq0qpcusds1g6kj0qyq6k9&qgpdjpaawohfv=ijbh5s3lmi09l33szvfcgvggd3v4vdqkkpq0id50c41qgmyer3e5yru4gmmvwyvsylibx6cprq&l=sr5i4r30z9dv2zg00r3muczqlfg5sigrzdqy#%C2%8E%F3%B5%B3%AC%F1%A4%AF%9B%F0%A7%A1%B3%F3%B5%B3%AC%20%F0%90%99%85%C2%8E%F0%A2%85%B7%F0%A2%85%B7%C2%8E%C2%8E%F1%A4%AF%9B%20%F3%B5%B3%AC%F0%90%99%85%F2%B9%B1%84%F3%B5%B3%AC%20%F0%A2%85%B7%C2%8E%C2%8E'

And of course:

.. code-block:: python

    @given(url=URL())
    def test_true(url):
        assert True


IP
--

Generates IPv4 only.

.. code-block:: python

    >>> from more_strategies import IP
    
    >>> IP().example()
    IPv4Address('82.247.101.60')
