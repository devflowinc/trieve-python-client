# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.5.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from trieve_python_client.models.field_condition import FieldCondition
from typing import Optional, Set
from typing_extensions import Self

class ChunkFilter(BaseModel):
    """
    ChunkFilter
    """ # noqa: E501
    must: Optional[List[FieldCondition]] = Field(default=None, description="All of these field conditions have to match for the chunk to be included in the result set.")
    must_not: Optional[List[FieldCondition]] = Field(default=None, description="None of these field conditions can match for the chunk to be included in the result set.")
    should: Optional[List[FieldCondition]] = Field(default=None, description="Only one of these field conditions has to match for the chunk to be included in the result set.")
    __properties: ClassVar[List[str]] = ["must", "must_not", "should"]

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
        """Create an instance of ChunkFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in must (list)
        _items = []
        if self.must:
            for _item in self.must:
                if _item:
                    _items.append(_item.to_dict())
            _dict['must'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in must_not (list)
        _items = []
        if self.must_not:
            for _item in self.must_not:
                if _item:
                    _items.append(_item.to_dict())
            _dict['must_not'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in should (list)
        _items = []
        if self.should:
            for _item in self.should:
                if _item:
                    _items.append(_item.to_dict())
            _dict['should'] = _items
        # set to None if must (nullable) is None
        # and model_fields_set contains the field
        if self.must is None and "must" in self.model_fields_set:
            _dict['must'] = None

        # set to None if must_not (nullable) is None
        # and model_fields_set contains the field
        if self.must_not is None and "must_not" in self.model_fields_set:
            _dict['must_not'] = None

        # set to None if should (nullable) is None
        # and model_fields_set contains the field
        if self.should is None and "should" in self.model_fields_set:
            _dict['should'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChunkFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "must": [FieldCondition.from_dict(_item) for _item in obj["must"]] if obj.get("must") is not None else None,
            "must_not": [FieldCondition.from_dict(_item) for _item in obj["must_not"]] if obj.get("must_not") is not None else None,
            "should": [FieldCondition.from_dict(_item) for _item in obj["should"]] if obj.get("should") is not None else None
        })
        return _obj

