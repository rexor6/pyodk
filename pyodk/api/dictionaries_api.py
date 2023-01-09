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


class DictionariesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dictionaries_get_dictionaries(self, **kwargs):  # noqa: E501
        """Returns dictionaries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_dictionaries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Response fields filter
        :return: ApiCollectionDictionary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dictionaries_get_dictionaries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dictionaries_get_dictionaries_with_http_info(**kwargs)  # noqa: E501
            return data

    def dictionaries_get_dictionaries_with_http_info(self, **kwargs):  # noqa: E501
        """Returns dictionaries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_dictionaries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Response fields filter
        :return: ApiCollectionDictionary
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
                    " to method dictionaries_get_dictionaries" % key
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
            '/dictionaries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiCollectionDictionary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dictionaries_get_dictionaries_items(self, ids, **kwargs):  # noqa: E501
        """Returns dictionaries items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_dictionaries_items(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Dictionaries ids (required)
        :param str fields: Response fields filter
        :return: ApiCollectionDictionaryItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dictionaries_get_dictionaries_items_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.dictionaries_get_dictionaries_items_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def dictionaries_get_dictionaries_items_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Returns dictionaries items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_dictionaries_items_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: Dictionaries ids (required)
        :param str fields: Response fields filter
        :return: ApiCollectionDictionaryItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dictionaries_get_dictionaries_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if self.api_client.client_side_validation and ('ids' not in params or
                                                       params['ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ids` when calling `dictionaries_get_dictionaries_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ids' in params:
            path_params['ids'] = params['ids']  # noqa: E501

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
            '/dictionaries/{ids}', 'GET',
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

    def dictionaries_get_languages(self, **kwargs):  # noqa: E501
        """Returns languages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_languages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fields: Response fields filter
        :return: ApiCollectionDictionaryItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dictionaries_get_languages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dictionaries_get_languages_with_http_info(**kwargs)  # noqa: E501
            return data

    def dictionaries_get_languages_with_http_info(self, **kwargs):  # noqa: E501
        """Returns languages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dictionaries_get_languages_with_http_info(async_req=True)
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
                    " to method dictionaries_get_languages" % key
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
            '/dictionaries/languages', 'GET',
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
