from flask import Flask
from flask_caching import Cache

from typing import Optional
from .select_element_helper import SelectElementHelper
__version__="0.0.0" #The version string will be replaced by CI/CD

FLASK_APP:Optional[Flask] = None
FLASK_CACHE:Optional[Cache] = None