more_strategies
===============

Extra hypothesis strategies


URL
---

.. code-block:: python

    >>> from more_strategies import URL
    
    >>> URL().example()
    ParseResult(scheme='vz47zrwv3udelvsscor1onz61fchhfzsys3bhs1yvmqncr91l1vqyqep7clnjecja1z9h4117ps87ovocmfa71uu7sxaveshzfsjjeuffe7f8ls9aazx3e247lfz12l7sbrd7vv1eldt7nvueqsbcj1us', netloc='i.x.5.j.r.r.j.0.o.c.x.n.j.a.bwwbyjgjomccpniyqfwbpowtqqiwscfzfunspnjmnoiowuifpy', path='', params='', query='', fragment='')

    >>> URL(userpass=True, port=True, url=True, query=True, fragment=True).example()
    ParseResult(scheme='t1aifipkzqyfqp3xotl', netloc='fitjnfh7jfc7xqxi7uzczhkx6ad31va9o:kbwwuxoz7hwgr52pnb29248a6cfs82b35xky976pli81rtsvcwusgw7gxyry78fxf0qb6pcwe33bei5u7b79f7f7p89rpifr1psbtl1ubs6188r83ub7i89o7i6fbc89bm5zivx65fz297vsca7gxb3awj46wi8wuwttupbtvsbp3xigguk8gzx9r559nwdw7m8vfx5i5vwrchcw61c3rc9c76j5gk6cprmj6x56us6x5lj8w6sjyjwwhvnkfzvruu6@ce7kjpku.vv9lh77j3.vf6ha.omj1m97qlipp4xykbhxcscjvk76c2ia5po4ekcpjkp80hp86h9uu4h1lo2q6o0hfpv1q7subqndcq13gup1vhlhhvc52o9veqx09h4imvghr99g8oyfe.h.qwtaotlfaheepyssayqx:47029', path='/%F2%BE%9B%BF%F2%A2%B6%89%C4%B5%C4%B5%C4%B5%F0%9E%BA%AF%F0%9E%BA%AF%7F%F2%8B%A3%83%7F%F2%BE%9B%BF%F2%BE%9B%BF%7F%F2%A2%B6%89%F2%8B%A3%83%7F%F2%BE%9B%BF////%F2%A2%B6%89', params='', query='lkgadqpujtrudmotwpjkmbjgpciowmdetiqmflcreklphjfaowdpdkujbrtdrkybdadubpdkhcjwhg=3qqu69pu5mnha4snu69qmvbapj6x6a6vusb2bx9c3zm499bucpxamqcn55b6dl66676vmmqn87bcuqhwpy85hmpamc7xj7lib3iqni861l458oacu91l8ux3kb1pgca496cpp33a5n9j378bah14uv97qy0xb9nacrx54rs0yix4xjpmu34599e9lmiz756myylbvq322615z6i5xbbsnbubh2po4nmnnvjsili14xm1r6x199184p8aidmya1mubp5p6maxjv9qxxmmhnqbluqjl9ns1mm5b1kp1tl9cpr5sph', fragment='%F2%A8%AC%96%F2%B5%AF%B4%F2%AC%96%B8%F2%B5%AF%B4%F1%A6%94%A2')

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
