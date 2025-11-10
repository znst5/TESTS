from habr import get_result
import time
import pytest
import requests
from uuid import uuid4


URL = 'https://habr.com/ru/search/?q='

def things(queries):
    params = {}
    for query in queries:
        params = {
         'q': query,
         }
    return params

things(['new', 'Photoshop', 'switches'])

