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


class ExpandTreeNodeOperation(str, Enum):
    """
    Operation is an enum representing the type of operation to be applied on the tree node.
    """

    """
    allowed enum values
    """
    OPERATION_UNSPECIFIED = 'OPERATION_UNSPECIFIED'
    OPERATION_UNION = 'OPERATION_UNION'
    OPERATION_INTERSECTION = 'OPERATION_INTERSECTION'
    OPERATION_EXCLUSION = 'OPERATION_EXCLUSION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ExpandTreeNodeOperation from a JSON string"""
        return cls(json.loads(json_str))


