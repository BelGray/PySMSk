from enum import Enum

import requests


class Formats(Enum):
    JSON = "JSON"
    DEFAULT = None

class Methods(Enum):
    POST = requests.post
    GET = requests.get
    PUT = requests.put
    DELETE = requests.delete
    PATCH = requests.patch
    HEAD = requests.head
    OPTIONS = requests.options
