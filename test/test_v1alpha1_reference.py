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

from permify_async.models.v1alpha1_reference import V1alpha1Reference

class TestV1alpha1Reference(unittest.TestCase):
    """V1alpha1Reference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1Reference:
        """Test V1alpha1Reference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1Reference`
        """
        model = V1alpha1Reference()
        if include_optional:
            return V1alpha1Reference(
                name = '',
                overload_id = [
                    ''
                    ],
                value = permify_async.models.constant.Constant(
                    null_value = '', 
                    bool_value = True, 
                    int64_value = '', 
                    uint64_value = '', 
                    double_value = 1.337, 
                    string_value = '', 
                    bytes_value = 'YQ==', 
                    duration_value = '', 
                    timestamp_value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return V1alpha1Reference(
        )
        """

    def testV1alpha1Reference(self):
        """Test V1alpha1Reference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
