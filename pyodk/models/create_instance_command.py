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


class CreateInstanceCommand(object):
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
        'authorization_method_id': 'int',
        'disk_class': 'int',
        'disk_size': 'int',
        'instance_name': 'str',
        'instances_count': 'int',
        'ip_address_id': 'int',
        'ssh_keys_ids': 'list[int]',
        'opns_ids': 'list[int]',
        'subregion_id': 'int',
        'template_id': 'int',
        'type_id': 'int',
        'freemium': 'bool',
        'init_script': 'str',
        'without_public_ip': 'bool'
    }

    attribute_map = {
        'authorization_method_id': 'AuthorizationMethodId',
        'disk_class': 'DiskClass',
        'disk_size': 'DiskSize',
        'instance_name': 'InstanceName',
        'instances_count': 'InstancesCount',
        'ip_address_id': 'IPAddressId',
        'ssh_keys_ids': 'SshKeysIds',
        'opns_ids': 'OpnsIds',
        'subregion_id': 'SubregionId',
        'template_id': 'TemplateId',
        'type_id': 'TypeId',
        'freemium': 'Freemium',
        'init_script': 'InitScript',
        'without_public_ip': 'WithoutPublicIp'
    }

    def __init__(self, authorization_method_id=None, disk_class=None, disk_size=None, instance_name=None, instances_count=None, ip_address_id=None, ssh_keys_ids=None, opns_ids=None, subregion_id=None, template_id=None, type_id=None, freemium=False, init_script=None, without_public_ip=False, _configuration=None):  # noqa: E501
        """CreateInstanceCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authorization_method_id = None
        self._disk_class = None
        self._disk_size = None
        self._instance_name = None
        self._instances_count = None
        self._ip_address_id = None
        self._ssh_keys_ids = None
        self._opns_ids = None
        self._subregion_id = None
        self._template_id = None
        self._type_id = None
        self._freemium = None
        self._init_script = None
        self._without_public_ip = None
        self.discriminator = None

        if authorization_method_id is not None:
            self.authorization_method_id = authorization_method_id
        if disk_class is not None:
            self.disk_class = disk_class
        if disk_size is not None:
            self.disk_size = disk_size
        self.instance_name = instance_name
        if instances_count is not None:
            self.instances_count = instances_count
        if ip_address_id is not None:
            self.ip_address_id = ip_address_id
        if ssh_keys_ids is not None:
            self.ssh_keys_ids = ssh_keys_ids
        if opns_ids is not None:
            self.opns_ids = opns_ids
        if subregion_id is not None:
            self.subregion_id = subregion_id
        self.template_id = template_id
        if type_id is not None:
            self.type_id = type_id
        if freemium is not None:
            self.freemium = freemium
        if init_script is not None:
            self.init_script = init_script
        if without_public_ip is not None:
            self.without_public_ip = without_public_ip

    @property
    def authorization_method_id(self):
        """Gets the authorization_method_id of this CreateInstanceCommand.  # noqa: E501

        Authorization method (Password)  # noqa: E501

        :return: The authorization_method_id of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._authorization_method_id

    @authorization_method_id.setter
    def authorization_method_id(self, authorization_method_id):
        """Sets the authorization_method_id of this CreateInstanceCommand.

        Authorization method (Password)  # noqa: E501

        :param authorization_method_id: The authorization_method_id of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """

        self._authorization_method_id = authorization_method_id

    @property
    def disk_class(self):
        """Gets the disk_class of this CreateInstanceCommand.  # noqa: E501

        Class of disk  # noqa: E501

        :return: The disk_class of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._disk_class

    @disk_class.setter
    def disk_class(self, disk_class):
        """Sets the disk_class of this CreateInstanceCommand.

        Class of disk  # noqa: E501

        :param disk_class: The disk_class of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """

        self._disk_class = disk_class

    @property
    def disk_size(self):
        """Gets the disk_size of this CreateInstanceCommand.  # noqa: E501

        Size of disk in gigabytes  # noqa: E501

        :return: The disk_size of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this CreateInstanceCommand.

        Size of disk in gigabytes  # noqa: E501

        :param disk_size: The disk_size of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                disk_size is not None and disk_size > 300):  # noqa: E501
            raise ValueError("Invalid value for `disk_size`, must be a value less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                disk_size is not None and disk_size < 5):  # noqa: E501
            raise ValueError("Invalid value for `disk_size`, must be a value greater than or equal to `5`")  # noqa: E501

        self._disk_size = disk_size

    @property
    def instance_name(self):
        """Gets the instance_name of this CreateInstanceCommand.  # noqa: E501

        Name of an instance  # noqa: E501

        :return: The instance_name of this CreateInstanceCommand.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CreateInstanceCommand.

        Name of an instance  # noqa: E501

        :param instance_name: The instance_name of this CreateInstanceCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_name is None:
            raise ValueError("Invalid value for `instance_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_name is not None and len(instance_name) > 40):
            raise ValueError("Invalid value for `instance_name`, length must be less than or equal to `40`")  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_name is not None and len(instance_name) < 1):
            raise ValueError("Invalid value for `instance_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                instance_name is not None and not re.search(r'^[^\/\\\\|<>%]*$', instance_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `instance_name`, must be a follow pattern or equal to `/^[^\/\\\\|<>%]*$/`")  # noqa: E501

        self._instance_name = instance_name

    @property
    def instances_count(self):
        """Gets the instances_count of this CreateInstanceCommand.  # noqa: E501

        Count of instances  # noqa: E501

        :return: The instances_count of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._instances_count

    @instances_count.setter
    def instances_count(self, instances_count):
        """Sets the instances_count of this CreateInstanceCommand.

        Count of instances  # noqa: E501

        :param instances_count: The instances_count of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                instances_count is not None and instances_count > 5):  # noqa: E501
            raise ValueError("Invalid value for `instances_count`, must be a value less than or equal to `5`")  # noqa: E501
        if (self._configuration.client_side_validation and
                instances_count is not None and instances_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `instances_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._instances_count = instances_count

    @property
    def ip_address_id(self):
        """Gets the ip_address_id of this CreateInstanceCommand.  # noqa: E501

        Id of ip address  # noqa: E501

        :return: The ip_address_id of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._ip_address_id

    @ip_address_id.setter
    def ip_address_id(self, ip_address_id):
        """Sets the ip_address_id of this CreateInstanceCommand.

        Id of ip address  # noqa: E501

        :param ip_address_id: The ip_address_id of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """

        self._ip_address_id = ip_address_id

    @property
    def ssh_keys_ids(self):
        """Gets the ssh_keys_ids of this CreateInstanceCommand.  # noqa: E501

        Id of ssh keys to be attached to the instance  # noqa: E501

        :return: The ssh_keys_ids of this CreateInstanceCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._ssh_keys_ids

    @ssh_keys_ids.setter
    def ssh_keys_ids(self, ssh_keys_ids):
        """Sets the ssh_keys_ids of this CreateInstanceCommand.

        Id of ssh keys to be attached to the instance  # noqa: E501

        :param ssh_keys_ids: The ssh_keys_ids of this CreateInstanceCommand.  # noqa: E501
        :type: list[int]
        """

        self._ssh_keys_ids = ssh_keys_ids

    @property
    def opns_ids(self):
        """Gets the opns_ids of this CreateInstanceCommand.  # noqa: E501

        Id of opns where attach the instance  # noqa: E501

        :return: The opns_ids of this CreateInstanceCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._opns_ids

    @opns_ids.setter
    def opns_ids(self, opns_ids):
        """Sets the opns_ids of this CreateInstanceCommand.

        Id of opns where attach the instance  # noqa: E501

        :param opns_ids: The opns_ids of this CreateInstanceCommand.  # noqa: E501
        :type: list[int]
        """

        self._opns_ids = opns_ids

    @property
    def subregion_id(self):
        """Gets the subregion_id of this CreateInstanceCommand.  # noqa: E501

        Id of target subregion  # noqa: E501

        :return: The subregion_id of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._subregion_id

    @subregion_id.setter
    def subregion_id(self, subregion_id):
        """Sets the subregion_id of this CreateInstanceCommand.

        Id of target subregion  # noqa: E501

        :param subregion_id: The subregion_id of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """

        self._subregion_id = subregion_id

    @property
    def template_id(self):
        """Gets the template_id of this CreateInstanceCommand.  # noqa: E501

        Template id  # noqa: E501

        :return: The template_id of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateInstanceCommand.

        Template id  # noqa: E501

        :param template_id: The template_id of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and template_id is None:
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def type_id(self):
        """Gets the type_id of this CreateInstanceCommand.  # noqa: E501

        Type of an instance  # noqa: E501

        :return: The type_id of this CreateInstanceCommand.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this CreateInstanceCommand.

        Type of an instance  # noqa: E501

        :param type_id: The type_id of this CreateInstanceCommand.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def freemium(self):
        """Gets the freemium of this CreateInstanceCommand.  # noqa: E501

        Freemium  # noqa: E501

        :return: The freemium of this CreateInstanceCommand.  # noqa: E501
        :rtype: bool
        """
        return self._freemium

    @freemium.setter
    def freemium(self, freemium):
        """Sets the freemium of this CreateInstanceCommand.

        Freemium  # noqa: E501

        :param freemium: The freemium of this CreateInstanceCommand.  # noqa: E501
        :type: bool
        """

        self._freemium = freemium

    @property
    def init_script(self):
        """Gets the init_script of this CreateInstanceCommand.  # noqa: E501

        InitScript  # noqa: E501

        :return: The init_script of this CreateInstanceCommand.  # noqa: E501
        :rtype: str
        """
        return self._init_script

    @init_script.setter
    def init_script(self, init_script):
        """Sets the init_script of this CreateInstanceCommand.

        InitScript  # noqa: E501

        :param init_script: The init_script of this CreateInstanceCommand.  # noqa: E501
        :type: str
        """

        self._init_script = init_script

    @property
    def without_public_ip(self):
        """Gets the without_public_ip of this CreateInstanceCommand.  # noqa: E501

        Freemium  # noqa: E501

        :return: The without_public_ip of this CreateInstanceCommand.  # noqa: E501
        :rtype: bool
        """
        return self._without_public_ip

    @without_public_ip.setter
    def without_public_ip(self, without_public_ip):
        """Sets the without_public_ip of this CreateInstanceCommand.

        Freemium  # noqa: E501

        :param without_public_ip: The without_public_ip of this CreateInstanceCommand.  # noqa: E501
        :type: bool
        """

        self._without_public_ip = without_public_ip

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
        if issubclass(CreateInstanceCommand, dict):
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
        if not isinstance(other, CreateInstanceCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInstanceCommand):
            return True

        return self.to_dict() != other.to_dict()
