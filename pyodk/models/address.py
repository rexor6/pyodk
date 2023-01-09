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


class Address(object):
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
        'address_type': 'DictionaryItem',
        'street': 'str',
        'city': 'str',
        'zip': 'str',
        'country': 'DictionaryItem',
        'region': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'address_type': 'AddressType',
        'street': 'Street',
        'city': 'City',
        'zip': 'Zip',
        'country': 'Country',
        'region': 'Region'
    }

    def __init__(self, id=None, address_type=None, street=None, city=None, zip=None, country=None, region=None, _configuration=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._address_type = None
        self._street = None
        self._city = None
        self._zip = None
        self._country = None
        self._region = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address_type is not None:
            self.address_type = address_type
        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country
        if region is not None:
            self.region = region

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        Id of address  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        Id of address  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def address_type(self):
        """Gets the address_type of this Address.  # noqa: E501

        Address type  # noqa: E501

        :return: The address_type of this Address.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Address.

        Address type  # noqa: E501

        :param address_type: The address_type of this Address.  # noqa: E501
        :type: DictionaryItem
        """

        self._address_type = address_type

    @property
    def street(self):
        """Gets the street of this Address.  # noqa: E501

        Street  # noqa: E501

        :return: The street of this Address.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Address.

        Street  # noqa: E501

        :param street: The street of this Address.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        City  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        City  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def zip(self):
        """Gets the zip of this Address.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Address.

        Zip code  # noqa: E501

        :param zip: The zip of this Address.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        Country  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: DictionaryItem
        """

        self._country = country

    @property
    def region(self):
        """Gets the region of this Address.  # noqa: E501

        Region  # noqa: E501

        :return: The region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Address.

        Region  # noqa: E501

        :param region: The region of this Address.  # noqa: E501
        :type: str
        """

        self._region = region

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
