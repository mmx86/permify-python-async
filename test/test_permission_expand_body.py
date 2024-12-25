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

from permify_async.models.permission_expand_body import PermissionExpandBody

class TestPermissionExpandBody(unittest.TestCase):
    """PermissionExpandBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionExpandBody:
        """Test PermissionExpandBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionExpandBody`
        """
        model = PermissionExpandBody()
        if include_optional:
            return PermissionExpandBody(
                metadata = permify_async.models.permission_expand_request_metadata.PermissionExpandRequestMetadata(
                    schema_version = '', 
                    snap_token = '', ),
                entity = permify_async.models.entity.Entity(
                    type = '', 
                    id = '', ),
                permission = '',
                context = permify_async.models.context.Context(
                    tuples = [
                        permify_async.models.tuple.Tuple(
                            entity = permify_async.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            relation = '', 
                            subject = permify_async.models.subject.Subject(
                                type = '', 
                                id = '', 
                                relation = '', ), )
                        ], 
                    attributes = [
                        permify_async.models.attribute.Attribute(
                            attribute = '', 
                            value = {
                                'key' : None
                                }, )
                        ], 
                    data = permify_async.models.data.data(), ),
                arguments = [
                    permify_async.models.argument.Argument(
                        computed_attribute = permify_async.models.computed_attribute.ComputedAttribute(
                            name = '', ), )
                    ]
            )
        else:
            return PermissionExpandBody(
        )
        """

    def testPermissionExpandBody(self):
        """Test PermissionExpandBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()