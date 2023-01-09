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


class SshKey(object):
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
        'name': 'str',
        'value': 'str',
        'owner_user': 'UserResource',
        'creation_date': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'value': 'Value',
        'owner_user': 'OwnerUser',
        'creation_date': 'CreationDate'
    }

    def __init__(self, id=None, name=None, value=None, owner_user=None, creation_date=None, _configuration=None):  # noqa: E501
        """SshKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._value = None
        self._owner_user = None
        self._creation_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if owner_user is not None:
            self.owner_user = owner_user
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this SshKey.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this SshKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SshKey.

        Id  # noqa: E501

        :param id: The id of this SshKey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SshKey.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SshKey.

        Name  # noqa: E501

        :param name: The name of this SshKey.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this SshKey.  # noqa: E501

        Key value trimmed  # noqa: E501

        :return: The value of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SshKey.

        Key value trimmed  # noqa: E501

        :param value: The value of this SshKey.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def owner_user(self):
        """Gets the owner_user of this SshKey.  # noqa: E501

        User owning the key  # noqa: E501

        :return: The owner_user of this SshKey.  # noqa: E501
        :rtype: UserResource
        """
        return self._owner_user

    @owner_user.setter
    def owner_user(self, owner_user):
        """Sets the owner_user of this SshKey.

        User owning the key  # noqa: E501

        :param owner_user: The owner_user of this SshKey.  # noqa: E501
        :type: UserResource
        """

        self._owner_user = owner_user

    @property
    def creation_date(self):
        """Gets the creation_date of this SshKey.  # noqa: E501

        Creation date  # noqa: E501

        :return: The creation_date of this SshKey.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this SshKey.

        Creation date  # noqa: E501

        :param creation_date: The creation_date of this SshKey.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

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
        if issubclass(SshKey, dict):
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
        if not isinstance(other, SshKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SshKey):
            return True

        return self.to_dict() != other.to_dict()