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
from pyodk.api.account_api import AccountApi  # noqa: E501
from pyodk.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_delete_ssh_key(self):
        """Test case for account_delete_ssh_key

        Deletes SSH key  # noqa: E501
        """
        pass

    def test_account_get(self):
        """Test case for account_get

        Returns account details  # noqa: E501
        """
        pass

    def test_account_get_ssh_key(self):
        """Test case for account_get_ssh_key

        Returns SSH key  # noqa: E501
        """
        pass

    def test_account_get_ssh_keys(self):
        """Test case for account_get_ssh_keys

        Returns SSH keys  # noqa: E501
        """
        pass

    def test_account_post_ssh_key(self):
        """Test case for account_post_ssh_key

        Creates new SSH key for user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()