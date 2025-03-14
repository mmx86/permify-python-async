# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.2.3
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EntityDefinitionReference(str, Enum):
    """
    The Reference enum specifies whether a name pertains to a relation, permission, or attribute.   - REFERENCE_UNSPECIFIED: Default, unspecified reference.  - REFERENCE_RELATION: Indicates that the name refers to a relation.  - REFERENCE_PERMISSION: Indicates that the name refers to a permission.  - REFERENCE_ATTRIBUTE: Indicates that the name refers to an attribute.
    """

    """
    allowed enum values
    """
    REFERENCE_UNSPECIFIED = 'REFERENCE_UNSPECIFIED'
    REFERENCE_RELATION = 'REFERENCE_RELATION'
    REFERENCE_PERMISSION = 'REFERENCE_PERMISSION'
    REFERENCE_ATTRIBUTE = 'REFERENCE_ATTRIBUTE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntityDefinitionReference from a JSON string"""
        return cls(json.loads(json_str))


