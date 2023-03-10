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


class RunImportNetworkCommand(object):
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
        'public': 'bool',
        'public_ip_id': 'int',
        'opn_id': 'int'
    }

    attribute_map = {
        'public': 'Public',
        'public_ip_id': 'PublicIpId',
        'opn_id': 'OpnId'
    }

    def __init__(self, public=None, public_ip_id=None, opn_id=None, _configuration=None):  # noqa: E501
        """RunImportNetworkCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._public = None
        self._public_ip_id = None
        self._opn_id = None
        self.discriminator = None

        self.public = public
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if opn_id is not None:
            self.opn_id = opn_id

    @property
    def public(self):
        """Gets the public of this RunImportNetworkCommand.  # noqa: E501

        Is public network  # noqa: E501

        :return: The public of this RunImportNetworkCommand.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this RunImportNetworkCommand.

        Is public network  # noqa: E501

        :param public: The public of this RunImportNetworkCommand.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and public is None:
            raise ValueError("Invalid value for `public`, must not be `None`")  # noqa: E501

        self._public = public

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this RunImportNetworkCommand.  # noqa: E501

        Id of public ip - only for public network. When null, random address will be assigned.  # noqa: E501

        :return: The public_ip_id of this RunImportNetworkCommand.  # noqa: E501
        :rtype: int
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this RunImportNetworkCommand.

        Id of public ip - only for public network. When null, random address will be assigned.  # noqa: E501

        :param public_ip_id: The public_ip_id of this RunImportNetworkCommand.  # noqa: E501
        :type: int
        """

        self._public_ip_id = public_ip_id

    @property
    def opn_id(self):
        """Gets the opn_id of this RunImportNetworkCommand.  # noqa: E501

        Id of Opn - only for private network  # noqa: E501

        :return: The opn_id of this RunImportNetworkCommand.  # noqa: E501
        :rtype: int
        """
        return self._opn_id

    @opn_id.setter
    def opn_id(self, opn_id):
        """Sets the opn_id of this RunImportNetworkCommand.

        Id of Opn - only for private network  # noqa: E501

        :param opn_id: The opn_id of this RunImportNetworkCommand.  # noqa: E501
        :type: int
        """

        self._opn_id = opn_id

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
        if issubclass(RunImportNetworkCommand, dict):
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
        if not isinstance(other, RunImportNetworkCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunImportNetworkCommand):
            return True

        return self.to_dict() != other.to_dict()
