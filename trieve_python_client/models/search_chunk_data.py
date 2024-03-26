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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from trieve_python_client.models.chunk_filter import ChunkFilter
from typing import Optional, Set
from typing_extensions import Self

class SearchChunkData(BaseModel):
    """
    SearchChunkData
    """ # noqa: E501
    date_bias: Optional[StrictBool] = Field(default=None, description="Set date_bias to true to bias search results towards more recent chunks. This will work best in hybrid search mode.")
    filters: Optional[ChunkFilter] = None
    get_collisions: Optional[StrictBool] = Field(default=None, description="Set get_collisions to true to get the collisions for each chunk. This will only apply if environment variable COLLISIONS_ENABLED is set to true.")
    highlight_delimiters: Optional[List[StrictStr]] = Field(default=None, description="Set highlight_delimiters to a list of strings to use as delimiters for highlighting. If not specified, this defaults to [\"?\", \",\", \".\", \"!\"].")
    highlight_results: Optional[StrictBool] = Field(default=None, description="Set highlight_results to true to highlight the results. If not specified, this defaults to true.")
    page: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Page of chunks to fetch. Each page is 10 chunks. Support for custom page size is coming soon.")
    page_size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Page size is the number of chunks to fetch. This can be used to fetch more than 10 chunks at a time.")
    query: StrictStr = Field(description="Query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set.")
    score_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set score_threshold to a float to filter out chunks with a score below the threshold.")
    search_type: StrictStr = Field(description="Can be either \"semantic\", \"fulltext\", or \"hybrid\". \"hybrid\" will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \"semantic\" will pull in one page (10 chunks) of the nearest cosine distant vectors. \"fulltext\" will pull in one page (10 chunks) of full-text results based on SPLADE.")
    use_weights: Optional[StrictBool] = Field(default=None, description="Set use_weights to true to use the weights of the chunks in the result set in order to sort them. If not specified, this defaults to true.")
    __properties: ClassVar[List[str]] = ["date_bias", "filters", "get_collisions", "highlight_delimiters", "highlight_results", "page", "page_size", "query", "score_threshold", "search_type", "use_weights"]

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
        """Create an instance of SearchChunkData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # set to None if date_bias (nullable) is None
        # and model_fields_set contains the field
        if self.date_bias is None and "date_bias" in self.model_fields_set:
            _dict['date_bias'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if get_collisions (nullable) is None
        # and model_fields_set contains the field
        if self.get_collisions is None and "get_collisions" in self.model_fields_set:
            _dict['get_collisions'] = None

        # set to None if highlight_delimiters (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_delimiters is None and "highlight_delimiters" in self.model_fields_set:
            _dict['highlight_delimiters'] = None

        # set to None if highlight_results (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_results is None and "highlight_results" in self.model_fields_set:
            _dict['highlight_results'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['page_size'] = None

        # set to None if score_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.score_threshold is None and "score_threshold" in self.model_fields_set:
            _dict['score_threshold'] = None

        # set to None if use_weights (nullable) is None
        # and model_fields_set contains the field
        if self.use_weights is None and "use_weights" in self.model_fields_set:
            _dict['use_weights'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchChunkData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date_bias": obj.get("date_bias"),
            "filters": ChunkFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "get_collisions": obj.get("get_collisions"),
            "highlight_delimiters": obj.get("highlight_delimiters"),
            "highlight_results": obj.get("highlight_results"),
            "page": obj.get("page"),
            "page_size": obj.get("page_size"),
            "query": obj.get("query"),
            "score_threshold": obj.get("score_threshold"),
            "search_type": obj.get("search_type"),
            "use_weights": obj.get("use_weights")
        })
        return _obj


