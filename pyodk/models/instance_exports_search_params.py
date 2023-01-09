# coding: utf-8

"""
    Oktawave API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pyodk.configuration import Configuration


class InstanceExportsSearchParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status_id': 'int',
        'page_size': 'int',
        'page_number': 'int',
        'order_by': 'str',
        'sort_expression': 'str',
        'sort_direction': 'str'
    }

    attribute_map = {
        'status_id': 'StatusId',
        'page_size': 'PageSize',
        'page_number': 'PageNumber',
        'order_by': 'OrderBy',
        'sort_expression': 'SortExpression',
        'sort_direction': 'SortDirection'
    }

    def __init__(self, status_id=None, page_size=None, page_number=None, order_by=None, sort_expression=None, sort_direction=None, _configuration=None):  # noqa: E501
        """InstanceExportsSearchParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status_id = None
        self._page_size = None
        self._page_number = None
        self._order_by = None
        self._sort_expression = None
        self._sort_direction = None
        self.discriminator = None

        if status_id is not None:
            self.status_id = status_id
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if order_by is not None:
            self.order_by = order_by
        if sort_expression is not None:
            self.sort_expression = sort_expression
        if sort_direction is not None:
            self.sort_direction = sort_direction

    @property
    def status_id(self):
        """Gets the status_id of this InstanceExportsSearchParams.  # noqa: E501

        Status id  # noqa: E501

        :return: The status_id of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this InstanceExportsSearchParams.

        Status id  # noqa: E501

        :param status_id: The status_id of this InstanceExportsSearchParams.  # noqa: E501
        :type: int
        """

        self._status_id = status_id

    @property
    def page_size(self):
        """Gets the page_size of this InstanceExportsSearchParams.  # noqa: E501

        Page size  # noqa: E501

        :return: The page_size of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InstanceExportsSearchParams.

        Page size  # noqa: E501

        :param page_size: The page_size of this InstanceExportsSearchParams.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this InstanceExportsSearchParams.  # noqa: E501

        Page number  # noqa: E501

        :return: The page_number of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this InstanceExportsSearchParams.

        Page number  # noqa: E501

        :param page_number: The page_number of this InstanceExportsSearchParams.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def order_by(self):
        """Gets the order_by of this InstanceExportsSearchParams.  # noqa: E501

        Order by  # noqa: E501

        :return: The order_by of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this InstanceExportsSearchParams.

        Order by  # noqa: E501

        :param order_by: The order_by of this InstanceExportsSearchParams.  # noqa: E501
        :type: str
        """

        self._order_by = order_by

    @property
    def sort_expression(self):
        """Gets the sort_expression of this InstanceExportsSearchParams.  # noqa: E501

        Sort expression  # noqa: E501

        :return: The sort_expression of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._sort_expression

    @sort_expression.setter
    def sort_expression(self, sort_expression):
        """Sets the sort_expression of this InstanceExportsSearchParams.

        Sort expression  # noqa: E501

        :param sort_expression: The sort_expression of this InstanceExportsSearchParams.  # noqa: E501
        :type: str
        """

        self._sort_expression = sort_expression

    @property
    def sort_direction(self):
        """Gets the sort_direction of this InstanceExportsSearchParams.  # noqa: E501

        Sort direction  # noqa: E501

        :return: The sort_direction of this InstanceExportsSearchParams.  # noqa: E501
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        """Sets the sort_direction of this InstanceExportsSearchParams.

        Sort direction  # noqa: E501

        :param sort_direction: The sort_direction of this InstanceExportsSearchParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["Descending", "Ascending"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_direction not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_direction` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_direction, allowed_values)
            )

        self._sort_direction = sort_direction

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InstanceExportsSearchParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceExportsSearchParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceExportsSearchParams):
            return True

        return self.to_dict() != other.to_dict()
