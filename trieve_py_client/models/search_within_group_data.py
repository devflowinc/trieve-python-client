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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from trieve_py_client.models.chunk_filter import ChunkFilter
from typing import Optional, Set
from typing_extensions import Self

class SearchWithinGroupData(BaseModel):
    """
    SearchWithinGroupData
    """ # noqa: E501
    filters: Optional[ChunkFilter] = None
    get_total_pages: Optional[StrictBool] = Field(default=None, description="Get total page count for the query accounting for the applied filters. Defaults to false, but can be set to true when the latency penalty is acceptable (typically 50-200ms).")
    group_id: Optional[StrictStr] = Field(default=None, description="Group specifies the group to search within. Results will only consist of chunks which are bookmarks within the specified group.")
    group_tracking_id: Optional[StrictStr] = Field(default=None, description="Group_tracking_id specifies the group to search within by tracking id. Results will only consist of chunks which are bookmarks within the specified group. If both group_id and group_tracking_id are provided, group_id will be used.")
    highlight_delimiters: Optional[List[StrictStr]] = Field(default=None, description="Set highlight_delimiters to a list of strings to use as delimiters for highlighting. If not specified, this defaults to [\"?\", \",\", \".\", \"!\"].")
    highlight_results: Optional[StrictBool] = Field(default=None, description="Set highlight_results to false for a slight latency improvement (1-10ms). If not specified, this defaults to true. This will add `<b><mark>` tags to the chunk_html of the chunks to highlight matching sub-sentences.")
    highlight_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set highlight_threshold to a lower or higher value to adjust the sensitivity of the highlights applied to the chunk html. If not specified, this defaults to 0.8. The range is 0.0 to 1.0.")
    page: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The page of chunks to fetch. Page is 1-indexed.")
    page_size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The page size is the number of chunks to fetch. This can be used to fetch more than 10 chunks at a time.")
    query: StrictStr = Field(description="The query is the search query. This can be any string. The query will be used to create an embedding vector and/or SPLADE vector which will be used to find the result set.")
    recency_bias: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Recency Bias lets you determine how much of an effect the recency of chunks will have on the search results. If not specified, this defaults to 0.0.")
    score_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set score_threshold to a float to filter out chunks with a score below the threshold.")
    search_type: StrictStr = Field(description="Search_type can be either \"semantic\", \"fulltext\", or \"hybrid\". \"hybrid\" will pull in one page (10 chunks) of both semantic and full-text results then re-rank them using BAAI/bge-reranker-large. \"semantic\" will pull in one page (10 chunks) of the nearest cosine distant vectors. \"fulltext\" will pull in one page (10 chunks) of full-text results based on SPLADE.")
    slim_chunks: Optional[StrictBool] = Field(default=None, description="Set slim_chunks to true to avoid returning the content and chunk_html of the chunks. This is useful for when you want to reduce amount of data over the wire for latency improvement (typicall 10-50ms). Default is false.")
    tag_weights: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="Tag weights is a JSON object which can be used to boost the ranking of chunks with certain tags. This is useful for when you want to be able to bias towards chunks with a certain tag on the fly. The keys are the tag names and the values are the weights.")
    use_weights: Optional[StrictBool] = Field(default=None, description="Set use_weights to true to use the weights of the chunks in the result set in order to sort them. If not specified, this defaults to true.")
    __properties: ClassVar[List[str]] = ["filters", "get_total_pages", "group_id", "group_tracking_id", "highlight_delimiters", "highlight_results", "highlight_threshold", "page", "page_size", "query", "recency_bias", "score_threshold", "search_type", "slim_chunks", "tag_weights", "use_weights"]

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
        """Create an instance of SearchWithinGroupData from a JSON string"""
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
        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if get_total_pages (nullable) is None
        # and model_fields_set contains the field
        if self.get_total_pages is None and "get_total_pages" in self.model_fields_set:
            _dict['get_total_pages'] = None

        # set to None if group_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_id is None and "group_id" in self.model_fields_set:
            _dict['group_id'] = None

        # set to None if group_tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_tracking_id is None and "group_tracking_id" in self.model_fields_set:
            _dict['group_tracking_id'] = None

        # set to None if highlight_delimiters (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_delimiters is None and "highlight_delimiters" in self.model_fields_set:
            _dict['highlight_delimiters'] = None

        # set to None if highlight_results (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_results is None and "highlight_results" in self.model_fields_set:
            _dict['highlight_results'] = None

        # set to None if highlight_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_threshold is None and "highlight_threshold" in self.model_fields_set:
            _dict['highlight_threshold'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['page_size'] = None

        # set to None if recency_bias (nullable) is None
        # and model_fields_set contains the field
        if self.recency_bias is None and "recency_bias" in self.model_fields_set:
            _dict['recency_bias'] = None

        # set to None if score_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.score_threshold is None and "score_threshold" in self.model_fields_set:
            _dict['score_threshold'] = None

        # set to None if slim_chunks (nullable) is None
        # and model_fields_set contains the field
        if self.slim_chunks is None and "slim_chunks" in self.model_fields_set:
            _dict['slim_chunks'] = None

        # set to None if tag_weights (nullable) is None
        # and model_fields_set contains the field
        if self.tag_weights is None and "tag_weights" in self.model_fields_set:
            _dict['tag_weights'] = None

        # set to None if use_weights (nullable) is None
        # and model_fields_set contains the field
        if self.use_weights is None and "use_weights" in self.model_fields_set:
            _dict['use_weights'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchWithinGroupData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filters": ChunkFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "get_total_pages": obj.get("get_total_pages"),
            "group_id": obj.get("group_id"),
            "group_tracking_id": obj.get("group_tracking_id"),
            "highlight_delimiters": obj.get("highlight_delimiters"),
            "highlight_results": obj.get("highlight_results"),
            "highlight_threshold": obj.get("highlight_threshold"),
            "page": obj.get("page"),
            "page_size": obj.get("page_size"),
            "query": obj.get("query"),
            "recency_bias": obj.get("recency_bias"),
            "score_threshold": obj.get("score_threshold"),
            "search_type": obj.get("search_type"),
            "slim_chunks": obj.get("slim_chunks"),
            "tag_weights": obj.get("tag_weights"),
            "use_weights": obj.get("use_weights")
        })
        return _obj


