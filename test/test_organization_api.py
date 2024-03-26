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

from trieve_python_client.api.organization_api import OrganizationApi


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        Create Organization
        """
        pass

    def test_delete_organization_by_id(self) -> None:
        """Test case for delete_organization_by_id

        Delete Organization
        """
        pass

    def test_get_organization_by_id(self) -> None:
        """Test case for get_organization_by_id

        Get Organization
        """
        pass

    def test_get_organization_usage(self) -> None:
        """Test case for get_organization_usage

        Get Organization Usage
        """
        pass

    def test_get_organization_users(self) -> None:
        """Test case for get_organization_users

        Get Organization Users
        """
        pass

    def test_update_organization(self) -> None:
        """Test case for update_organization

        Update Organization
        """
        pass


if __name__ == '__main__':
    unittest.main()