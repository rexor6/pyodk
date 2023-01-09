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


class TemplateDisk(object):
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
        'space_capacity': 'int',
        'tier': 'DictionaryItem',
        'creation_date': 'datetime',
        'controller': 'int',
        'slot': 'int',
        'is_system_disk': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'space_capacity': 'SpaceCapacity',
        'tier': 'Tier',
        'creation_date': 'CreationDate',
        'controller': 'Controller',
        'slot': 'Slot',
        'is_system_disk': 'IsSystemDisk'
    }

    def __init__(self, id=None, name=None, space_capacity=None, tier=None, creation_date=None, controller=None, slot=None, is_system_disk=None, _configuration=None):  # noqa: E501
        """TemplateDisk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._space_capacity = None
        self._tier = None
        self._creation_date = None
        self._controller = None
        self._slot = None
        self._is_system_disk = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if space_capacity is not None:
            self.space_capacity = space_capacity
        if tier is not None:
            self.tier = tier
        if creation_date is not None:
            self.creation_date = creation_date
        if controller is not None:
            self.controller = controller
        if slot is not None:
            self.slot = slot
        if is_system_disk is not None:
            self.is_system_disk = is_system_disk

    @property
    def id(self):
        """Gets the id of this TemplateDisk.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this TemplateDisk.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDisk.

        Id  # noqa: E501

        :param id: The id of this TemplateDisk.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateDisk.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this TemplateDisk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateDisk.

        Name  # noqa: E501

        :param name: The name of this TemplateDisk.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def space_capacity(self):
        """Gets the space_capacity of this TemplateDisk.  # noqa: E501

        Space capacity in GB  # noqa: E501

        :return: The space_capacity of this TemplateDisk.  # noqa: E501
        :rtype: int
        """
        return self._space_capacity

    @space_capacity.setter
    def space_capacity(self, space_capacity):
        """Sets the space_capacity of this TemplateDisk.

        Space capacity in GB  # noqa: E501

        :param space_capacity: The space_capacity of this TemplateDisk.  # noqa: E501
        :type: int
        """

        self._space_capacity = space_capacity

    @property
    def tier(self):
        """Gets the tier of this TemplateDisk.  # noqa: E501

        Tier  # noqa: E501

        :return: The tier of this TemplateDisk.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this TemplateDisk.

        Tier  # noqa: E501

        :param tier: The tier of this TemplateDisk.  # noqa: E501
        :type: DictionaryItem
        """

        self._tier = tier

    @property
    def creation_date(self):
        """Gets the creation_date of this TemplateDisk.  # noqa: E501

        Creation date  # noqa: E501

        :return: The creation_date of this TemplateDisk.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TemplateDisk.

        Creation date  # noqa: E501

        :param creation_date: The creation_date of this TemplateDisk.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def controller(self):
        """Gets the controller of this TemplateDisk.  # noqa: E501

        Controller  # noqa: E501

        :return: The controller of this TemplateDisk.  # noqa: E501
        :rtype: int
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this TemplateDisk.

        Controller  # noqa: E501

        :param controller: The controller of this TemplateDisk.  # noqa: E501
        :type: int
        """

        self._controller = controller

    @property
    def slot(self):
        """Gets the slot of this TemplateDisk.  # noqa: E501

        Slot  # noqa: E501

        :return: The slot of this TemplateDisk.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this TemplateDisk.

        Slot  # noqa: E501

        :param slot: The slot of this TemplateDisk.  # noqa: E501
        :type: int
        """

        self._slot = slot

    @property
    def is_system_disk(self):
        """Gets the is_system_disk of this TemplateDisk.  # noqa: E501

        If is system disk  # noqa: E501

        :return: The is_system_disk of this TemplateDisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_disk

    @is_system_disk.setter
    def is_system_disk(self, is_system_disk):
        """Sets the is_system_disk of this TemplateDisk.

        If is system disk  # noqa: E501

        :param is_system_disk: The is_system_disk of this TemplateDisk.  # noqa: E501
        :type: bool
        """

        self._is_system_disk = is_system_disk

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
        if issubclass(TemplateDisk, dict):
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
        if not isinstance(other, TemplateDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateDisk):
            return True

        return self.to_dict() != other.to_dict()