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

from permify_async.models.data_bundle import DataBundle

class TestDataBundle(unittest.TestCase):
    """DataBundle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataBundle:
        """Test DataBundle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataBundle`
        """
        model = DataBundle()
        if include_optional:
            return DataBundle(
                name = '',
                arguments = [
                    ''
                    ],
                operations = [
                    permify_async.models.v1/operation.v1.Operation(
                        relationships_write = [
                            ''
                            ], 
                        relationships_delete = [
                            ''
                            ], 
                        attributes_write = [
                            ''
                            ], 
                        attributes_delete = [
                            ''
                            ], )
                    ]
            )
        else:
            return DataBundle(
        )
        """

    def testDataBundle(self):
        """Test DataBundle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
