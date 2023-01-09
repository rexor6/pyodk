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
from pyodk.api.oci_schedulers_api import OCISchedulersApi  # noqa: E501
from pyodk.rest import ApiException


class TestOCISchedulersApi(unittest.TestCase):
    """OCISchedulersApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.oci_schedulers_api.OCISchedulersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_instance_schedulers_delete(self):
        """Test case for instance_schedulers_delete

        Deletes instance scheduler  # noqa: E501
        """
        pass

    def test_instance_schedulers_get(self):
        """Test case for instance_schedulers_get

        Gets scheduler by identifier  # noqa: E501
        """
        pass

    def test_instance_schedulers_get_instance_schedulers(self):
        """Test case for instance_schedulers_get_instance_schedulers

        Gets instance schedulers  # noqa: E501
        """
        pass

    def test_instance_schedulers_post(self):
        """Test case for instance_schedulers_post

        Creates instance scheduler  # noqa: E501
        """
        pass

    def test_instance_schedulers_put(self):
        """Test case for instance_schedulers_put

        Updates instance scheduler  # noqa: E501
        """
        pass

    def test_instances_get_schedulers(self):
        """Test case for instances_get_schedulers

        Gets schedulers by search params  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
