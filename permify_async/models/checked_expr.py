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
from permify_async.models.expr import Expr
from permify_async.models.source_info import SourceInfo
from permify_async.models.v1alpha1_reference import V1alpha1Reference
from permify_async.models.v1alpha1_type import V1alpha1Type
from typing import Optional, Set
from typing_extensions import Self

class CheckedExpr(BaseModel):
    """
    A CEL expression which has been successfully type checked.
    """ # noqa: E501
    reference_map: Optional[Dict[str, V1alpha1Reference]] = Field(default=None, description="A map from expression ids to resolved references.  The following entries are in this table:  - An Ident or Select expression is represented here if it resolves to a   declaration. For instance, if `a.b.c` is represented by   `select(select(id(a), b), c)`, and `a.b` resolves to a declaration,   while `c` is a field selection, then the reference is attached to the   nested select expression (but not to the id or or the outer select).   In turn, if `a` resolves to a declaration and `b.c` are field selections,   the reference is attached to the ident expression. - Every Call expression has an entry here, identifying the function being   called. - Every CreateStruct expression for a message has an entry, identifying   the message.", alias="referenceMap")
    type_map: Optional[Dict[str, V1alpha1Type]] = Field(default=None, description="A map from expression ids to types.  Every expression node which has a type different than DYN has a mapping here. If an expression has type DYN, it is omitted from this map to save space.", alias="typeMap")
    source_info: Optional[SourceInfo] = Field(default=None, alias="sourceInfo")
    expr_version: Optional[StrictStr] = Field(default=None, description="The expr version indicates the major / minor version number of the `expr` representation.  The most common reason for a version change will be to indicate to the CEL runtimes that transformations have been performed on the expr during static analysis. In some cases, this will save the runtime the work of applying the same or similar transformations prior to evaluation.", alias="exprVersion")
    expr: Optional[Expr] = None
    __properties: ClassVar[List[str]] = ["referenceMap", "typeMap", "sourceInfo", "exprVersion", "expr"]

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
        """Create an instance of CheckedExpr from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in reference_map (dict)
        _field_dict = {}
        if self.reference_map:
            for _key_reference_map in self.reference_map:
                if self.reference_map[_key_reference_map]:
                    _field_dict[_key_reference_map] = self.reference_map[_key_reference_map].to_dict()
            _dict['referenceMap'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in type_map (dict)
        _field_dict = {}
        if self.type_map:
            for _key_type_map in self.type_map:
                if self.type_map[_key_type_map]:
                    _field_dict[_key_type_map] = self.type_map[_key_type_map].to_dict()
            _dict['typeMap'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of source_info
        if self.source_info:
            _dict['sourceInfo'] = self.source_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expr
        if self.expr:
            _dict['expr'] = self.expr.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CheckedExpr from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referenceMap": dict(
                (_k, V1alpha1Reference.from_dict(_v))
                for _k, _v in obj["referenceMap"].items()
            )
            if obj.get("referenceMap") is not None
            else None,
            "typeMap": dict(
                (_k, V1alpha1Type.from_dict(_v))
                for _k, _v in obj["typeMap"].items()
            )
            if obj.get("typeMap") is not None
            else None,
            "sourceInfo": SourceInfo.from_dict(obj["sourceInfo"]) if obj.get("sourceInfo") is not None else None,
            "exprVersion": obj.get("exprVersion"),
            "expr": Expr.from_dict(obj["expr"]) if obj.get("expr") is not None else None
        })
        return _obj


