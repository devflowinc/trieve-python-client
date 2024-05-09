# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.8.2
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
from trieve_py_client.models.location_bounding_box import LocationBoundingBox
from trieve_py_client.models.location_polygon import LocationPolygon
from trieve_py_client.models.location_radius import LocationRadius
from trieve_py_client.models.match_condition import MatchCondition
from trieve_py_client.models.range import Range
from typing import Optional, Set
from typing_extensions import Self

class FieldCondition(BaseModel):
    """
    FieldCondition
    """ # noqa: E501
    field: StrictStr = Field(description="Field is the name of the field to filter on. The field value will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. To access fields inside of the metadata that you provide with the card, prefix the field name with `metadata.`.")
    geo_bounding_box: Optional[LocationBoundingBox] = None
    geo_polygon: Optional[LocationPolygon] = None
    geo_radius: Optional[LocationRadius] = None
    match: Optional[List[MatchCondition]] = Field(default=None, description="Match is the value to match on the field. The match value will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata.")
    range: Optional[Range] = None
    __properties: ClassVar[List[str]] = ["field", "geo_bounding_box", "geo_polygon", "geo_radius", "match", "range"]

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
        """Create an instance of FieldCondition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geo_bounding_box
        if self.geo_bounding_box:
            _dict['geo_bounding_box'] = self.geo_bounding_box.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_polygon
        if self.geo_polygon:
            _dict['geo_polygon'] = self.geo_polygon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_radius
        if self.geo_radius:
            _dict['geo_radius'] = self.geo_radius.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in match (list)
        _items = []
        if self.match:
            for _item in self.match:
                if _item:
                    _items.append(_item.to_dict())
            _dict['match'] = _items
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        # set to None if geo_bounding_box (nullable) is None
        # and model_fields_set contains the field
        if self.geo_bounding_box is None and "geo_bounding_box" in self.model_fields_set:
            _dict['geo_bounding_box'] = None

        # set to None if geo_polygon (nullable) is None
        # and model_fields_set contains the field
        if self.geo_polygon is None and "geo_polygon" in self.model_fields_set:
            _dict['geo_polygon'] = None

        # set to None if geo_radius (nullable) is None
        # and model_fields_set contains the field
        if self.geo_radius is None and "geo_radius" in self.model_fields_set:
            _dict['geo_radius'] = None

        # set to None if match (nullable) is None
        # and model_fields_set contains the field
        if self.match is None and "match" in self.model_fields_set:
            _dict['match'] = None

        # set to None if range (nullable) is None
        # and model_fields_set contains the field
        if self.range is None and "range" in self.model_fields_set:
            _dict['range'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FieldCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "field": obj.get("field"),
            "geo_bounding_box": LocationBoundingBox.from_dict(obj["geo_bounding_box"]) if obj.get("geo_bounding_box") is not None else None,
            "geo_polygon": LocationPolygon.from_dict(obj["geo_polygon"]) if obj.get("geo_polygon") is not None else None,
            "geo_radius": LocationRadius.from_dict(obj["geo_radius"]) if obj.get("geo_radius") is not None else None,
            "match": [MatchCondition.from_dict(_item) for _item in obj["match"]] if obj.get("match") is not None else None,
            "range": Range.from_dict(obj["range"]) if obj.get("range") is not None else None
        })
        return _obj


