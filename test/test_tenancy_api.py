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

from permify_async.api.tenancy_api import TenancyApi


class TestTenancyApi(unittest.IsolatedAsyncioTestCase):
    """TenancyApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = TenancyApi()

    async def asyncTearDown(self) -> None:
        pass

    async def test_tenants_create(self) -> None:
        """Test case for tenants_create

        create tenant
        """
        pass

    async def test_tenants_delete(self) -> None:
        """Test case for tenants_delete

        delete tenant
        """
        pass

    async def test_tenants_list(self) -> None:
        """Test case for tenants_list

        list tenants
        """
        pass


if __name__ == '__main__':
    unittest.main()
