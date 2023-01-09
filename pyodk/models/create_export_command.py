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


class CreateExportCommand(object):
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
        'name': 'str',
        'ocs_location': 'str',
        'ocs_project_id': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'ocs_location': 'OcsLocation',
        'ocs_project_id': 'OcsProjectId'
    }

    def __init__(self, name=None, ocs_location=None, ocs_project_id=None, _configuration=None):  # noqa: E501
        """CreateExportCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._ocs_location = None
        self._ocs_project_id = None
        self.discriminator = None

        self.name = name
        self.ocs_location = ocs_location
        self.ocs_project_id = ocs_project_id

    @property
    def name(self):
        """Gets the name of this CreateExportCommand.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this CreateExportCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateExportCommand.

        Name  # noqa: E501

        :param name: The name of this CreateExportCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 300):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[^\/\\\\|<>%]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^\/\\\\|<>%]*$/`")  # noqa: E501

        self._name = name

    @property
    def ocs_location(self):
        """Gets the ocs_location of this CreateExportCommand.  # noqa: E501

        OCS location  # noqa: E501

        :return: The ocs_location of this CreateExportCommand.  # noqa: E501
        :rtype: str
        """
        return self._ocs_location

    @ocs_location.setter
    def ocs_location(self, ocs_location):
        """Sets the ocs_location of this CreateExportCommand.

        OCS location  # noqa: E501

        :param ocs_location: The ocs_location of this CreateExportCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ocs_location is None:
            raise ValueError("Invalid value for `ocs_location`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ocs_location is not None and len(ocs_location) > 100):
            raise ValueError("Invalid value for `ocs_location`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ocs_location is not None and len(ocs_location) < 0):
            raise ValueError("Invalid value for `ocs_location`, length must be greater than or equal to `0`")  # noqa: E501

        self._ocs_location = ocs_location

    @property
    def ocs_project_id(self):
        """Gets the ocs_project_id of this CreateExportCommand.  # noqa: E501

        OCS Project Id  # noqa: E501

        :return: The ocs_project_id of this CreateExportCommand.  # noqa: E501
        :rtype: str
        """
        return self._ocs_project_id

    @ocs_project_id.setter
    def ocs_project_id(self, ocs_project_id):
        """Sets the ocs_project_id of this CreateExportCommand.

        OCS Project Id  # noqa: E501

        :param ocs_project_id: The ocs_project_id of this CreateExportCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ocs_project_id is None:
            raise ValueError("Invalid value for `ocs_project_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ocs_project_id is not None and len(ocs_project_id) > 50):
            raise ValueError("Invalid value for `ocs_project_id`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ocs_project_id is not None and len(ocs_project_id) < 0):
            raise ValueError("Invalid value for `ocs_project_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._ocs_project_id = ocs_project_id

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
        if issubclass(CreateExportCommand, dict):
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
        if not isinstance(other, CreateExportCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateExportCommand):
            return True

        return self.to_dict() != other.to_dict()
