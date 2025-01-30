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


class AttributeType(str, Enum):
    """
    Enumerates the types of attribute.   - ATTRIBUTE_TYPE_UNSPECIFIED: Not specified attribute type. This is the default value.  - ATTRIBUTE_TYPE_BOOLEAN: A boolean attribute type.  - ATTRIBUTE_TYPE_BOOLEAN_ARRAY: A boolean array attribute type.  - ATTRIBUTE_TYPE_STRING: A string attribute type.  - ATTRIBUTE_TYPE_STRING_ARRAY: A string array attribute type.  - ATTRIBUTE_TYPE_INTEGER: An integer attribute type.  - ATTRIBUTE_TYPE_INTEGER_ARRAY: An integer array attribute type.  - ATTRIBUTE_TYPE_DOUBLE: A double attribute type.  - ATTRIBUTE_TYPE_DOUBLE_ARRAY: A double array attribute type.
    """

    """
    allowed enum values
    """
    ATTRIBUTE_TYPE_UNSPECIFIED = 'ATTRIBUTE_TYPE_UNSPECIFIED'
    ATTRIBUTE_TYPE_BOOLEAN = 'ATTRIBUTE_TYPE_BOOLEAN'
    ATTRIBUTE_TYPE_BOOLEAN_ARRAY = 'ATTRIBUTE_TYPE_BOOLEAN_ARRAY'
    ATTRIBUTE_TYPE_STRING = 'ATTRIBUTE_TYPE_STRING'
    ATTRIBUTE_TYPE_STRING_ARRAY = 'ATTRIBUTE_TYPE_STRING_ARRAY'
    ATTRIBUTE_TYPE_INTEGER = 'ATTRIBUTE_TYPE_INTEGER'
    ATTRIBUTE_TYPE_INTEGER_ARRAY = 'ATTRIBUTE_TYPE_INTEGER_ARRAY'
    ATTRIBUTE_TYPE_DOUBLE = 'ATTRIBUTE_TYPE_DOUBLE'
    ATTRIBUTE_TYPE_DOUBLE_ARRAY = 'ATTRIBUTE_TYPE_DOUBLE_ARRAY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AttributeType from a JSON string"""
        return cls(json.loads(json_str))


