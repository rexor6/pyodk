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
from pyodk.api.ovs_api import OVSApi  # noqa: E501
from pyodk.rest import ApiException


class TestOVSApi(unittest.TestCase):
    """OVSApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.ovs_api.OVSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_disks_attach_to_instance(self):
        """Test case for disks_attach_to_instance

        Attach disk to instance  # noqa: E501
        """
        pass

    def test_disks_change_subregion(self):
        """Test case for disks_change_subregion

        Change disk subregion  # noqa: E501
        """
        pass

    def test_disks_change_tier(self):
        """Test case for disks_change_tier

        Change disk tier  # noqa: E501
        """
        pass

    def test_disks_delete(self):
        """Test case for disks_delete

        Delete disk  # noqa: E501
        """
        pass

    def test_disks_detach_from_instance(self):
        """Test case for disks_detach_from_instance

        Detach disk from instance  # noqa: E501
        """
        pass

    def test_disks_extend(self):
        """Test case for disks_extend

        Extend disk  # noqa: E501
        """
        pass

    def test_disks_get(self):
        """Test case for disks_get

        Returns disk by identifier  # noqa: E501
        """
        pass

    def test_disks_get_disks(self):
        """Test case for disks_get_disks

        Returns disk list  # noqa: E501
        """
        pass

    def test_disks_post(self):
        """Test case for disks_post

        Creates disk  # noqa: E501
        """
        pass

    def test_disks_put(self):
        """Test case for disks_put

        Update disk  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
