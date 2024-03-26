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

from trieve_python_client.models.create_chunk_data import CreateChunkData

class TestCreateChunkData(unittest.TestCase):
    """CreateChunkData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateChunkData:
        """Test CreateChunkData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateChunkData`
        """
        model = CreateChunkData()
        if include_optional:
            return CreateChunkData(
                chunk_html = '',
                chunk_vector = [
                    1.337
                    ],
                file_id = '',
                group_ids = [
                    ''
                    ],
                group_tracking_ids = [
                    ''
                    ],
                link = '',
                metadata = None,
                split_avg = True,
                tag_set = [
                    ''
                    ],
                time_stamp = '',
                tracking_id = '',
                upsert_by_tracking_id = True,
                weight = 1.337
            )
        else:
            return CreateChunkData(
        )
        """

    def testCreateChunkData(self):
        """Test CreateChunkData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
