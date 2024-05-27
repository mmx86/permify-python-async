# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v0.6.1
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V1Operation(BaseModel):
    """
    Operation is a message representing a series of operations that can be performed. It includes fields for writing and deleting relationships and attributes.
    """ # noqa: E501
    relationships_write: Optional[List[StrictStr]] = Field(default=None, description="'relationships_write' is a repeated string field for storing relationship keys that are to be written or created.")
    relationships_delete: Optional[List[StrictStr]] = Field(default=None, description="'relationships_delete' is a repeated string field for storing relationship keys that are to be deleted or removed.")
    attributes_write: Optional[List[StrictStr]] = Field(default=None, description="'attributes_write' is a repeated string field for storing attribute keys that are to be written or created.")
    attributes_delete: Optional[List[StrictStr]] = Field(default=None, description="'attributes_delete' is a repeated string field for storing attribute keys that are to be deleted or removed.")
    __properties: ClassVar[List[str]] = ["relationships_write", "relationships_delete", "attributes_write", "attributes_delete"]

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
        """Create an instance of V1Operation from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1Operation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "relationships_write": obj.get("relationships_write"),
            "relationships_delete": obj.get("relationships_delete"),
            "attributes_write": obj.get("attributes_write"),
            "attributes_delete": obj.get("attributes_delete")
        })
        return _obj


