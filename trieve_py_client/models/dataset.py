# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.6.2
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Dataset(BaseModel):
    """
    Dataset
    """ # noqa: E501
    client_configuration: Optional[Any]
    created_at: datetime
    id: StrictStr
    name: StrictStr
    organization_id: StrictStr
    server_configuration: Optional[Any]
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["client_configuration", "created_at", "id", "name", "organization_id", "server_configuration", "updated_at"]

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
        """Create an instance of Dataset from a JSON string"""
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
        # set to None if client_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.client_configuration is None and "client_configuration" in self.model_fields_set:
            _dict['client_configuration'] = None

        # set to None if server_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.server_configuration is None and "server_configuration" in self.model_fields_set:
            _dict['server_configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dataset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_configuration": obj.get("client_configuration"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization_id": obj.get("organization_id"),
            "server_configuration": obj.get("server_configuration"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


