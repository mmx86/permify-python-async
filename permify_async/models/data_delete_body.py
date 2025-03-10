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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from permify_async.models.attribute_filter import AttributeFilter
from permify_async.models.tuple_filter import TupleFilter
from typing import Optional, Set
from typing_extensions import Self

class DataDeleteBody(BaseModel):
    """
    DataDeleteRequest defines the structure of a request to delete data. It includes the tenant_id and filters for selecting tuples and attributes to be deleted.
    """ # noqa: E501
    tuple_filter: Optional[TupleFilter] = None
    attribute_filter: Optional[AttributeFilter] = None
    __properties: ClassVar[List[str]] = ["tuple_filter", "attribute_filter"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataDeleteBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tuple_filter
        if self.tuple_filter:
            _dict['tuple_filter'] = self.tuple_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attribute_filter
        if self.attribute_filter:
            _dict['attribute_filter'] = self.attribute_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataDeleteBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tuple_filter": TupleFilter.from_dict(obj["tuple_filter"]) if obj.get("tuple_filter") is not None else None,
            "attribute_filter": AttributeFilter.from_dict(obj["attribute_filter"]) if obj.get("attribute_filter") is not None else None
        })
        return _obj


