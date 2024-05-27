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

from permify_async.models.expand_leaf import ExpandLeaf

class TestExpandLeaf(unittest.TestCase):
    """ExpandLeaf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExpandLeaf:
        """Test ExpandLeaf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExpandLeaf`
        """
        model = ExpandLeaf()
        if include_optional:
            return ExpandLeaf(
                subjects = permify_async.models.subjects.Subjects(),
                values = permify_async.models.values.Values(),
                value = {
                    'key' : None
                    }
            )
        else:
            return ExpandLeaf(
        )
        """

    def testExpandLeaf(self):
        """Test ExpandLeaf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
