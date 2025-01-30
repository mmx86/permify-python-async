# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.8.7
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from permify_async.models.expand import Expand

class TestExpand(unittest.TestCase):
    """Expand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Expand:
        """Test Expand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Expand`
        """
        model = Expand()
        if include_optional:
            return Expand(
                entity = permify_async.models.entity.Entity(
                    type = '', 
                    id = '', ),
                permission = '',
                arguments = [
                    permify_async.models.argument.Argument(
                        computed_attribute = permify_async.models.computed_attribute.ComputedAttribute(
                            name = '', ), 
                        context_attribute = permify_async.models.context_attribute.ContextAttribute(
                            name = '', ), )
                    ],
                expand = permify_async.models.expand_tree_node.ExpandTreeNode(
                    operation = 'OPERATION_UNSPECIFIED', 
                    children = [
                        permify_async.models.expand.Expand(
                            entity = permify_async.models.entity.Entity(
                                type = '', 
                                id = '', ), 
                            permission = '', 
                            arguments = [
                                permify_async.models.argument.Argument(
                                    computed_attribute = permify_async.models.computed_attribute.ComputedAttribute(
                                        name = '', ), 
                                    context_attribute = permify_async.models.context_attribute.ContextAttribute(
                                        name = '', ), )
                                ], 
                            expand = permify_async.models.expand_tree_node.ExpandTreeNode(
                                children = [
                                    permify_async.models.expand.Expand(
                                        permission = '', 
                                        leaf = permify_async.models.expand_leaf.ExpandLeaf(
                                            subjects = permify_async.models.subjects.Subjects(), 
                                            values = permify_async.models.values.Values(), 
                                            value = {
                                                'key' : None
                                                }, ), )
                                    ], ), 
                            leaf = permify_async.models.expand_leaf.ExpandLeaf(), )
                        ], ),
                leaf = permify_async.models.expand_leaf.ExpandLeaf(
                    subjects = permify_async.models.subjects.Subjects(), 
                    values = permify_async.models.values.Values(), 
                    value = {
                        'key' : None
                        }, )
            )
        else:
            return Expand(
        )
        """

    def testExpand(self):
        """Test Expand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
