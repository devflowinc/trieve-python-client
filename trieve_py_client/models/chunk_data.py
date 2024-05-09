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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from trieve_py_client.models.geo_info import GeoInfo
from typing import Optional, Set
from typing_extensions import Self

class ChunkData(BaseModel):
    """
    ChunkData
    """ # noqa: E501
    chunk_html: StrictStr = Field(description="HTML content of the chunk. This can also be plaintext. The innerText of the HTML will be used to create the embedding vector. The point of using HTML is for convienience, as some users have applications where users submit HTML content.")
    chunk_vector: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="Chunk_vector is a vector of floats which can be used instead of generating a new embedding. This is useful for when you are using a pre-embedded dataset. If this is not provided, the innerText of the chunk_html will be used to create the embedding.")
    convert_html_to_text: Optional[StrictBool] = Field(default=None, description="Convert HTML to raw text before processing to avoid adding noise to the vector embeddings. By default this is true. If you are using HTML content that you want to be included in the vector embeddings, set this to false.")
    group_ids: Optional[List[StrictStr]] = Field(default=None, description="Group ids are the ids of the groups that the chunk should be placed into. This is useful for when you want to create a chunk and add it to a group or multiple groups in one request. Necessary because this route queues the chunk for ingestion and the chunk may not exist yet immediately after response.")
    group_tracking_ids: Optional[List[StrictStr]] = Field(default=None, description="Group tracking_ids are the tracking_ids of the groups that the chunk should be placed into. This is useful for when you want to create a chunk and add it to a group or multiple groups in one request. Necessary because this route queues the chunk for ingestion and the chunk may not exist yet immediately after response.")
    link: Optional[StrictStr] = Field(default=None, description="Link to the chunk. This can also be any string. Frequently, this is a link to the source of the chunk. The link value will not affect the embedding creation.")
    location: Optional[GeoInfo] = None
    metadata: Optional[Any] = Field(default=None, description="Metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata.")
    split_avg: Optional[StrictBool] = Field(default=None, description="Split avg is a boolean which tells the server to split the text in the chunk_html into smaller chunks and average their resulting vectors. This is useful for when you want to create a chunk from a large piece of text and want to split it into smaller chunks to create a more fuzzy average dense vector. The sparse vector will be generated normally with no averaging. By default this is false.")
    tag_set: Optional[List[StrictStr]] = Field(default=None, description="Tag set is a list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them.")
    time_stamp: Optional[StrictStr] = Field(default=None, description="Time_stamp should be an ISO 8601 combined date and time without timezone. It is used for time window filtering and recency-biasing search results.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="Tracking_id is a string which can be used to identify a chunk. This is useful for when you are coordinating with an external system and want to use the tracking_id to identify the chunk.")
    upsert_by_tracking_id: Optional[StrictBool] = Field(default=None, description="Upsert when a chunk with the same tracking_id exists. By default this is false, and the request will fail if a chunk with the same tracking_id exists. If this is true, the chunk will be updated if a chunk with the same tracking_id exists.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Weight is a float which can be used to bias search results. This is useful for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the chunk's dataset dataset.")
    __properties: ClassVar[List[str]] = ["chunk_html", "chunk_vector", "convert_html_to_text", "group_ids", "group_tracking_ids", "link", "location", "metadata", "split_avg", "tag_set", "time_stamp", "tracking_id", "upsert_by_tracking_id", "weight"]

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
        """Create an instance of ChunkData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if chunk_vector (nullable) is None
        # and model_fields_set contains the field
        if self.chunk_vector is None and "chunk_vector" in self.model_fields_set:
            _dict['chunk_vector'] = None

        # set to None if convert_html_to_text (nullable) is None
        # and model_fields_set contains the field
        if self.convert_html_to_text is None and "convert_html_to_text" in self.model_fields_set:
            _dict['convert_html_to_text'] = None

        # set to None if group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.group_ids is None and "group_ids" in self.model_fields_set:
            _dict['group_ids'] = None

        # set to None if group_tracking_ids (nullable) is None
        # and model_fields_set contains the field
        if self.group_tracking_ids is None and "group_tracking_ids" in self.model_fields_set:
            _dict['group_tracking_ids'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if split_avg (nullable) is None
        # and model_fields_set contains the field
        if self.split_avg is None and "split_avg" in self.model_fields_set:
            _dict['split_avg'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        # set to None if time_stamp (nullable) is None
        # and model_fields_set contains the field
        if self.time_stamp is None and "time_stamp" in self.model_fields_set:
            _dict['time_stamp'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        # set to None if upsert_by_tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.upsert_by_tracking_id is None and "upsert_by_tracking_id" in self.model_fields_set:
            _dict['upsert_by_tracking_id'] = None

        # set to None if weight (nullable) is None
        # and model_fields_set contains the field
        if self.weight is None and "weight" in self.model_fields_set:
            _dict['weight'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChunkData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chunk_html": obj.get("chunk_html"),
            "chunk_vector": obj.get("chunk_vector"),
            "convert_html_to_text": obj.get("convert_html_to_text"),
            "group_ids": obj.get("group_ids"),
            "group_tracking_ids": obj.get("group_tracking_ids"),
            "link": obj.get("link"),
            "location": GeoInfo.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "metadata": obj.get("metadata"),
            "split_avg": obj.get("split_avg"),
            "tag_set": obj.get("tag_set"),
            "time_stamp": obj.get("time_stamp"),
            "tracking_id": obj.get("tracking_id"),
            "upsert_by_tracking_id": obj.get("upsert_by_tracking_id"),
            "weight": obj.get("weight")
        })
        return _obj


