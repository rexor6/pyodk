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


class BookIpCommand(object):
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
        'subregion_id': 'int'
    }

    attribute_map = {
        'subregion_id': 'SubregionId'
    }

    def __init__(self, subregion_id=None, _configuration=None):  # noqa: E501
        """BookIpCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._subregion_id = None
        self.discriminator = None

        self.subregion_id = subregion_id

    @property
    def subregion_id(self):
        """Gets the subregion_id of this BookIpCommand.  # noqa: E501

        Subregion Id  # noqa: E501

        :return: The subregion_id of this BookIpCommand.  # noqa: E501
        :rtype: int
        """
        return self._subregion_id

    @subregion_id.setter
    def subregion_id(self, subregion_id):
        """Sets the subregion_id of this BookIpCommand.

        Subregion Id  # noqa: E501

        :param subregion_id: The subregion_id of this BookIpCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and subregion_id is None:
            raise ValueError("Invalid value for `subregion_id`, must not be `None`")  # noqa: E501

        self._subregion_id = subregion_id

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
        if issubclass(BookIpCommand, dict):
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
        if not isinstance(other, BookIpCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BookIpCommand):
            return True

        return self.to_dict() != other.to_dict()
