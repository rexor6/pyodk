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


class DictionaryItem(object):
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
        'label': 'str',
        'dictionary': 'Resource'
    }

    attribute_map = {
        'id': 'Id',
        'label': 'Label',
        'dictionary': 'Dictionary'
    }

    def __init__(self, id=None, label=None, dictionary=None, _configuration=None):  # noqa: E501
        """DictionaryItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._label = None
        self._dictionary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if dictionary is not None:
            self.dictionary = dictionary

    @property
    def id(self):
        """Gets the id of this DictionaryItem.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this DictionaryItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DictionaryItem.

        ID  # noqa: E501

        :param id: The id of this DictionaryItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this DictionaryItem.  # noqa: E501

        Label  # noqa: E501

        :return: The label of this DictionaryItem.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DictionaryItem.

        Label  # noqa: E501

        :param label: The label of this DictionaryItem.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def dictionary(self):
        """Gets the dictionary of this DictionaryItem.  # noqa: E501

        Dictionary  # noqa: E501

        :return: The dictionary of this DictionaryItem.  # noqa: E501
        :rtype: Resource
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this DictionaryItem.

        Dictionary  # noqa: E501

        :param dictionary: The dictionary of this DictionaryItem.  # noqa: E501
        :type: Resource
        """

        self._dictionary = dictionary

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
        if issubclass(DictionaryItem, dict):
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
        if not isinstance(other, DictionaryItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryItem):
            return True

        return self.to_dict() != other.to_dict()
