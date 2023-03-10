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


class CreateOpnCommand(object):
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
        'opn_name': 'str'
    }

    attribute_map = {
        'opn_name': 'OpnName'
    }

    def __init__(self, opn_name=None, _configuration=None):  # noqa: E501
        """CreateOpnCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._opn_name = None
        self.discriminator = None

        self.opn_name = opn_name

    @property
    def opn_name(self):
        """Gets the opn_name of this CreateOpnCommand.  # noqa: E501

        OPN name  # noqa: E501

        :return: The opn_name of this CreateOpnCommand.  # noqa: E501
        :rtype: str
        """
        return self._opn_name

    @opn_name.setter
    def opn_name(self, opn_name):
        """Sets the opn_name of this CreateOpnCommand.

        OPN name  # noqa: E501

        :param opn_name: The opn_name of this CreateOpnCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and opn_name is None:
            raise ValueError("Invalid value for `opn_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                opn_name is not None and len(opn_name) > 500):
            raise ValueError("Invalid value for `opn_name`, length must be less than or equal to `500`")  # noqa: E501
        if (self._configuration.client_side_validation and
                opn_name is not None and len(opn_name) < 1):
            raise ValueError("Invalid value for `opn_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                opn_name is not None and not re.search(r'^[^\/\\\\|<>%]*$', opn_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `opn_name`, must be a follow pattern or equal to `/^[^\/\\\\|<>%]*$/`")  # noqa: E501

        self._opn_name = opn_name

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
        if issubclass(CreateOpnCommand, dict):
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
        if not isinstance(other, CreateOpnCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOpnCommand):
            return True

        return self.to_dict() != other.to_dict()
