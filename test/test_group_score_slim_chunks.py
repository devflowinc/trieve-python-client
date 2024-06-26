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

from trieve_py_client.models.group_score_slim_chunks import GroupScoreSlimChunks

class TestGroupScoreSlimChunks(unittest.TestCase):
    """GroupScoreSlimChunks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GroupScoreSlimChunks:
        """Test GroupScoreSlimChunks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GroupScoreSlimChunks`
        """
        model = GroupScoreSlimChunks()
        if include_optional:
            return GroupScoreSlimChunks(
                group_id = '',
                metadata = [
                    {"metadata":[{"created_at":"2021-01-01T00:00:00","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}],"score":0.5}
                    ]
            )
        else:
            return GroupScoreSlimChunks(
                group_id = '',
                metadata = [
                    {"metadata":[{"created_at":"2021-01-01T00:00:00","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}],"score":0.5}
                    ],
        )
        """

    def testGroupScoreSlimChunks(self):
        """Test GroupScoreSlimChunks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
