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

from permify_async.models.permission_definition import PermissionDefinition

class TestPermissionDefinition(unittest.TestCase):
    """PermissionDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PermissionDefinition:
        """Test PermissionDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PermissionDefinition`
        """
        model = PermissionDefinition()
        if include_optional:
            return PermissionDefinition(
                name = '',
                child = permify_async.models.child.Child(
                    leaf = permify_async.models.leaf.Leaf(
                        computed_user_set = permify_async.models.computed_user_set.ComputedUserSet(
                            relation = '', ), 
                        tuple_to_user_set = permify_async.models.tuple_to_user_set.TupleToUserSet(
                            tuple_set = permify_async.models.tuple_set.TupleSet(
                                relation = '', ), 
                            computed = permify_async.models.computed_user_set.ComputedUserSet(
                                relation = '', ), ), 
                        computed_attribute = permify_async.models.computed_attribute.ComputedAttribute(
                            name = '', ), 
                        call = permify_async.models.v1/call.v1.Call(
                            rule_name = '', 
                            arguments = [
                                permify_async.models.argument.Argument(
                                    context_attribute = permify_async.models.context_attribute.ContextAttribute(
                                        name = '', ), )
                                ], ), ), 
                    rewrite = permify_async.models.rewrite.Rewrite(
                        rewrite_operation = 'OPERATION_UNSPECIFIED', 
                        children = [
                            permify_async.models.child.Child()
                            ], ), )
            )
        else:
            return PermissionDefinition(
        )
        """

    def testPermissionDefinition(self):
        """Test PermissionDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()