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


class PaymentDetails(object):
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
        'account_number': 'str',
        'external_account_number': 'str',
        'payment_method': 'DictionaryItem',
        'vat_rate': 'float'
    }

    attribute_map = {
        'account_number': 'AccountNumber',
        'external_account_number': 'ExternalAccountNumber',
        'payment_method': 'PaymentMethod',
        'vat_rate': 'VatRate'
    }

    def __init__(self, account_number=None, external_account_number=None, payment_method=None, vat_rate=None, _configuration=None):  # noqa: E501
        """PaymentDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_number = None
        self._external_account_number = None
        self._payment_method = None
        self._vat_rate = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if external_account_number is not None:
            self.external_account_number = external_account_number
        if payment_method is not None:
            self.payment_method = payment_method
        if vat_rate is not None:
            self.vat_rate = vat_rate

    @property
    def account_number(self):
        """Gets the account_number of this PaymentDetails.  # noqa: E501

        Account number  # noqa: E501

        :return: The account_number of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentDetails.

        Account number  # noqa: E501

        :param account_number: The account_number of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def external_account_number(self):
        """Gets the external_account_number of this PaymentDetails.  # noqa: E501

        External account number  # noqa: E501

        :return: The external_account_number of this PaymentDetails.  # noqa: E501
        :rtype: str
        """
        return self._external_account_number

    @external_account_number.setter
    def external_account_number(self, external_account_number):
        """Sets the external_account_number of this PaymentDetails.

        External account number  # noqa: E501

        :param external_account_number: The external_account_number of this PaymentDetails.  # noqa: E501
        :type: str
        """

        self._external_account_number = external_account_number

    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentDetails.  # noqa: E501

        Payment method  # noqa: E501

        :return: The payment_method of this PaymentDetails.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentDetails.

        Payment method  # noqa: E501

        :param payment_method: The payment_method of this PaymentDetails.  # noqa: E501
        :type: DictionaryItem
        """

        self._payment_method = payment_method

    @property
    def vat_rate(self):
        """Gets the vat_rate of this PaymentDetails.  # noqa: E501

        Vat rate  # noqa: E501

        :return: The vat_rate of this PaymentDetails.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this PaymentDetails.

        Vat rate  # noqa: E501

        :param vat_rate: The vat_rate of this PaymentDetails.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

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
        if issubclass(PaymentDetails, dict):
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
        if not isinstance(other, PaymentDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentDetails):
            return True

        return self.to_dict() != other.to_dict()
