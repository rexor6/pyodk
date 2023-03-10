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


class UpdateTemplateCommand(object):
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
        'template_descriptions': 'list[TemplateDescription]'
    }

    attribute_map = {
        'name': 'Name',
        'template_descriptions': 'TemplateDescriptions'
    }

    def __init__(self, name=None, template_descriptions=None, _configuration=None):  # noqa: E501
        """UpdateTemplateCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._template_descriptions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if template_descriptions is not None:
            self.template_descriptions = template_descriptions

    @property
    def name(self):
        """Gets the name of this UpdateTemplateCommand.  # noqa: E501

        Template name  # noqa: E501

        :return: The name of this UpdateTemplateCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTemplateCommand.

        Template name  # noqa: E501

        :param name: The name of this UpdateTemplateCommand.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 300):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `300`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def template_descriptions(self):
        """Gets the template_descriptions of this UpdateTemplateCommand.  # noqa: E501

        Template descriptions  # noqa: E501

        :return: The template_descriptions of this UpdateTemplateCommand.  # noqa: E501
        :rtype: list[TemplateDescription]
        """
        return self._template_descriptions

    @template_descriptions.setter
    def template_descriptions(self, template_descriptions):
        """Sets the template_descriptions of this UpdateTemplateCommand.

        Template descriptions  # noqa: E501

        :param template_descriptions: The template_descriptions of this UpdateTemplateCommand.  # noqa: E501
        :type: list[TemplateDescription]
        """

        self._template_descriptions = template_descriptions

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
        if issubclass(UpdateTemplateCommand, dict):
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
        if not isinstance(other, UpdateTemplateCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTemplateCommand):
            return True

        return self.to_dict() != other.to_dict()
