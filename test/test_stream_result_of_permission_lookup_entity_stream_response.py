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

from permify_async.models.stream_result_of_permission_lookup_entity_stream_response import StreamResultOfPermissionLookupEntityStreamResponse

class TestStreamResultOfPermissionLookupEntityStreamResponse(unittest.TestCase):
    """StreamResultOfPermissionLookupEntityStreamResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamResultOfPermissionLookupEntityStreamResponse:
        """Test StreamResultOfPermissionLookupEntityStreamResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamResultOfPermissionLookupEntityStreamResponse`
        """
        model = StreamResultOfPermissionLookupEntityStreamResponse()
        if include_optional:
            return StreamResultOfPermissionLookupEntityStreamResponse(
                result = permify_async.models.permission_lookup_entity_stream_response.PermissionLookupEntityStreamResponse(
                    entity_id = '', 
                    continuous_token = '', ),
                error = permify_async.models.status.Status(
                    code = 56, 
                    message = '', 
                    details = [
                        {
                            'key' : None
                            }
                        ], )
            )
        else:
            return StreamResultOfPermissionLookupEntityStreamResponse(
        )
        """

    def testStreamResultOfPermissionLookupEntityStreamResponse(self):
        """Test StreamResultOfPermissionLookupEntityStreamResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
