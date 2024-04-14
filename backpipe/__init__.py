"""
--- Backpipe ---

Backends simplified.
Backpipe is an API creation framework.

Backpipe by Simoso68 is licensed under the GNU GPL v3.

Check it out under:

https://github.com/Simoso68/backpipe
https://pypi.org/project/backpipe
"""

# Request.params will be renamed to Request.query at a later point in time.

from .app import BackPipe
from .rq import Request
from .config import config
from colorama import init as __init

__init()

__version__ = "0.4.1"