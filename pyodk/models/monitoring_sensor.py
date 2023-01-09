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


class MonitoringSensor(object):
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
        'id': 'int',
        'country': 'str',
        'city': 'str',
        'ip_address': 'str',
        'name': 'str',
        'is_available': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'country': 'Country',
        'city': 'City',
        'ip_address': 'IPAddress',
        'name': 'Name',
        'is_available': 'IsAvailable'
    }

    def __init__(self, id=None, country=None, city=None, ip_address=None, name=None, is_available=None, _configuration=None):  # noqa: E501
        """MonitoringSensor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._country = None
        self._city = None
        self._ip_address = None
        self._name = None
        self._is_available = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if ip_address is not None:
            self.ip_address = ip_address
        if name is not None:
            self.name = name
        if is_available is not None:
            self.is_available = is_available

    @property
    def id(self):
        """Gets the id of this MonitoringSensor.  # noqa: E501

        Identifier  # noqa: E501

        :return: The id of this MonitoringSensor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MonitoringSensor.

        Identifier  # noqa: E501

        :param id: The id of this MonitoringSensor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def country(self):
        """Gets the country of this MonitoringSensor.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this MonitoringSensor.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this MonitoringSensor.

        Country  # noqa: E501

        :param country: The country of this MonitoringSensor.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city(self):
        """Gets the city of this MonitoringSensor.  # noqa: E501

        City  # noqa: E501

        :return: The city of this MonitoringSensor.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this MonitoringSensor.

        City  # noqa: E501

        :param city: The city of this MonitoringSensor.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def ip_address(self):
        """Gets the ip_address of this MonitoringSensor.  # noqa: E501

        IPAddress  # noqa: E501

        :return: The ip_address of this MonitoringSensor.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this MonitoringSensor.

        IPAddress  # noqa: E501

        :param ip_address: The ip_address of this MonitoringSensor.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def name(self):
        """Gets the name of this MonitoringSensor.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this MonitoringSensor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MonitoringSensor.

        Name  # noqa: E501

        :param name: The name of this MonitoringSensor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_available(self):
        """Gets the is_available of this MonitoringSensor.  # noqa: E501

        Is available  # noqa: E501

        :return: The is_available of this MonitoringSensor.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this MonitoringSensor.

        Is available  # noqa: E501

        :param is_available: The is_available of this MonitoringSensor.  # noqa: E501
        :type: bool
        """

        self._is_available = is_available

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
        if issubclass(MonitoringSensor, dict):
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
        if not isinstance(other, MonitoringSensor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonitoringSensor):
            return True

        return self.to_dict() != other.to_dict()