more_strategies
===============

Extra hypothesis strategies


URL
---

.. code-block:: python

    >>> from from more_strategies import URL
    
    >>> URL().example()
    'kvog210zodz9po2dqchosv3zd40vjzzc://i.1.k.m.0.r.u.z.t.7.a.h.0.i.l'

    >>> URL(userpass=True, port=True, url=True, query=True, fragment=True).example()

    'tc://enz6lm39v4lk89rv9w6lt22g8dlj4v:axaqmi@o.l.5.7.p.7.7.5.i.1.e:45250/%F2%B5%A0%8B%F2%BF%B2%B9%F3%8D%80%89%F3%96%94%AC%F2%BF%B2%B9%F1%AF%B6%84%F2%BF%B2%B9%F1%86%8F%96%F3%8D%80%89%F1%AF%B6%84%F2%8F%B0%86%F1%AF%B6%84%F2%B9%A4%A0%F1%B8%B5%A4%F3%8D%80%89%F0%A7%95%88%F0%A7%95%88?otptaagnwpxdpzkoicqvtmlexcgvqsugodsupujmcehngeqcphzauabbamxurixnsceionoqtpaoejeeudwhcpgtwaxggpcbuqeivknronpkjjjsrucorzjjzeihiszmqinhnxchoeoazzexkxpbagurzwcnaesotpnaptwqtxhrqxrnevtdvxvwxxhtqwkixixbttmixozuqcoexchqxhuozxoqrhpjctgpqjpscehazvapmbzzxtkrtcarreecjpzpqszgdmnn=t3w&uvzbtqqraceoqtxngtvxgtesdeqzzweqtporqxgvucsbzausqtxtkezutipqzeclddkodawoaep=677n33246iew33j2btnk0k9d7k0#\U0001daee\U00072617\U000b16b2\x19\U0001daee\U000c6482\U000b16b2t\U0002e600\U000dd769\U0002e402\U00072617\U0002e402\U000b16b2\ued49\U000dd769'

And of course:

.. code-block:: python

    @given(url=URL())
    def test_true(url):
        assert True


IP
--

Generates IPv4 only.

.. code-block:: python

    >>> from from more_strategies import IP
    
    >>> IP().example()
    IPv4Address('82.247.101.60')
