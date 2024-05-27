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

from permify_async.models.relationship_delete_request import RelationshipDeleteRequest

class TestRelationshipDeleteRequest(unittest.TestCase):
    """RelationshipDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelationshipDeleteRequest:
        """Test RelationshipDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelationshipDeleteRequest`
        """
        model = RelationshipDeleteRequest()
        if include_optional:
            return RelationshipDeleteRequest(
                filter = permify_async.models.tuple_filter.TupleFilter(
                    entity = permify_async.models.entity_filter.EntityFilter(
                        type = '', 
                        ids = [
                            ''
                            ], ), 
                    relation = '', 
                    subject = permify_async.models.subject_filter.SubjectFilter(
                        type = '', 
                        ids = [
                            ''
                            ], 
                        relation = '', ), )
            )
        else:
            return RelationshipDeleteRequest(
        )
        """

    def testRelationshipDeleteRequest(self):
        """Test RelationshipDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
