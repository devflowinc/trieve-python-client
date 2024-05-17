# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.8.5
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

class AuthQuery(BaseModel):
    """
    AuthQuery
    """ # noqa: E501
    inv_code: Optional[StrictStr] = Field(default=None, description="Code sent via email as a result of successful call to send_invitation")
    organization_id: Optional[StrictStr] = Field(default=None, description="ID of organization to authenticate into")
    redirect_uri: Optional[StrictStr] = Field(default=None, description="URL to redirect to after successful login")
    __properties: ClassVar[List[str]] = ["inv_code", "organization_id", "redirect_uri"]

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
        """Create an instance of AuthQuery from a JSON string"""
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
        # set to None if inv_code (nullable) is None
        # and model_fields_set contains the field
        if self.inv_code is None and "inv_code" in self.model_fields_set:
            _dict['inv_code'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organization_id'] = None

        # set to None if redirect_uri (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_uri is None and "redirect_uri" in self.model_fields_set:
            _dict['redirect_uri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inv_code": obj.get("inv_code"),
            "organization_id": obj.get("organization_id"),
            "redirect_uri": obj.get("redirect_uri")
        })
        return _obj


