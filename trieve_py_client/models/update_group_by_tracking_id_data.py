# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.7.6
    Contact: developers@trieve.ai
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

class UpdateGroupByTrackingIDData(BaseModel):
    """
    UpdateGroupByTrackingIDData
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description to assign to the chunk_group. Convenience field for you to avoid having to remember what the group is for. If not provided, the description will not be updated.")
    metadata: Optional[Any] = Field(default=None, description="Optional metadata to assign to the chunk_group. This is a JSON object that can store any additional information you want to associate with the chunks inside of the chunk_group.")
    name: Optional[StrictStr] = Field(default=None, description="Name to assign to the chunk_group. Does not need to be unique. If not provided, the name will not be updated.")
    tag_set: Optional[List[StrictStr]] = Field(default=None, description="Optional tags to assign to the chunk_group. This is a list of strings that can be used to categorize the chunks inside the chunk_group.")
    tracking_id: StrictStr = Field(description="Tracking Id of the chunk_group to update.")
    __properties: ClassVar[List[str]] = ["description", "metadata", "name", "tag_set", "tracking_id"]

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
        """Create an instance of UpdateGroupByTrackingIDData from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateGroupByTrackingIDData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "tag_set": obj.get("tag_set"),
            "tracking_id": obj.get("tracking_id")
        })
        return _obj


