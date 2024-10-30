from flask import Flask
from flask_caching import Cache

from typing import Optional
from .select_element_helper import SelectElementHelper

FLASK_APP:Optional[Flask] = None
FLASK_CACHE:Optional[Cache] = None