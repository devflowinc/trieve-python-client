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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UploadFileData(BaseModel):
    """
    UploadFileData
    """ # noqa: E501
    base64_file: StrictStr = Field(description="Base64 encoded file. Convert + to -, / to _, and remove the ending = if present. This is the standard base64url encoding.")
    create_chunks: Optional[StrictBool] = Field(default=None, description="Create chunks is a boolean which determines whether or not to create chunks from the file. If false, you can manually chunk the file and send the chunks to the create_chunk endpoint with the file_id to associate chunks with the file. Meant mostly for advanced users.")
    description: Optional[StrictStr] = Field(default=None, description="Description is an optional convience field so you do not have to remember what the file contains or is about. It will be included on the group resulting from the file which will hold its chunk.")
    file_mime_type: StrictStr = Field(description="MIME type of the file being uploaded.")
    file_name: StrictStr = Field(description="Name of the file being uploaded, including the extension.")
    link: Optional[StrictStr] = Field(default=None, description="Link to the file. This can also be any string. This can be used to filter when searching for the file's resulting chunks. The link value will not affect embedding creation.")
    metadata: Optional[Any] = Field(default=None, description="Metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. Will be passed down to the file's chunks.")
    tag_set: Optional[List[StrictStr]] = Field(default=None, description="Tag set is a comma separated list of tags which will be passed down to the chunks made from the file. Tags are used to filter chunks when searching. HNSW indices are created for each tag such that there is no performance loss when filtering on them.")
    time_stamp: Optional[StrictStr] = Field(default=None, description="Time stamp should be an ISO 8601 combined date and time without timezone. Time_stamp is used for time window filtering and recency-biasing search results. Will be passed down to the file's chunks.")
    __properties: ClassVar[List[str]] = ["base64_file", "create_chunks", "description", "file_mime_type", "file_name", "link", "metadata", "tag_set", "time_stamp"]

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
        """Create an instance of UploadFileData from a JSON string"""
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
        # set to None if create_chunks (nullable) is None
        # and model_fields_set contains the field
        if self.create_chunks is None and "create_chunks" in self.model_fields_set:
            _dict['create_chunks'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        # set to None if time_stamp (nullable) is None
        # and model_fields_set contains the field
        if self.time_stamp is None and "time_stamp" in self.model_fields_set:
            _dict['time_stamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UploadFileData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "base64_file": obj.get("base64_file"),
            "create_chunks": obj.get("create_chunks"),
            "description": obj.get("description"),
            "file_mime_type": obj.get("file_mime_type"),
            "file_name": obj.get("file_name"),
            "link": obj.get("link"),
            "metadata": obj.get("metadata"),
            "tag_set": obj.get("tag_set"),
            "time_stamp": obj.get("time_stamp")
        })
        return _obj


