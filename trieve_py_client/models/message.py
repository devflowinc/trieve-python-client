# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.6.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Message(BaseModel):
    """
    Message
    """ # noqa: E501
    completion_tokens: Optional[StrictInt] = None
    content: StrictStr
    created_at: datetime
    dataset_id: StrictStr
    deleted: StrictBool
    id: StrictStr
    prompt_tokens: Optional[StrictInt] = None
    role: StrictStr
    sort_order: StrictInt
    topic_id: StrictStr
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["completion_tokens", "content", "created_at", "dataset_id", "deleted", "id", "prompt_tokens", "role", "sort_order", "topic_id", "updated_at"]

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
        """Create an instance of Message from a JSON string"""
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
        # set to None if completion_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.completion_tokens is None and "completion_tokens" in self.model_fields_set:
            _dict['completion_tokens'] = None

        # set to None if prompt_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_tokens is None and "prompt_tokens" in self.model_fields_set:
            _dict['prompt_tokens'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion_tokens": obj.get("completion_tokens"),
            "content": obj.get("content"),
            "created_at": obj.get("created_at"),
            "dataset_id": obj.get("dataset_id"),
            "deleted": obj.get("deleted"),
            "id": obj.get("id"),
            "prompt_tokens": obj.get("prompt_tokens"),
            "role": obj.get("role"),
            "sort_order": obj.get("sort_order"),
            "topic_id": obj.get("topic_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


