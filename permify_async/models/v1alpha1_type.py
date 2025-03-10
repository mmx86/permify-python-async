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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from permify_async.models.primitive_type import PrimitiveType
from permify_async.models.well_known_type import WellKnownType
from typing import Optional, Set
from typing_extensions import Self

class V1alpha1Type(BaseModel):
    """
    Represents a CEL type.
    """ # noqa: E501
    dyn: Optional[Dict[str, Any]] = Field(default=None, description="Dynamic type.")
    null: Optional[StrictStr] = Field(default=None, description="Null value.")
    primitive: Optional[PrimitiveType] = PrimitiveType.PRIMITIVE_TYPE_UNSPECIFIED
    wrapper: Optional[PrimitiveType] = PrimitiveType.PRIMITIVE_TYPE_UNSPECIFIED
    well_known: Optional[WellKnownType] = Field(default=WellKnownType.WELL_KNOWN_TYPE_UNSPECIFIED, alias="wellKnown")
    list_type: Optional[ListType] = Field(default=None, alias="listType")
    map_type: Optional[MapType] = Field(default=None, alias="mapType")
    function: Optional[FunctionType] = None
    message_type: Optional[StrictStr] = Field(default=None, description="Protocol buffer message type.  The `message_type` string specifies the qualified message type name. For example, `google.plus.Profile`.", alias="messageType")
    type_param: Optional[StrictStr] = Field(default=None, description="Type param type.  The `type_param` string specifies the type parameter name, e.g. `list<E>` would be a `list_type` whose element type was a `type_param` type named `E`.", alias="typeParam")
    type: Optional[V1alpha1Type] = None
    error: Optional[Dict[str, Any]] = Field(default=None, description="Error type.  During type-checking if an expression is an error, its type is propagated as the `ERROR` type. This permits the type-checker to discover other errors present in the expression.")
    abstract_type: Optional[AbstractType] = Field(default=None, alias="abstractType")
    __properties: ClassVar[List[str]] = ["dyn", "null", "primitive", "wrapper", "wellKnown", "listType", "mapType", "function", "messageType", "typeParam", "type", "error", "abstractType"]

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
        """Create an instance of V1alpha1Type from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of list_type
        if self.list_type:
            _dict['listType'] = self.list_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of map_type
        if self.map_type:
            _dict['mapType'] = self.map_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of function
        if self.function:
            _dict['function'] = self.function.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of abstract_type
        if self.abstract_type:
            _dict['abstractType'] = self.abstract_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1alpha1Type from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dyn": obj.get("dyn"),
            "null": obj.get("null"),
            "primitive": obj.get("primitive") if obj.get("primitive") is not None else PrimitiveType.PRIMITIVE_TYPE_UNSPECIFIED,
            "wrapper": obj.get("wrapper") if obj.get("wrapper") is not None else PrimitiveType.PRIMITIVE_TYPE_UNSPECIFIED,
            "wellKnown": obj.get("wellKnown") if obj.get("wellKnown") is not None else WellKnownType.WELL_KNOWN_TYPE_UNSPECIFIED,
            "listType": ListType.from_dict(obj["listType"]) if obj.get("listType") is not None else None,
            "mapType": MapType.from_dict(obj["mapType"]) if obj.get("mapType") is not None else None,
            "function": FunctionType.from_dict(obj["function"]) if obj.get("function") is not None else None,
            "messageType": obj.get("messageType"),
            "typeParam": obj.get("typeParam"),
            "type": V1alpha1Type.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "error": obj.get("error"),
            "abstractType": AbstractType.from_dict(obj["abstractType"]) if obj.get("abstractType") is not None else None
        })
        return _obj

from permify_async.models.abstract_type import AbstractType
from permify_async.models.function_type import FunctionType
from permify_async.models.list_type import ListType
from permify_async.models.map_type import MapType
# TODO: Rewrite to not use raise_errors
V1alpha1Type.model_rebuild(raise_errors=False)

