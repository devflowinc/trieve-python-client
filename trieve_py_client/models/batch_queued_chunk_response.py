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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List
from trieve_py_client.models.chunk_metadata import ChunkMetadata
from typing import Optional, Set
from typing_extensions import Self

class BatchQueuedChunkResponse(BaseModel):
    """
    BatchQueuedChunkResponse
    """ # noqa: E501
    chunk_metadata: List[ChunkMetadata]
    pos_in_queue: StrictInt = Field(description="The current position the last access item is in the queue")
    __properties: ClassVar[List[str]] = ["chunk_metadata", "pos_in_queue"]

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
        """Create an instance of BatchQueuedChunkResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in chunk_metadata (list)
        _items = []
        if self.chunk_metadata:
            for _item in self.chunk_metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['chunk_metadata'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchQueuedChunkResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chunk_metadata": [ChunkMetadata.from_dict(_item) for _item in obj["chunk_metadata"]] if obj.get("chunk_metadata") is not None else None,
            "pos_in_queue": obj.get("pos_in_queue")
        })
        return _obj


