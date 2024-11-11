import json
from hubspot.callsFilter import CallsFilter
import pytest


def test_calls_filter():
    cf = CallsFilter()
    assert cf.countMaxOverlappingCalls([]) == {"results": []}
