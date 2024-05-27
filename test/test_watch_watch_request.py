# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.6.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify_async.models.watch_watch_request import WatchWatchRequest

class TestWatchWatchRequest(unittest.TestCase):
    """WatchWatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WatchWatchRequest:
        """Test WatchWatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WatchWatchRequest`
        """
        model = WatchWatchRequest()
        if include_optional:
            return WatchWatchRequest(
                snap_token = ''
            )
        else:
            return WatchWatchRequest(
        )
        """

    def testWatchWatchRequest(self):
        """Test WatchWatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()