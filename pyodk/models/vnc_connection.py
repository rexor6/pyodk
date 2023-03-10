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


class VncConnection(object):
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
        'instance': 'BaseResource',
        'source_ip': 'str',
        'address': 'str',
        'port': 'int',
        'password': 'str',
        'open_until': 'datetime'
    }

    attribute_map = {
        'instance': 'Instance',
        'source_ip': 'SourceIp',
        'address': 'Address',
        'port': 'Port',
        'password': 'Password',
        'open_until': 'OpenUntil'
    }

    def __init__(self, instance=None, source_ip=None, address=None, port=None, password=None, open_until=None, _configuration=None):  # noqa: E501
        """VncConnection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance = None
        self._source_ip = None
        self._address = None
        self._port = None
        self._password = None
        self._open_until = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if source_ip is not None:
            self.source_ip = source_ip
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if password is not None:
            self.password = password
        if open_until is not None:
            self.open_until = open_until

    @property
    def instance(self):
        """Gets the instance of this VncConnection.  # noqa: E501

        Instance  # noqa: E501

        :return: The instance of this VncConnection.  # noqa: E501
        :rtype: BaseResource
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this VncConnection.

        Instance  # noqa: E501

        :param instance: The instance of this VncConnection.  # noqa: E501
        :type: BaseResource
        """

        self._instance = instance

    @property
    def source_ip(self):
        """Gets the source_ip of this VncConnection.  # noqa: E501

        Source ip  # noqa: E501

        :return: The source_ip of this VncConnection.  # noqa: E501
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this VncConnection.

        Source ip  # noqa: E501

        :param source_ip: The source_ip of this VncConnection.  # noqa: E501
        :type: str
        """

        self._source_ip = source_ip

    @property
    def address(self):
        """Gets the address of this VncConnection.  # noqa: E501

        Address  # noqa: E501

        :return: The address of this VncConnection.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this VncConnection.

        Address  # noqa: E501

        :param address: The address of this VncConnection.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def port(self):
        """Gets the port of this VncConnection.  # noqa: E501

        Port  # noqa: E501

        :return: The port of this VncConnection.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VncConnection.

        Port  # noqa: E501

        :param port: The port of this VncConnection.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def password(self):
        """Gets the password of this VncConnection.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this VncConnection.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VncConnection.

        Password  # noqa: E501

        :param password: The password of this VncConnection.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def open_until(self):
        """Gets the open_until of this VncConnection.  # noqa: E501

        Open until  # noqa: E501

        :return: The open_until of this VncConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._open_until

    @open_until.setter
    def open_until(self, open_until):
        """Sets the open_until of this VncConnection.

        Open until  # noqa: E501

        :param open_until: The open_until of this VncConnection.  # noqa: E501
        :type: datetime
        """

        self._open_until = open_until

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
        if issubclass(VncConnection, dict):
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
        if not isinstance(other, VncConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VncConnection):
            return True

        return self.to_dict() != other.to_dict()
