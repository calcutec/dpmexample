# -*- coding: utf-8 -*-

"""
pythoncompat

Copied from requests
"""

import sys

# -------
# Pythons
# -------

PY3 = sys.version_info[0] == 3


# ---------
# Specifics
# ---------


if PY3:
    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)


try:
    from zipfile import ZIP64_VERSION
except ImportError:
    ZIP64_VERSION = 45

try:
    from zipfile import BZIP2_VERSION
except ImportError:
    BZIP2_VERSION = 46

try:
    from zipfile import ZIP_BZIP2
except ImportError:
    ZIP_BZIP2 = 12

try:
    from zipfile import LZMA_VERSION
except ImportError:
    LZMA_VERSION = 63

try:
    from zipfile import ZIP_LZMA
except ImportError:
    ZIP_LZMA = 14

try:
    from zipfile import ZIP_MAX_COMMENT
except ImportError:
    ZIP_MAX_COMMENT = (1 << 16) - 1