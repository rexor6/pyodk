# coding: utf-8

"""
    Oktawave API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyodk
from pyodk.api.tickets_api import TicketsApi  # noqa: E501
from pyodk.rest import ApiException


class TestTicketsApi(unittest.TestCase):
    """TicketsApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.tickets_api.TicketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tickets_get(self):
        """Test case for tickets_get

        Returns ticket collection  # noqa: E501
        """
        pass

    def test_tickets_get_0(self):
        """Test case for tickets_get_0

        Returns ticket by identifier  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
