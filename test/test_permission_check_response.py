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

from permify_async.models.permission_check_response import PermissionCheckResponse

class TestPermissionCheckResponse(unittest.TestCase):
    """PermissionCheckResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionCheckResponse:
        """Test PermissionCheckResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionCheckResponse`
        """
        model = PermissionCheckResponse()
        if include_optional:
            return PermissionCheckResponse(
                can = 'CHECK_RESULT_UNSPECIFIED',
                metadata = permify_async.models.permission_check_response_metadata.PermissionCheckResponseMetadata(
                    check_count = 56, )
            )
        else:
            return PermissionCheckResponse(
        )
        """

    def testPermissionCheckResponse(self):
        """Test PermissionCheckResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
