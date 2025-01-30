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


class NullValue(str, Enum):
    """
    `NullValue` is a singleton enumeration to represent the null value for the `Value` type union.  The JSON representation for `NullValue` is JSON `null`.   - NULL_VALUE: Null value.
    """

    """
    allowed enum values
    """
    NULL_VALUE = 'NULL_VALUE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NullValue from a JSON string"""
        return cls(json.loads(json_str))


