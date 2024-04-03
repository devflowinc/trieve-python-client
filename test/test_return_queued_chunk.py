# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.5.7
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.return_queued_chunk import ReturnQueuedChunk

class TestReturnQueuedChunk(unittest.TestCase):
    """ReturnQueuedChunk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnQueuedChunk:
        """Test ReturnQueuedChunk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnQueuedChunk`
        """
        model = ReturnQueuedChunk()
        if include_optional:
            return ReturnQueuedChunk(
                chunk_metadata = [
                    {"chunk_html":"<p>Hello, world!</p>","content":"Hello, world!","created_at":"2021-01-01T00:00:00","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}
                    ],
                pos_in_queue = 56
            )
        else:
            return ReturnQueuedChunk(
                chunk_metadata = [
                    {"chunk_html":"<p>Hello, world!</p>","content":"Hello, world!","created_at":"2021-01-01T00:00:00","dataset_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","link":"https://trieve.ai","metadata":{"key":"value"},"qdrant_point_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","tag_set":"tag1,tag2","time_stamp":"2021-01-01T00:00:00","tracking_id":"e3e3e3e3-e3e3-e3e3-e3e3-e3e3e3e3e3e3","updated_at":"2021-01-01T00:00:00","weight":0.5}
                    ],
                pos_in_queue = 56,
        )
        """

    def testReturnQueuedChunk(self):
        """Test ReturnQueuedChunk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
