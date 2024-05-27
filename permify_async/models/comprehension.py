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

class Comprehension(BaseModel):
    """
    A comprehension expression applied to a list or map.  Comprehensions are not part of the core syntax, but enabled with macros. A macro matches a specific call signature within a parsed AST and replaces the call with an alternate AST block. Macro expansion happens at parse time.  The following macros are supported within CEL:  Aggregate type macros may be applied to all elements in a list or all keys in a map:  *  `all`, `exists`, `exists_one` -  test a predicate expression against    the inputs and return `true` if the predicate is satisfied for all,    any, or only one value `list.all(x, x < 10)`. *  `filter` - test a predicate expression against the inputs and return    the subset of elements which satisfy the predicate:    `payments.filter(p, p > 1000)`. *  `map` - apply an expression to all elements in the input and return the    output aggregate type: `[1, 2, 3].map(i, i * i)`.  The `has(m.x)` macro tests whether the property `x` is present in struct `m`. The semantics of this macro depend on the type of `m`. For proto2 messages `has(m.x)` is defined as 'defined, but not set`. For proto3, the macro tests whether the property is set to its default. For map and struct types, the macro tests whether the property `x` is defined on `m`.
    """ # noqa: E501
    iter_var: Optional[StrictStr] = Field(default=None, description="The name of the iteration variable.", alias="iterVar")
    iter_range: Optional[Expr] = Field(default=None, alias="iterRange")
    accu_var: Optional[StrictStr] = Field(default=None, description="The name of the variable used for accumulation of the result.", alias="accuVar")
    accu_init: Optional[Expr] = Field(default=None, alias="accuInit")
    loop_condition: Optional[Expr] = Field(default=None, alias="loopCondition")
    loop_step: Optional[Expr] = Field(default=None, alias="loopStep")
    result: Optional[Expr] = None
    __properties: ClassVar[List[str]] = ["iterVar", "iterRange", "accuVar", "accuInit", "loopCondition", "loopStep", "result"]

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
        """Create an instance of Comprehension from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of iter_range
        if self.iter_range:
            _dict['iterRange'] = self.iter_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accu_init
        if self.accu_init:
            _dict['accuInit'] = self.accu_init.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_condition
        if self.loop_condition:
            _dict['loopCondition'] = self.loop_condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loop_step
        if self.loop_step:
            _dict['loopStep'] = self.loop_step.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Comprehension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iterVar": obj.get("iterVar"),
            "iterRange": Expr.from_dict(obj["iterRange"]) if obj.get("iterRange") is not None else None,
            "accuVar": obj.get("accuVar"),
            "accuInit": Expr.from_dict(obj["accuInit"]) if obj.get("accuInit") is not None else None,
            "loopCondition": Expr.from_dict(obj["loopCondition"]) if obj.get("loopCondition") is not None else None,
            "loopStep": Expr.from_dict(obj["loopStep"]) if obj.get("loopStep") is not None else None,
            "result": Expr.from_dict(obj["result"]) if obj.get("result") is not None else None
        })
        return _obj

from permify_async.models.expr import Expr
# TODO: Rewrite to not use raise_errors
Comprehension.model_rebuild(raise_errors=False)

