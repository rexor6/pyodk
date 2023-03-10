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
from pyodk.api.oci_groups_api import OCIGroupsApi  # noqa: E501
from pyodk.rest import ApiException


class TestOCIGroupsApi(unittest.TestCase):
    """OCIGroupsApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.oci_groups_api.OCIGroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_groups_change_assignments_in_group(self):
        """Test case for groups_change_assignments_in_group

        Changes group assignments  # noqa: E501
        """
        pass

    def test_groups_create(self):
        """Test case for groups_create

        Creates group  # noqa: E501
        """
        pass

    def test_groups_create_container_scheduler(self):
        """Test case for groups_create_container_scheduler

        Creates a group scheduler  # noqa: E501
        """
        pass

    def test_groups_delete(self):
        """Test case for groups_delete

        Deletes group  # noqa: E501
        """
        pass

    def test_groups_delete_group_scheduler(self):
        """Test case for groups_delete_group_scheduler

        Deletes group scheduler  # noqa: E501
        """
        pass

    def test_groups_get_assignments_in_group(self):
        """Test case for groups_get_assignments_in_group

        Returns group assignments  # noqa: E501
        """
        pass

    def test_groups_get_group(self):
        """Test case for groups_get_group

        Returns group  # noqa: E501
        """
        pass

    def test_groups_get_group_autoscaler(self):
        """Test case for groups_get_group_autoscaler

        Returns group autoscaler settings  # noqa: E501
        """
        pass

    def test_groups_get_group_scheduler(self):
        """Test case for groups_get_group_scheduler

        Returns group scheduler  # noqa: E501
        """
        pass

    def test_groups_get_group_schedulers(self):
        """Test case for groups_get_group_schedulers

        Returns group schedulers  # noqa: E501
        """
        pass

    def test_groups_get_groups(self):
        """Test case for groups_get_groups

        Returns a list of groups  # noqa: E501
        """
        pass

    def test_groups_get_load_balancers(self):
        """Test case for groups_get_load_balancers

        Gets load balancers  # noqa: E501
        """
        pass

    def test_groups_set_group_autoscaler(self):
        """Test case for groups_set_group_autoscaler

        Sets group autoscaler  # noqa: E501
        """
        pass

    def test_groups_turnoff_group_autoscaler(self):
        """Test case for groups_turnoff_group_autoscaler

        Turns off group autoscaler  # noqa: E501
        """
        pass

    def test_groups_update(self):
        """Test case for groups_update

        Updates group  # noqa: E501
        """
        pass

    def test_groups_update_group_scheduler(self):
        """Test case for groups_update_group_scheduler

        Updates a group scheduler  # noqa: E501
        """
        pass

    def test_instances_get_groups(self):
        """Test case for instances_get_groups

        Returns a list of instance groups  # noqa: E501
        """
        pass

    def test_load_balancers_change_service_status(self):
        """Test case for load_balancers_change_service_status

        Changes load balancer service state  # noqa: E501
        """
        pass

    def test_load_balancers_create(self):
        """Test case for load_balancers_create

        Create load balancer for group  # noqa: E501
        """
        pass

    def test_load_balancers_delete(self):
        """Test case for load_balancers_delete

        Delete load balancer  # noqa: E501
        """
        pass

    def test_load_balancers_get_load_balancer(self):
        """Test case for load_balancers_get_load_balancer

        Gets load balancer for group  # noqa: E501
        """
        pass

    def test_load_balancers_get_load_balancer_details(self):
        """Test case for load_balancers_get_load_balancer_details

        Gets load balancer detail for group  # noqa: E501
        """
        pass

    def test_load_balancers_update(self):
        """Test case for load_balancers_update

        Update load balancer for group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
