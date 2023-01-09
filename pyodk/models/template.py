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


class Template(object):
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
        'description': 'str',
        'version': 'str',
        'creation_date': 'datetime',
        'last_change_date': 'datetime',
        'creation_user': 'UserResource',
        'default_instance_type': 'DictionaryItem',
        'minimum_instance_type': 'DictionaryItem',
        'ethernet_controllers_number': 'int',
        'ethernet_controllers_type': 'DictionaryItem',
        'system_category': 'DictionaryItem',
        'owner_account': 'BaseResource',
        'publication_status': 'DictionaryItem',
        'disks': 'list[TemplateDisk]',
        'software': 'list[Software]',
        'template_type': 'DictionaryItem'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'description': 'Description',
        'version': 'Version',
        'creation_date': 'CreationDate',
        'last_change_date': 'LastChangeDate',
        'creation_user': 'CreationUser',
        'default_instance_type': 'DefaultInstanceType',
        'minimum_instance_type': 'MinimumInstanceType',
        'ethernet_controllers_number': 'EthernetControllersNumber',
        'ethernet_controllers_type': 'EthernetControllersType',
        'system_category': 'SystemCategory',
        'owner_account': 'OwnerAccount',
        'publication_status': 'PublicationStatus',
        'disks': 'Disks',
        'software': 'Software',
        'template_type': 'TemplateType'
    }

    def __init__(self, id=None, name=None, description=None, version=None, creation_date=None, last_change_date=None, creation_user=None, default_instance_type=None, minimum_instance_type=None, ethernet_controllers_number=None, ethernet_controllers_type=None, system_category=None, owner_account=None, publication_status=None, disks=None, software=None, template_type=None, _configuration=None):  # noqa: E501
        """Template - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._creation_date = None
        self._last_change_date = None
        self._creation_user = None
        self._default_instance_type = None
        self._minimum_instance_type = None
        self._ethernet_controllers_number = None
        self._ethernet_controllers_type = None
        self._system_category = None
        self._owner_account = None
        self._publication_status = None
        self._disks = None
        self._software = None
        self._template_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if creation_date is not None:
            self.creation_date = creation_date
        if last_change_date is not None:
            self.last_change_date = last_change_date
        if creation_user is not None:
            self.creation_user = creation_user
        if default_instance_type is not None:
            self.default_instance_type = default_instance_type
        if minimum_instance_type is not None:
            self.minimum_instance_type = minimum_instance_type
        if ethernet_controllers_number is not None:
            self.ethernet_controllers_number = ethernet_controllers_number
        if ethernet_controllers_type is not None:
            self.ethernet_controllers_type = ethernet_controllers_type
        if system_category is not None:
            self.system_category = system_category
        if owner_account is not None:
            self.owner_account = owner_account
        if publication_status is not None:
            self.publication_status = publication_status
        if disks is not None:
            self.disks = disks
        if software is not None:
            self.software = software
        if template_type is not None:
            self.template_type = template_type

    @property
    def id(self):
        """Gets the id of this Template.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this Template.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Template.

        Id  # noqa: E501

        :param id: The id of this Template.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Template.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Template.

        Name  # noqa: E501

        :param name: The name of this Template.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Template.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this Template.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Template.

        Description  # noqa: E501

        :param description: The description of this Template.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this Template.  # noqa: E501

        Version  # noqa: E501

        :return: The version of this Template.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Template.

        Version  # noqa: E501

        :param version: The version of this Template.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def creation_date(self):
        """Gets the creation_date of this Template.  # noqa: E501

        Creation date  # noqa: E501

        :return: The creation_date of this Template.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Template.

        Creation date  # noqa: E501

        :param creation_date: The creation_date of this Template.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_change_date(self):
        """Gets the last_change_date of this Template.  # noqa: E501

        Last change date  # noqa: E501

        :return: The last_change_date of this Template.  # noqa: E501
        :rtype: datetime
        """
        return self._last_change_date

    @last_change_date.setter
    def last_change_date(self, last_change_date):
        """Sets the last_change_date of this Template.

        Last change date  # noqa: E501

        :param last_change_date: The last_change_date of this Template.  # noqa: E501
        :type: datetime
        """

        self._last_change_date = last_change_date

    @property
    def creation_user(self):
        """Gets the creation_user of this Template.  # noqa: E501

        User who created the template  # noqa: E501

        :return: The creation_user of this Template.  # noqa: E501
        :rtype: UserResource
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        """Sets the creation_user of this Template.

        User who created the template  # noqa: E501

        :param creation_user: The creation_user of this Template.  # noqa: E501
        :type: UserResource
        """

        self._creation_user = creation_user

    @property
    def default_instance_type(self):
        """Gets the default_instance_type of this Template.  # noqa: E501

        Default instance type  # noqa: E501

        :return: The default_instance_type of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._default_instance_type

    @default_instance_type.setter
    def default_instance_type(self, default_instance_type):
        """Sets the default_instance_type of this Template.

        Default instance type  # noqa: E501

        :param default_instance_type: The default_instance_type of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._default_instance_type = default_instance_type

    @property
    def minimum_instance_type(self):
        """Gets the minimum_instance_type of this Template.  # noqa: E501

        Minimum instance type  # noqa: E501

        :return: The minimum_instance_type of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._minimum_instance_type

    @minimum_instance_type.setter
    def minimum_instance_type(self, minimum_instance_type):
        """Sets the minimum_instance_type of this Template.

        Minimum instance type  # noqa: E501

        :param minimum_instance_type: The minimum_instance_type of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._minimum_instance_type = minimum_instance_type

    @property
    def ethernet_controllers_number(self):
        """Gets the ethernet_controllers_number of this Template.  # noqa: E501

        Ethernet controllers number  # noqa: E501

        :return: The ethernet_controllers_number of this Template.  # noqa: E501
        :rtype: int
        """
        return self._ethernet_controllers_number

    @ethernet_controllers_number.setter
    def ethernet_controllers_number(self, ethernet_controllers_number):
        """Sets the ethernet_controllers_number of this Template.

        Ethernet controllers number  # noqa: E501

        :param ethernet_controllers_number: The ethernet_controllers_number of this Template.  # noqa: E501
        :type: int
        """

        self._ethernet_controllers_number = ethernet_controllers_number

    @property
    def ethernet_controllers_type(self):
        """Gets the ethernet_controllers_type of this Template.  # noqa: E501

        Ethernet controllers type  # noqa: E501

        :return: The ethernet_controllers_type of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._ethernet_controllers_type

    @ethernet_controllers_type.setter
    def ethernet_controllers_type(self, ethernet_controllers_type):
        """Sets the ethernet_controllers_type of this Template.

        Ethernet controllers type  # noqa: E501

        :param ethernet_controllers_type: The ethernet_controllers_type of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._ethernet_controllers_type = ethernet_controllers_type

    @property
    def system_category(self):
        """Gets the system_category of this Template.  # noqa: E501

        System category  # noqa: E501

        :return: The system_category of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._system_category

    @system_category.setter
    def system_category(self, system_category):
        """Sets the system_category of this Template.

        System category  # noqa: E501

        :param system_category: The system_category of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._system_category = system_category

    @property
    def owner_account(self):
        """Gets the owner_account of this Template.  # noqa: E501

        Owner account  # noqa: E501

        :return: The owner_account of this Template.  # noqa: E501
        :rtype: BaseResource
        """
        return self._owner_account

    @owner_account.setter
    def owner_account(self, owner_account):
        """Sets the owner_account of this Template.

        Owner account  # noqa: E501

        :param owner_account: The owner_account of this Template.  # noqa: E501
        :type: BaseResource
        """

        self._owner_account = owner_account

    @property
    def publication_status(self):
        """Gets the publication_status of this Template.  # noqa: E501

        Publication status  # noqa: E501

        :return: The publication_status of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._publication_status

    @publication_status.setter
    def publication_status(self, publication_status):
        """Sets the publication_status of this Template.

        Publication status  # noqa: E501

        :param publication_status: The publication_status of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._publication_status = publication_status

    @property
    def disks(self):
        """Gets the disks of this Template.  # noqa: E501

        Disks  # noqa: E501

        :return: The disks of this Template.  # noqa: E501
        :rtype: list[TemplateDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Template.

        Disks  # noqa: E501

        :param disks: The disks of this Template.  # noqa: E501
        :type: list[TemplateDisk]
        """

        self._disks = disks

    @property
    def software(self):
        """Gets the software of this Template.  # noqa: E501

        Softwares  # noqa: E501

        :return: The software of this Template.  # noqa: E501
        :rtype: list[Software]
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this Template.

        Softwares  # noqa: E501

        :param software: The software of this Template.  # noqa: E501
        :type: list[Software]
        """

        self._software = software

    @property
    def template_type(self):
        """Gets the template_type of this Template.  # noqa: E501

        Template type  # noqa: E501

        :return: The template_type of this Template.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this Template.

        Template type  # noqa: E501

        :param template_type: The template_type of this Template.  # noqa: E501
        :type: DictionaryItem
        """

        self._template_type = template_type

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
        if issubclass(Template, dict):
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
        if not isinstance(other, Template):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Template):
            return True

        return self.to_dict() != other.to_dict()
