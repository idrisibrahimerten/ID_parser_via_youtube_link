# -*- coding: utf-8 -*-
"""
@author: IdrisIbrahimERTEN
"""

import urllib.parse as urlparse

url = urlparse.urlparse("https://www.youtube.com/watch?v=LR47mE04yys")

query = urlparse.parse_qs(url.query)

videoID = query["v"][0]

print(videoID)