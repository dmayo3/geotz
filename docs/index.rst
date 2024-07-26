geotz v0.0.2-alpha
==================

`GitHub repository <https://github.com/dmayo3/geotz>`_

This is a simple, lightweight library designed for fast and easy lookup
of time zones based on country code and postal code or postal code prefix.

It leverages offline data from www.geonames.org to determine the approximate
location and convert it into a time zone, all without the need for network
requests or external APIs.

Contents:
---------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   license

Introduction
------------

Geotz aims to provide a straightforward and efficient solution for applications requiring time zone data.

It is less feature-rich but easier to use and lighter than alternatives such as `geopy` or `pgeocode`.

Features include:

- **No API Key Required**: No need to manage API keys or external API services.
- **Offline Functionality**: Performs all operations offline.
- **Bundled Data**: Comes packaged with all necessary geographical data.
- **On-Demand Data Loading**: Loads data as needed to minimize memory usage.
- **Minimal Dependencies**: Keeps additional dependencies to a minimum.

Getting Started
---------------

To get started with geotz, see the Installation section, followed by the
Usage guide to see how to implement geotz in your projects.

Limitations
-----------

Some countries are not supported, and there are no guarantees that every postal code will be found.

Some timezones may be inaccurate, particularly around timezone borders. Hopefully the differences
are off by no more than an hour.

Here are some details about supported and unsupported locations:

.. automodule:: geotz
   :members: UNSUPPORTED_LOCATIONS, UNSUPPORTED_COUNTRY_CODES, SUPPORTED_COUNTRY_CODES


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
