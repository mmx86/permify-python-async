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
from permify_async.models.leaf import Leaf
from typing import Optional, Set
from typing_extensions import Self

class Child(BaseModel):
    """
    Child represents a node in the permission tree.
    """ # noqa: E501
    leaf: Optional[Leaf] = None
    rewrite: Optional[Rewrite] = None
    __properties: ClassVar[List[str]] = ["leaf", "rewrite"]

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
        """Create an instance of Child from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of leaf
        if self.leaf:
            _dict['leaf'] = self.leaf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rewrite
        if self.rewrite:
            _dict['rewrite'] = self.rewrite.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Child from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "leaf": Leaf.from_dict(obj["leaf"]) if obj.get("leaf") is not None else None,
            "rewrite": Rewrite.from_dict(obj["rewrite"]) if obj.get("rewrite") is not None else None
        })
        return _obj

from permify_async.models.rewrite import Rewrite
# TODO: Rewrite to not use raise_errors
Child.model_rebuild(raise_errors=False)

