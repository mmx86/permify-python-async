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

from permify_async.models.data_write_response import DataWriteResponse

class TestDataWriteResponse(unittest.TestCase):
    """DataWriteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataWriteResponse:
        """Test DataWriteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataWriteResponse`
        """
        model = DataWriteResponse()
        if include_optional:
            return DataWriteResponse(
                snap_token = ''
            )
        else:
            return DataWriteResponse(
        )
        """

    def testDataWriteResponse(self):
        """Test DataWriteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
