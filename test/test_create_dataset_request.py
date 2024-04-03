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

from trieve_py_client.models.create_dataset_request import CreateDatasetRequest

class TestCreateDatasetRequest(unittest.TestCase):
    """CreateDatasetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateDatasetRequest:
        """Test CreateDatasetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateDatasetRequest`
        """
        model = CreateDatasetRequest()
        if include_optional:
            return CreateDatasetRequest(
                client_configuration = None,
                dataset_name = '',
                organization_id = '',
                server_configuration = None
            )
        else:
            return CreateDatasetRequest(
                client_configuration = None,
                dataset_name = '',
                organization_id = '',
                server_configuration = None,
        )
        """

    def testCreateDatasetRequest(self):
        """Test CreateDatasetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
