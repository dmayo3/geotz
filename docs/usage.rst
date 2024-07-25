Usage
=====

.. doctest::

    >>> import geotz

    >>> geotz.lookup('US', '10001')
    'America/New_York'

    >>> geotz.lookup('JP', '100-0001')
    'Asia/Tokyo'

    >>> geotz.lookup('GB', 'SW1A 0AA')
    'Europe/London'

    >>> geotz.lookup('FR', '75008')
    'Europe/Paris'

If `lookup()` does not find a time zone, it returns `None`.

It's important to handle this possibility in your code:

.. doctest::

    >>> print(geotz.lookup('XX', '99999'))
    None
