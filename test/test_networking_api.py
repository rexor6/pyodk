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
from pyodk.api.networking_api import NetworkingApi  # noqa: E501
from pyodk.rest import ApiException


class TestNetworkingApi(unittest.TestCase):
    """NetworkingApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.networking_api.NetworkingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_opns_delete(self):
        """Test case for opns_delete

        Deletes an OPN  # noqa: E501
        """
        pass

    def test_opns_get(self):
        """Test case for opns_get

        Returns OPNs  # noqa: E501
        """
        pass

    def test_opns_post(self):
        """Test case for opns_post

        Creates an OPN  # noqa: E501
        """
        pass

    def test_opns_put(self):
        """Test case for opns_put

        Updates OPN  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()