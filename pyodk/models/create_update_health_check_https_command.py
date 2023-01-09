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


class CreateUpdateHealthCheckHttpsCommand(object):
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
        'http_method_id': 'int',
        'content_regular_expression': 'str',
        'content_negative_regular_expression': 'str',
        'port': 'int',
        'timeout': 'int',
        'content': 'str',
        'content_type': 'str',
        'error_tolerance': 'int',
        'name': 'str',
        'address': 'str',
        'interval': 'int',
        'paused': 'bool',
        'locations_failover_enabled': 'bool',
        'notification_type_ids': 'list[int]',
        'notification_event_type_ids': 'list[int]',
        'notification_time_id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'http_method_id': 'HttpMethodId',
        'content_regular_expression': 'ContentRegularExpression',
        'content_negative_regular_expression': 'ContentNegativeRegularExpression',
        'port': 'Port',
        'timeout': 'Timeout',
        'content': 'Content',
        'content_type': 'ContentType',
        'error_tolerance': 'ErrorTolerance',
        'name': 'Name',
        'address': 'Address',
        'interval': 'Interval',
        'paused': 'Paused',
        'locations_failover_enabled': 'LocationsFailoverEnabled',
        'notification_type_ids': 'NotificationTypeIds',
        'notification_event_type_ids': 'NotificationEventTypeIds',
        'notification_time_id': 'NotificationTimeId',
        'description': 'Description'
    }

    def __init__(self, http_method_id=1440, content_regular_expression='', content_negative_regular_expression='', port=80, timeout=7000, content='', content_type='', error_tolerance=51, name='', address='', interval=60, paused=False, locations_failover_enabled=True, notification_type_ids=None, notification_event_type_ids=None, notification_time_id=1594, description=None, _configuration=None):  # noqa: E501
        """CreateUpdateHealthCheckHttpsCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._http_method_id = None
        self._content_regular_expression = None
        self._content_negative_regular_expression = None
        self._port = None
        self._timeout = None
        self._content = None
        self._content_type = None
        self._error_tolerance = None
        self._name = None
        self._address = None
        self._interval = None
        self._paused = None
        self._locations_failover_enabled = None
        self._notification_type_ids = None
        self._notification_event_type_ids = None
        self._notification_time_id = None
        self._description = None
        self.discriminator = None

        self.http_method_id = http_method_id
        if content_regular_expression is not None:
            self.content_regular_expression = content_regular_expression
        if content_negative_regular_expression is not None:
            self.content_negative_regular_expression = content_negative_regular_expression
        self.port = port
        self.timeout = timeout
        if content is not None:
            self.content = content
        if content_type is not None:
            self.content_type = content_type
        self.error_tolerance = error_tolerance
        self.name = name
        self.address = address
        self.interval = interval
        self.paused = paused
        self.locations_failover_enabled = locations_failover_enabled
        if notification_type_ids is not None:
            self.notification_type_ids = notification_type_ids
        if notification_event_type_ids is not None:
            self.notification_event_type_ids = notification_event_type_ids
        self.notification_time_id = notification_time_id
        if description is not None:
            self.description = description

    @property
    def http_method_id(self):
        """Gets the http_method_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Health check http method type (Dictionary 166)  # noqa: E501

        :return: The http_method_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._http_method_id

    @http_method_id.setter
    def http_method_id(self, http_method_id):
        """Sets the http_method_id of this CreateUpdateHealthCheckHttpsCommand.

        Health check http method type (Dictionary 166)  # noqa: E501

        :param http_method_id: The http_method_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and http_method_id is None:
            raise ValueError("Invalid value for `http_method_id`, must not be `None`")  # noqa: E501

        self._http_method_id = http_method_id

    @property
    def content_regular_expression(self):
        """Gets the content_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        The content has to match the expression (GET and POST methods only)  # noqa: E501

        :return: The content_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._content_regular_expression

    @content_regular_expression.setter
    def content_regular_expression(self, content_regular_expression):
        """Sets the content_regular_expression of this CreateUpdateHealthCheckHttpsCommand.

        The content has to match the expression (GET and POST methods only)  # noqa: E501

        :param content_regular_expression: The content_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """

        self._content_regular_expression = content_regular_expression

    @property
    def content_negative_regular_expression(self):
        """Gets the content_negative_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        The content cannot match the expression (GET and POST methods only)  # noqa: E501

        :return: The content_negative_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._content_negative_regular_expression

    @content_negative_regular_expression.setter
    def content_negative_regular_expression(self, content_negative_regular_expression):
        """Sets the content_negative_regular_expression of this CreateUpdateHealthCheckHttpsCommand.

        The content cannot match the expression (GET and POST methods only)  # noqa: E501

        :param content_negative_regular_expression: The content_negative_regular_expression of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """

        self._content_negative_regular_expression = content_negative_regular_expression

    @property
    def port(self):
        """Gets the port of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Port  # noqa: E501

        :return: The port of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CreateUpdateHealthCheckHttpsCommand.

        Port  # noqa: E501

        :param port: The port of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 0):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def timeout(self):
        """Gets the timeout of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Time the server has to complete the request in [ms]  # noqa: E501

        :return: The timeout of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateUpdateHealthCheckHttpsCommand.

        Time the server has to complete the request in [ms]  # noqa: E501

        :param timeout: The timeout of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and timeout is None:
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                timeout is not None and timeout > 120000):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `120000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                timeout is not None and timeout < 10):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `10`")  # noqa: E501

        self._timeout = timeout

    @property
    def content(self):
        """Gets the content of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Content  # noqa: E501

        :return: The content of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateUpdateHealthCheckHttpsCommand.

        Content  # noqa: E501

        :param content: The content of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_type(self):
        """Gets the content_type of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Content type  # noqa: E501

        :return: The content_type of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateUpdateHealthCheckHttpsCommand.

        Content type  # noqa: E501

        :param content_type: The content_type of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def error_tolerance(self):
        """Gets the error_tolerance of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        How many (%) locations have to report an error to consider it a breakdown  # noqa: E501

        :return: The error_tolerance of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._error_tolerance

    @error_tolerance.setter
    def error_tolerance(self, error_tolerance):
        """Sets the error_tolerance of this CreateUpdateHealthCheckHttpsCommand.

        How many (%) locations have to report an error to consider it a breakdown  # noqa: E501

        :param error_tolerance: The error_tolerance of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and error_tolerance is None:
            raise ValueError("Invalid value for `error_tolerance`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                error_tolerance is not None and error_tolerance > 100):  # noqa: E501
            raise ValueError("Invalid value for `error_tolerance`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                error_tolerance is not None and error_tolerance < 1):  # noqa: E501
            raise ValueError("Invalid value for `error_tolerance`, must be a value greater than or equal to `1`")  # noqa: E501

        self._error_tolerance = error_tolerance

    @property
    def name(self):
        """Gets the name of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Health check name  # noqa: E501

        :return: The name of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUpdateHealthCheckHttpsCommand.

        Health check name  # noqa: E501

        :param name: The name of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 2000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `2000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[^\/\\\\|<>%]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^\/\\\\|<>%]*$/`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        URL or IP address of the monitored service  # noqa: E501

        :return: The address of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateUpdateHealthCheckHttpsCommand.

        URL or IP address of the monitored service  # noqa: E501

        :param address: The address of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def interval(self):
        """Gets the interval of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Time interval between health checks, in seconds  # noqa: E501

        :return: The interval of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateUpdateHealthCheckHttpsCommand.

        Time interval between health checks, in seconds  # noqa: E501

        :param interval: The interval of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def paused(self):
        """Gets the paused of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Is paused  # noqa: E501

        :return: The paused of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this CreateUpdateHealthCheckHttpsCommand.

        Is paused  # noqa: E501

        :param paused: The paused of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and paused is None:
            raise ValueError("Invalid value for `paused`, must not be `None`")  # noqa: E501

        self._paused = paused

    @property
    def locations_failover_enabled(self):
        """Gets the locations_failover_enabled of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Use random substitute locations in case of location breakdown  # noqa: E501

        :return: The locations_failover_enabled of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: bool
        """
        return self._locations_failover_enabled

    @locations_failover_enabled.setter
    def locations_failover_enabled(self, locations_failover_enabled):
        """Sets the locations_failover_enabled of this CreateUpdateHealthCheckHttpsCommand.

        Use random substitute locations in case of location breakdown  # noqa: E501

        :param locations_failover_enabled: The locations_failover_enabled of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and locations_failover_enabled is None:
            raise ValueError("Invalid value for `locations_failover_enabled`, must not be `None`")  # noqa: E501

        self._locations_failover_enabled = locations_failover_enabled

    @property
    def notification_type_ids(self):
        """Gets the notification_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Notification types enabled for a health check  # noqa: E501

        :return: The notification_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._notification_type_ids

    @notification_type_ids.setter
    def notification_type_ids(self, notification_type_ids):
        """Sets the notification_type_ids of this CreateUpdateHealthCheckHttpsCommand.

        Notification types enabled for a health check  # noqa: E501

        :param notification_type_ids: The notification_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: list[int]
        """

        self._notification_type_ids = notification_type_ids

    @property
    def notification_event_type_ids(self):
        """Gets the notification_event_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Event types with enabled notification  # noqa: E501

        :return: The notification_event_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: list[int]
        """
        return self._notification_event_type_ids

    @notification_event_type_ids.setter
    def notification_event_type_ids(self, notification_event_type_ids):
        """Sets the notification_event_type_ids of this CreateUpdateHealthCheckHttpsCommand.

        Event types with enabled notification  # noqa: E501

        :param notification_event_type_ids: The notification_event_type_ids of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: list[int]
        """

        self._notification_event_type_ids = notification_event_type_ids

    @property
    def notification_time_id(self):
        """Gets the notification_time_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Time when notification is sent  # noqa: E501

        :return: The notification_time_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: int
        """
        return self._notification_time_id

    @notification_time_id.setter
    def notification_time_id(self, notification_time_id):
        """Sets the notification_time_id of this CreateUpdateHealthCheckHttpsCommand.

        Time when notification is sent  # noqa: E501

        :param notification_time_id: The notification_time_id of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and notification_time_id is None:
            raise ValueError("Invalid value for `notification_time_id`, must not be `None`")  # noqa: E501

        self._notification_time_id = notification_time_id

    @property
    def description(self):
        """Gets the description of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUpdateHealthCheckHttpsCommand.

        Description  # noqa: E501

        :param description: The description of this CreateUpdateHealthCheckHttpsCommand.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(CreateUpdateHealthCheckHttpsCommand, dict):
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
        if not isinstance(other, CreateUpdateHealthCheckHttpsCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUpdateHealthCheckHttpsCommand):
            return True

        return self.to_dict() != other.to_dict()
