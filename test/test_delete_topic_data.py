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

from trieve_python_client.models.delete_topic_data import DeleteTopicData

class TestDeleteTopicData(unittest.TestCase):
    """DeleteTopicData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteTopicData:
        """Test DeleteTopicData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteTopicData`
        """
        model = DeleteTopicData()
        if include_optional:
            return DeleteTopicData(
                topic_id = ''
            )
        else:
            return DeleteTopicData(
                topic_id = '',
        )
        """

    def testDeleteTopicData(self):
        """Test DeleteTopicData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
