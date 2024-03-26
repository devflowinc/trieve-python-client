# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.5.0
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_python_client.models.search_within_group_data import SearchWithinGroupData

class TestSearchWithinGroupData(unittest.TestCase):
    """SearchWithinGroupData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchWithinGroupData:
        """Test SearchWithinGroupData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchWithinGroupData`
        """
        model = SearchWithinGroupData()
        if include_optional:
            return SearchWithinGroupData(
                date_bias = True,
                filters = {"must":[{"field":"metadata.key2","match":["value3","value4"],"range":{"gt":0,"gte":0,"lt":1,"lte":1}}],"must_not":[{"field":"metadata.key3","match":["value5","value6"],"range":{"gt":0,"gte":0,"lt":1,"lte":1}}],"should":[{"field":"metadata.key1","match":["value1","value2"],"range":{"gt":0,"gte":0,"lt":1,"lte":1}}]},
                group_id = '',
                group_tracking_id = '',
                highlight_delimiters = [
                    ''
                    ],
                highlight_results = True,
                page = 0,
                page_size = 0,
                query = '',
                score_threshold = 1.337,
                search_type = '',
                use_weights = True
            )
        else:
            return SearchWithinGroupData(
                query = '',
                search_type = '',
        )
        """

    def testSearchWithinGroupData(self):
        """Test SearchWithinGroupData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
