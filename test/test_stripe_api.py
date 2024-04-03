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

from trieve_py_client.api.stripe_api import StripeApi


class TestStripeApi(unittest.TestCase):
    """StripeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StripeApi()

    def tearDown(self) -> None:
        pass

    def test_cancel_subscription(self) -> None:
        """Test case for cancel_subscription

        Cancel Subscription
        """
        pass

    def test_direct_to_payment_link(self) -> None:
        """Test case for direct_to_payment_link

        Checkout
        """
        pass

    def test_get_all_plans(self) -> None:
        """Test case for get_all_plans

        Get All Plans
        """
        pass

    def test_update_subscription_plan(self) -> None:
        """Test case for update_subscription_plan

        Update Subscription Plan
        """
        pass


if __name__ == '__main__':
    unittest.main()
