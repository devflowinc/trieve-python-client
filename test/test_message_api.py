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

from trieve_python_client.api.message_api import MessageApi


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MessageApi()

    def tearDown(self) -> None:
        pass

    def test_create_message_completion_handler(self) -> None:
        """Test case for create_message_completion_handler

        Create a message
        """
        pass

    def test_edit_message_handler(self) -> None:
        """Test case for edit_message_handler

        Edit a message
        """
        pass

    def test_get_all_topic_messages(self) -> None:
        """Test case for get_all_topic_messages

        Get all messages for a given topic
        """
        pass

    def test_regenerate_message_handler(self) -> None:
        """Test case for regenerate_message_handler

        Regenerate message
        """
        pass


if __name__ == '__main__':
    unittest.main()
