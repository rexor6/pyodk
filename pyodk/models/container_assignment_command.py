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


class ContainerAssignmentCommand(object):
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
        'instance_id': 'int',
        'ip_id': 'int'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'ip_id': 'IpId'
    }

    def __init__(self, instance_id=None, ip_id=None, _configuration=None):  # noqa: E501
        """ContainerAssignmentCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._ip_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.ip_id = ip_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ContainerAssignmentCommand.  # noqa: E501

        Id of an instance  # noqa: E501

        :return: The instance_id of this ContainerAssignmentCommand.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ContainerAssignmentCommand.

        Id of an instance  # noqa: E501

        :param instance_id: The instance_id of this ContainerAssignmentCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def ip_id(self):
        """Gets the ip_id of this ContainerAssignmentCommand.  # noqa: E501

        Id of instance ip  # noqa: E501

        :return: The ip_id of this ContainerAssignmentCommand.  # noqa: E501
        :rtype: int
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this ContainerAssignmentCommand.

        Id of instance ip  # noqa: E501

        :param ip_id: The ip_id of this ContainerAssignmentCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and ip_id is None:
            raise ValueError("Invalid value for `ip_id`, must not be `None`")  # noqa: E501

        self._ip_id = ip_id

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
        if issubclass(ContainerAssignmentCommand, dict):
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
        if not isinstance(other, ContainerAssignmentCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerAssignmentCommand):
            return True

        return self.to_dict() != other.to_dict()
