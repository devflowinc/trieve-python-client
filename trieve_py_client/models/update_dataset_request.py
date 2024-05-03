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

class UpdateDatasetRequest(BaseModel):
    """
    UpdateDatasetRequest
    """ # noqa: E501
    client_configuration: Optional[Any] = Field(default=None, description="The new client configuration of the dataset, can be arbitrary JSON. See docs.trieve.ai for more information. If not provided, the client configuration will not be updated.")
    dataset_id: Optional[StrictStr] = Field(default=None, description="The id of the dataset you want to update.")
    dataset_name: Optional[StrictStr] = Field(default=None, description="The new name of the dataset. Must be unique within the organization. If not provided, the name will not be updated.")
    server_configuration: Optional[Any] = Field(default=None, description="The new server configuration of the dataset, can be arbitrary JSON. See docs.trieve.ai for more information. If not provided, the server configuration will not be updated.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="tracking ID for the dataset. Can be used to track the dataset in external systems.")
    __properties: ClassVar[List[str]] = ["client_configuration", "dataset_id", "dataset_name", "server_configuration", "tracking_id"]

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
        """Create an instance of UpdateDatasetRequest from a JSON string"""
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

        # set to None if dataset_id (nullable) is None
        # and model_fields_set contains the field
        if self.dataset_id is None and "dataset_id" in self.model_fields_set:
            _dict['dataset_id'] = None

        # set to None if dataset_name (nullable) is None
        # and model_fields_set contains the field
        if self.dataset_name is None and "dataset_name" in self.model_fields_set:
            _dict['dataset_name'] = None

        # set to None if server_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.server_configuration is None and "server_configuration" in self.model_fields_set:
            _dict['server_configuration'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateDatasetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_configuration": obj.get("client_configuration"),
            "dataset_id": obj.get("dataset_id"),
            "dataset_name": obj.get("dataset_name"),
            "server_configuration": obj.get("server_configuration"),
            "tracking_id": obj.get("tracking_id")
        })
        return _obj


