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

from permify_async.models.data_changes import DataChanges

class TestDataChanges(unittest.TestCase):
    """DataChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataChanges:
        """Test DataChanges
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataChanges`
        """
        model = DataChanges()
        if include_optional:
            return DataChanges(
                snap_token = '',
                data_changes = [
                    permify_async.models.data_change.DataChange(
                        operation = 'OPERATION_UNSPECIFIED', 
                        tuple = permify_async.models.tuple.Tuple(
                            entity = permify_async.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            relation = '', 
                            subject = permify_async.models.subject.Subject(
                                type = '', 
                                id = '', 
                                relation = '', ), ), 
                        attribute = permify_async.models.attribute.Attribute(
                            value = {
                                'key' : None
                                }, ), )
                    ]
            )
        else:
            return DataChanges(
        )
        """

    def testDataChanges(self):
        """Test DataChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()