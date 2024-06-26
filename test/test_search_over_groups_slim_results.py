# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.6.2
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.search_over_groups_slim_results import SearchOverGroupsSlimResults

class TestSearchOverGroupsSlimResults(unittest.TestCase):
    """SearchOverGroupsSlimResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchOverGroupsSlimResults:
        """Test SearchOverGroupsSlimResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchOverGroupsSlimResults`
        """
        model = SearchOverGroupsSlimResults()
        if include_optional:
            return SearchOverGroupsSlimResults(
                group_chunks = [
                    {"group_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","metadata":[{"metadata":[{"created_at":"2021-01-01T00:00:00","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}],"score":0.5}]}
                    ],
                total_chunk_pages = 56
            )
        else:
            return SearchOverGroupsSlimResults(
                group_chunks = [
                    {"group_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","metadata":[{"metadata":[{"created_at":"2021-01-01T00:00:00","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}],"score":0.5}]}
                    ],
                total_chunk_pages = 56,
        )
        """

    def testSearchOverGroupsSlimResults(self):
        """Test SearchOverGroupsSlimResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
