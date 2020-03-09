# SDTLpy
[![Build Status](https://travis-ci.org/ThomasThelen/SDTLpy.svg?branch=master)](https://travis-ci.org/ThomasThelen/SDTLpy)
[![codecov](https://codecov.io/gh/ThomasThelen/SDTLpy/branch/master/graph/badge.svg)](https://codecov.io/gh/ThomasThelen/SDTLpy)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)]()

Python library for generating SDTL via C2Metadata deployments


### How to Use

1. Decide which endpoint to use (R vs STATA/SASS)
1. Create the SDTLClient, passing the endpoint url to it
1. Add your scripts to SDTLClient with `add_directory()` or `add_file()`
1. Call `transform()` to query the service
1. Save them to disk with `save()`
