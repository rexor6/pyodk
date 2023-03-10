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
from pyodk.api.watch_api import WatchApi  # noqa: E501
from pyodk.rest import ApiException


class TestWatchApi(unittest.TestCase):
    """WatchApi unit test stubs"""

    def setUp(self):
        self.api = pyodk.api.watch_api.WatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_watch_add_selected_monitoring_stations(self):
        """Test case for watch_add_selected_monitoring_stations

        Add monitoring sensor  # noqa: E501
        """
        pass

    def test_watch_create_dns_health_check(self):
        """Test case for watch_create_dns_health_check

        Creates dns health check  # noqa: E501
        """
        pass

    def test_watch_create_full_page_health_check(self):
        """Test case for watch_create_full_page_health_check

        Creates FullPage health check  # noqa: E501
        """
        pass

    def test_watch_create_full_page_https_health_check(self):
        """Test case for watch_create_full_page_https_health_check

        Creates FullPage Https health check  # noqa: E501
        """
        pass

    def test_watch_create_health_check_notification(self):
        """Test case for watch_create_health_check_notification

        Creates health check notification  # noqa: E501
        """
        pass

    def test_watch_create_http_health_check(self):
        """Test case for watch_create_http_health_check

        Creates http health check  # noqa: E501
        """
        pass

    def test_watch_create_https_health_check(self):
        """Test case for watch_create_https_health_check

        Creates https health check  # noqa: E501
        """
        pass

    def test_watch_create_imap_health_check(self):
        """Test case for watch_create_imap_health_check

        Creates imap health check  # noqa: E501
        """
        pass

    def test_watch_create_imap_ssl_health_check(self):
        """Test case for watch_create_imap_ssl_health_check

        Creates imap ssl health check  # noqa: E501
        """
        pass

    def test_watch_create_ping_health_check(self):
        """Test case for watch_create_ping_health_check

        Creates ping health check  # noqa: E501
        """
        pass

    def test_watch_create_sip_health_check(self):
        """Test case for watch_create_sip_health_check

        Creates sip health check  # noqa: E501
        """
        pass

    def test_watch_create_smtp_health_check(self):
        """Test case for watch_create_smtp_health_check

        Creates smtp health check  # noqa: E501
        """
        pass

    def test_watch_create_tcp_health_check(self):
        """Test case for watch_create_tcp_health_check

        Creates Tcp health check  # noqa: E501
        """
        pass

    def test_watch_delete_health_check(self):
        """Test case for watch_delete_health_check

        Deletes health check  # noqa: E501
        """
        pass

    def test_watch_delete_health_check_notification(self):
        """Test case for watch_delete_health_check_notification

        Deletes health check notification  # noqa: E501
        """
        pass

    def test_watch_delete_selected_monitoring_stations(self):
        """Test case for watch_delete_selected_monitoring_stations

        Remove monitoring sensor  # noqa: E501
        """
        pass

    def test_watch_get_available_monitoring_stations(self):
        """Test case for watch_get_available_monitoring_stations

        Gets all available monitoring sensors  # noqa: E501
        """
        pass

    def test_watch_get_dns_health_check(self):
        """Test case for watch_get_dns_health_check

        Returns dns health check details  # noqa: E501
        """
        pass

    def test_watch_get_full_page_health_check(self):
        """Test case for watch_get_full_page_health_check

        Returns FullPage health check details  # noqa: E501
        """
        pass

    def test_watch_get_full_page_https_health_check(self):
        """Test case for watch_get_full_page_https_health_check

        Returns FullPage Https health check details  # noqa: E501
        """
        pass

    def test_watch_get_health_check(self):
        """Test case for watch_get_health_check

        Returns health check  # noqa: E501
        """
        pass

    def test_watch_get_health_check_notification(self):
        """Test case for watch_get_health_check_notification

        Returns health check notification details  # noqa: E501
        """
        pass

    def test_watch_get_health_check_notifications(self):
        """Test case for watch_get_health_check_notifications

        Returns a list of configured health check notifications  # noqa: E501
        """
        pass

    def test_watch_get_health_checks(self):
        """Test case for watch_get_health_checks

        Returns a list of configured health checks  # noqa: E501
        """
        pass

    def test_watch_get_http_health_check(self):
        """Test case for watch_get_http_health_check

        Returns http health check details  # noqa: E501
        """
        pass

    def test_watch_get_https_health_check(self):
        """Test case for watch_get_https_health_check

        Returns https health check details  # noqa: E501
        """
        pass

    def test_watch_get_imap_health_check(self):
        """Test case for watch_get_imap_health_check

        Returns imap health check details  # noqa: E501
        """
        pass

    def test_watch_get_imap_ssl_health_check(self):
        """Test case for watch_get_imap_ssl_health_check

        Returns imap ssl health check details  # noqa: E501
        """
        pass

    def test_watch_get_ping_health_check(self):
        """Test case for watch_get_ping_health_check

        Returns ping health check details  # noqa: E501
        """
        pass

    def test_watch_get_selected_monitoring_station(self):
        """Test case for watch_get_selected_monitoring_station

        Gets selected monitoring sensor  # noqa: E501
        """
        pass

    def test_watch_get_selected_monitoring_stations(self):
        """Test case for watch_get_selected_monitoring_stations

        Gets selected monitoring sensors  # noqa: E501
        """
        pass

    def test_watch_get_sip_health_check(self):
        """Test case for watch_get_sip_health_check

        Returns sip health check details  # noqa: E501
        """
        pass

    def test_watch_get_smtp_health_check(self):
        """Test case for watch_get_smtp_health_check

        Returns smtp health check details  # noqa: E501
        """
        pass

    def test_watch_get_tcp_health_check(self):
        """Test case for watch_get_tcp_health_check

        Returns tcp health check details  # noqa: E501
        """
        pass

    def test_watch_update_dns_health_check(self):
        """Test case for watch_update_dns_health_check

        Updates dns health check  # noqa: E501
        """
        pass

    def test_watch_update_full_page_health_check(self):
        """Test case for watch_update_full_page_health_check

        Updates FullPage health check  # noqa: E501
        """
        pass

    def test_watch_update_full_page_https_health_check(self):
        """Test case for watch_update_full_page_https_health_check

        Updates FullPage Https health check  # noqa: E501
        """
        pass

    def test_watch_update_health_check_notification(self):
        """Test case for watch_update_health_check_notification

        Updates health check notification  # noqa: E501
        """
        pass

    def test_watch_update_http_health_check(self):
        """Test case for watch_update_http_health_check

        Updates http health check  # noqa: E501
        """
        pass

    def test_watch_update_https_health_check(self):
        """Test case for watch_update_https_health_check

        Updates https health check  # noqa: E501
        """
        pass

    def test_watch_update_imap_health_check(self):
        """Test case for watch_update_imap_health_check

        Updates imap health check  # noqa: E501
        """
        pass

    def test_watch_update_imap_health_check_0(self):
        """Test case for watch_update_imap_health_check_0

        Updates sip health check  # noqa: E501
        """
        pass

    def test_watch_update_imap_ssl_health_check(self):
        """Test case for watch_update_imap_ssl_health_check

        Updates imap ssl health check  # noqa: E501
        """
        pass

    def test_watch_update_ping_health_check(self):
        """Test case for watch_update_ping_health_check

        Updates ping health check  # noqa: E501
        """
        pass

    def test_watch_update_smtp_health_check(self):
        """Test case for watch_update_smtp_health_check

        Updates smtp health check  # noqa: E501
        """
        pass

    def test_watch_update_tcp_health_check(self):
        """Test case for watch_update_tcp_health_check

        Updates Tcp health check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
