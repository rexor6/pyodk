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


class CreateDiskCommand(object):
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
        'disk_name': 'str',
        'space_capacity': 'int',
        'tier_id': 'int',
        'shared_disk_type_id': 'int',
        'subregion_id': 'int',
        'instance_ids_list': 'list[int]'
    }

    attribute_map = {
        'disk_name': 'DiskName',
        'space_capacity': 'SpaceCapacity',
        'tier_id': 'TierId',
        'shared_disk_type_id': 'SharedDiskTypeId',
        'subregion_id': 'SubregionId',
        'instance_ids_list': 'InstanceIdsList'
    }

    def __init__(self, disk_name=None, space_capacity=5, tier_id=48, shared_disk_type_id=None, subregion_id=None, instance_ids_list=None, _configuration=None):  # noqa: E501
        """CreateDiskCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._disk_name = None
        self._space_capacity = None
        self._tier_id = None
        self._shared_disk_type_id = None
        self._subregion_id = None
        self._instance_ids_list = None
        self.discriminator = None

        self.disk_name = disk_name
        self.space_capacity = space_capacity
        self.tier_id = tier_id
        if shared_disk_type_id is not None:
            self.shared_disk_type_id = shared_disk_type_id
        if subregion_id is not None:
            self.subregion_id = subregion_id
        if instance_ids_list is not None:
            self.instance_ids_list = instance_ids_list

    @property
    def disk_name(self):
        """Gets the disk_name of this CreateDiskCommand.  # noqa: E501

        Name of disk  # noqa: E501

        :return: The disk_name of this CreateDiskCommand.  # noqa: E501
        :rtype: str
        """
        return self._disk_name

    @disk_name.setter
    def disk_name(self, disk_name):
        """Sets the disk_name of this CreateDiskCommand.

        Name of disk  # noqa: E501

        :param disk_name: The disk_name of this CreateDiskCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and disk_name is None:
            raise ValueError("Invalid value for `disk_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                disk_name is not None and len(disk_name) > 300):
            raise ValueError("Invalid value for `disk_name`, length must be less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                disk_name is not None and len(disk_name) < 1):
            raise ValueError("Invalid value for `disk_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                disk_name is not None and not re.search(r'^[^\/\\\\|<>%]*$', disk_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `disk_name`, must be a follow pattern or equal to `/^[^\/\\\\|<>%]*$/`")  # noqa: E501

        self._disk_name = disk_name

    @property
    def space_capacity(self):
        """Gets the space_capacity of this CreateDiskCommand.  # noqa: E501

        Space capacity in GB  # noqa: E501

        :return: The space_capacity of this CreateDiskCommand.  # noqa: E501
        :rtype: int
        """
        return self._space_capacity

    @space_capacity.setter
    def space_capacity(self, space_capacity):
        """Sets the space_capacity of this CreateDiskCommand.

        Space capacity in GB  # noqa: E501

        :param space_capacity: The space_capacity of this CreateDiskCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and space_capacity is None:
            raise ValueError("Invalid value for `space_capacity`, must not be `None`")  # noqa: E501

        self._space_capacity = space_capacity

    @property
    def tier_id(self):
        """Gets the tier_id of this CreateDiskCommand.  # noqa: E501

        Tier id  # noqa: E501

        :return: The tier_id of this CreateDiskCommand.  # noqa: E501
        :rtype: int
        """
        return self._tier_id

    @tier_id.setter
    def tier_id(self, tier_id):
        """Sets the tier_id of this CreateDiskCommand.

        Tier id  # noqa: E501

        :param tier_id: The tier_id of this CreateDiskCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and tier_id is None:
            raise ValueError("Invalid value for `tier_id`, must not be `None`")  # noqa: E501

        self._tier_id = tier_id

    @property
    def shared_disk_type_id(self):
        """Gets the shared_disk_type_id of this CreateDiskCommand.  # noqa: E501

        Shared disk type, null if disk is not shared  # noqa: E501

        :return: The shared_disk_type_id of this CreateDiskCommand.  # noqa: E501
        :rtype: int
        """
        return self._shared_disk_type_id

    @shared_disk_type_id.setter
    def shared_disk_type_id(self, shared_disk_type_id):
        """Sets the shared_disk_type_id of this CreateDiskCommand.

        Shared disk type, null if disk is not shared  # noqa: E501

        :param shared_disk_type_id: The shared_disk_type_id of this CreateDiskCommand.  # noqa: E501
        :type: int
        """

        self._shared_disk_type_id = shared_disk_type_id

    @property
    def subregion_id(self):
        """Gets the subregion_id of this CreateDiskCommand.  # noqa: E501

        Subregion identifier  # noqa: E501

        :return: The subregion_id of this CreateDiskCommand.  # noqa: E501
        :rtype: int
        """
        return self._subregion_id

    @subregion_id.setter
    def subregion_id(self, subregion_id):
        """Sets the subregion_id of this CreateDiskCommand.

        Subregion identifier  # noqa: E501

        :param subregion_id: The subregion_id of this CreateDiskCommand.  # noqa: E501
        :type: int
        """

        self._subregion_id = subregion_id

    @property
    def instance_ids_list(self):
        """Gets the instance_ids_list of this CreateDiskCommand.  # noqa: E501

        Instance ids list  # noqa: E501

        :return: The instance_ids_list of this CreateDiskCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._instance_ids_list

    @instance_ids_list.setter
    def instance_ids_list(self, instance_ids_list):
        """Sets the instance_ids_list of this CreateDiskCommand.

        Instance ids list  # noqa: E501

        :param instance_ids_list: The instance_ids_list of this CreateDiskCommand.  # noqa: E501
        :type: list[int]
        """

        self._instance_ids_list = instance_ids_list

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
        if issubclass(CreateDiskCommand, dict):
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
        if not isinstance(other, CreateDiskCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDiskCommand):
            return True

        return self.to_dict() != other.to_dict()
