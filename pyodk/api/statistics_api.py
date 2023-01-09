# coding: utf-8

"""
    Oktawave API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyodk.api_client import ApiClient


class StatisticsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def statistics_get_client_statistics(self, date_from, date_to, statistic_types, **kwargs):  # noqa: E501
        """Gets client statistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_client_statistics(date_from, date_to, statistic_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime date_from: Date from (utc timezone) (required)
        :param datetime date_to: Date to (utc timezone) (required)
        :param list[int] statistic_types: Statistic types (required)
        :param str fields: Response fields filter
        :return: ApiCollectionClientStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.statistics_get_client_statistics_with_http_info(date_from, date_to, statistic_types, **kwargs)  # noqa: E501
        else:
            (data) = self.statistics_get_client_statistics_with_http_info(date_from, date_to, statistic_types, **kwargs)  # noqa: E501
            return data

    def statistics_get_client_statistics_with_http_info(self, date_from, date_to, statistic_types, **kwargs):  # noqa: E501
        """Gets client statistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_client_statistics_with_http_info(date_from, date_to, statistic_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime date_from: Date from (utc timezone) (required)
        :param datetime date_to: Date to (utc timezone) (required)
        :param list[int] statistic_types: Statistic types (required)
        :param str fields: Response fields filter
        :return: ApiCollectionClientStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_from', 'date_to', 'statistic_types', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method statistics_get_client_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'date_from' is set
        if self.api_client.client_side_validation and ('date_from' not in params or
                                                       params['date_from'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `date_from` when calling `statistics_get_client_statistics`")  # noqa: E501
        # verify the required parameter 'date_to' is set
        if self.api_client.client_side_validation and ('date_to' not in params or
                                                       params['date_to'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `date_to` when calling `statistics_get_client_statistics`")  # noqa: E501
        # verify the required parameter 'statistic_types' is set
        if self.api_client.client_side_validation and ('statistic_types' not in params or
                                                       params['statistic_types'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `statistic_types` when calling `statistics_get_client_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'statistic_types' in params:
            query_params.append(('statisticTypes', params['statistic_types']))  # noqa: E501
            collection_formats['statisticTypes'] = 'multi'  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/statistics/account', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiCollectionClientStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def statistics_get_instance_statistics(self, id, statistic_interval, date_from, date_to, statistic_types, **kwargs):  # noqa: E501
        """Gets instance statistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_instance_statistics(id, statistic_interval, date_from, date_to, statistic_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id (required)
        :param int statistic_interval: Statistic interval (required)
        :param datetime date_from: Date from (utc timezone) (required)
        :param datetime date_to: Date to (utc timezone) (required)
        :param list[int] statistic_types: Statistic types (required)
        :param str fields: Response fields filter
        :return: ApiCollectionInstanceStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.statistics_get_instance_statistics_with_http_info(id, statistic_interval, date_from, date_to, statistic_types, **kwargs)  # noqa: E501
        else:
            (data) = self.statistics_get_instance_statistics_with_http_info(id, statistic_interval, date_from, date_to, statistic_types, **kwargs)  # noqa: E501
            return data

    def statistics_get_instance_statistics_with_http_info(self, id, statistic_interval, date_from, date_to, statistic_types, **kwargs):  # noqa: E501
        """Gets instance statistics  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_instance_statistics_with_http_info(id, statistic_interval, date_from, date_to, statistic_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Id (required)
        :param int statistic_interval: Statistic interval (required)
        :param datetime date_from: Date from (utc timezone) (required)
        :param datetime date_to: Date to (utc timezone) (required)
        :param list[int] statistic_types: Statistic types (required)
        :param str fields: Response fields filter
        :return: ApiCollectionInstanceStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'statistic_interval', 'date_from', 'date_to', 'statistic_types', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method statistics_get_instance_statistics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `statistics_get_instance_statistics`")  # noqa: E501
        # verify the required parameter 'statistic_interval' is set
        if self.api_client.client_side_validation and ('statistic_interval' not in params or
                                                       params['statistic_interval'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `statistic_interval` when calling `statistics_get_instance_statistics`")  # noqa: E501
        # verify the required parameter 'date_from' is set
        if self.api_client.client_side_validation and ('date_from' not in params or
                                                       params['date_from'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `date_from` when calling `statistics_get_instance_statistics`")  # noqa: E501
        # verify the required parameter 'date_to' is set
        if self.api_client.client_side_validation and ('date_to' not in params or
                                                       params['date_to'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `date_to` when calling `statistics_get_instance_statistics`")  # noqa: E501
        # verify the required parameter 'statistic_types' is set
        if self.api_client.client_side_validation and ('statistic_types' not in params or
                                                       params['statistic_types'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `statistic_types` when calling `statistics_get_instance_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'statistic_interval' in params:
            query_params.append(('statisticInterval', params['statistic_interval']))  # noqa: E501
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'statistic_types' in params:
            query_params.append(('statisticTypes', params['statistic_types']))  # noqa: E501
            collection_formats['statisticTypes'] = 'multi'  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/statistics/instances/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiCollectionInstanceStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def statistics_get_statistic_intervals(self, **kwargs):  # noqa: E501
        """Gets statistic interval types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_statistic_intervals(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Response fields filter
        :return: ApiCollectionDictionaryItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.statistics_get_statistic_intervals_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.statistics_get_statistic_intervals_with_http_info(**kwargs)  # noqa: E501
            return data

    def statistics_get_statistic_intervals_with_http_info(self, **kwargs):  # noqa: E501
        """Gets statistic interval types  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statistics_get_statistic_intervals_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Response fields filter
        :return: ApiCollectionDictionaryItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method statistics_get_statistic_intervals" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/statistics/dictionaries/intervals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiCollectionDictionaryItem',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
