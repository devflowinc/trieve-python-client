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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RegenerateMessageData(BaseModel):
    """
    RegenerateMessageData
    """ # noqa: E501
    highlight_citations: Optional[StrictBool] = Field(default=None, description="Whether or not to highlight the citations in the response. If this is set to true or not included, the citations will be highlighted. If this is set to false, the citations will not be highlighted. Default is true.")
    highlight_delimiters: Optional[List[StrictStr]] = Field(default=None, description="The delimiters to use for highlighting the citations. If this is not included, the default delimiters will be used. Default is `[\".\", \"!\", \"?\", \"\\n\", \"\\t\", \",\"]`.")
    model: Optional[StrictStr] = Field(default=None, description="The model to use for the assistant generative inferences. This can be any model from the openrouter model list. If no model is provided, the gpt-3.5-turbo will be used.~")
    stream_response: Optional[StrictBool] = Field(default=None, description="Whether or not to stream the response. If this is set to true or not included, the response will be a stream. If this is set to false, the response will be a normal JSON response. Default is true.")
    topic_id: StrictStr = Field(description="The id of the topic to regenerate the last message for.")
    __properties: ClassVar[List[str]] = ["highlight_citations", "highlight_delimiters", "model", "stream_response", "topic_id"]

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
        """Create an instance of RegenerateMessageData from a JSON string"""
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
        # set to None if highlight_citations (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_citations is None and "highlight_citations" in self.model_fields_set:
            _dict['highlight_citations'] = None

        # set to None if highlight_delimiters (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_delimiters is None and "highlight_delimiters" in self.model_fields_set:
            _dict['highlight_delimiters'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if stream_response (nullable) is None
        # and model_fields_set contains the field
        if self.stream_response is None and "stream_response" in self.model_fields_set:
            _dict['stream_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegenerateMessageData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "highlight_citations": obj.get("highlight_citations"),
            "highlight_delimiters": obj.get("highlight_delimiters"),
            "model": obj.get("model"),
            "stream_response": obj.get("stream_response"),
            "topic_id": obj.get("topic_id")
        })
        return _obj


