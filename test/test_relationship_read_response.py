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

from permify_async.models.relationship_read_response import RelationshipReadResponse

class TestRelationshipReadResponse(unittest.TestCase):
    """RelationshipReadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationshipReadResponse:
        """Test RelationshipReadResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationshipReadResponse`
        """
        model = RelationshipReadResponse()
        if include_optional:
            return RelationshipReadResponse(
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
                continuous_token = ''
            )
        else:
            return RelationshipReadResponse(
        )
        """

    def testRelationshipReadResponse(self):
        """Test RelationshipReadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
