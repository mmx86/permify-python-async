# coding: utf-8

"""
    Permify API

    Permify is an open source authorization service for creating fine-grained and scalable authorization systems.

    The version of the OpenAPI document: v1.2.4
    Contact: hello@permify.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from permify_async.models.context import Context
from permify_async.models.permission_lookup_entity_request_metadata import PermissionLookupEntityRequestMetadata
from permify_async.models.string_array_value import StringArrayValue
from permify_async.models.subject import Subject
from typing import Optional, Set
from typing_extensions import Self

class LookupEntityStreamBody(BaseModel):
    """
    PermissionLookupEntityRequest is the request message for the LookupEntity method in the Permission service.
    """ # noqa: E501
    metadata: Optional[PermissionLookupEntityRequestMetadata] = None
    entity_type: Optional[StrictStr] = Field(default=None, description="Type of the entity to lookup, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes.")
    permission: Optional[StrictStr] = Field(default=None, description="Name of the permission to check, required, must start with a letter and can include alphanumeric and underscore, max 64 bytes.")
    subject: Optional[Subject] = None
    context: Optional[Context] = None
    scope: Optional[Dict[str, StringArrayValue]] = Field(default=None, description="Scope: A map that associates entity types with lists of identifiers. Each entry helps filter requests by specifying which entities are relevant to the operation.")
    page_size: Optional[StrictInt] = Field(default=None, description="page_size is the number of entities to be returned in the response. The value should be between 1 and 100.")
    continuous_token: Optional[StrictStr] = Field(default=None, description="continuous_token is an optional parameter used for pagination. It should be the value received in the previous response.")
    __properties: ClassVar[List[str]] = ["metadata", "entity_type", "permission", "subject", "context", "scope", "page_size", "continuous_token"]

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
        """Create an instance of LookupEntityStreamBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in scope (dict)
        _field_dict = {}
        if self.scope:
            for _key_scope in self.scope:
                if self.scope[_key_scope]:
                    _field_dict[_key_scope] = self.scope[_key_scope].to_dict()
            _dict['scope'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LookupEntityStreamBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": PermissionLookupEntityRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "entity_type": obj.get("entity_type"),
            "permission": obj.get("permission"),
            "subject": Subject.from_dict(obj["subject"]) if obj.get("subject") is not None else None,
            "context": Context.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "scope": dict(
                (_k, StringArrayValue.from_dict(_v))
                for _k, _v in obj["scope"].items()
            )
            if obj.get("scope") is not None
            else None,
            "page_size": obj.get("page_size"),
            "continuous_token": obj.get("continuous_token")
        })
        return _obj


