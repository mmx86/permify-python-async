# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.2.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify_async.api.watch_api import WatchApi


class TestWatchApi(unittest.IsolatedAsyncioTestCase):
    """WatchApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = WatchApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_watch_watch(self) -> None:
        """Test case for watch_watch

        watch changes
        """
        pass


if __name__ == '__main__':
    unittest.main()
