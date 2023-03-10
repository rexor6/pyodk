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


class HealthCheckDns(object):
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
        'timeout': 'int',
        'record_type': 'DictionaryItem',
        'query_domain': 'str',
        'expected_response_value': 'str',
        'recurse': 'bool',
        'notification_types': 'list[DictionaryItem]',
        'notification_event_types': 'list[DictionaryItem]',
        'notification_time': 'DictionaryItem',
        'locations_failover_enabled': 'bool',
        'error_tolerance': 'int',
        'id': 'int',
        'interval': 'int',
        'name': 'str',
        'address': 'str',
        'service_type': 'DictionaryItem',
        'state': 'DictionaryItem',
        'details_location': 'str',
        'paused': 'bool',
        'suspended': 'bool',
        'last_invalid_check': 'datetime',
        'last_valid_check': 'datetime',
        'description': 'str'
    }

    attribute_map = {
        'timeout': 'Timeout',
        'record_type': 'RecordType',
        'query_domain': 'QueryDomain',
        'expected_response_value': 'ExpectedResponseValue',
        'recurse': 'Recurse',
        'notification_types': 'NotificationTypes',
        'notification_event_types': 'NotificationEventTypes',
        'notification_time': 'NotificationTime',
        'locations_failover_enabled': 'LocationsFailoverEnabled',
        'error_tolerance': 'ErrorTolerance',
        'id': 'Id',
        'interval': 'Interval',
        'name': 'Name',
        'address': 'Address',
        'service_type': 'ServiceType',
        'state': 'State',
        'details_location': 'DetailsLocation',
        'paused': 'Paused',
        'suspended': 'Suspended',
        'last_invalid_check': 'LastInvalidCheck',
        'last_valid_check': 'LastValidCheck',
        'description': 'Description'
    }

    def __init__(self, timeout=None, record_type=None, query_domain=None, expected_response_value=None, recurse=None, notification_types=None, notification_event_types=None, notification_time=None, locations_failover_enabled=None, error_tolerance=None, id=None, interval=None, name=None, address=None, service_type=None, state=None, details_location=None, paused=None, suspended=None, last_invalid_check=None, last_valid_check=None, description=None, _configuration=None):  # noqa: E501
        """HealthCheckDns - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._timeout = None
        self._record_type = None
        self._query_domain = None
        self._expected_response_value = None
        self._recurse = None
        self._notification_types = None
        self._notification_event_types = None
        self._notification_time = None
        self._locations_failover_enabled = None
        self._error_tolerance = None
        self._id = None
        self._interval = None
        self._name = None
        self._address = None
        self._service_type = None
        self._state = None
        self._details_location = None
        self._paused = None
        self._suspended = None
        self._last_invalid_check = None
        self._last_valid_check = None
        self._description = None
        self.discriminator = None

        if timeout is not None:
            self.timeout = timeout
        if record_type is not None:
            self.record_type = record_type
        if query_domain is not None:
            self.query_domain = query_domain
        if expected_response_value is not None:
            self.expected_response_value = expected_response_value
        if recurse is not None:
            self.recurse = recurse
        if notification_types is not None:
            self.notification_types = notification_types
        if notification_event_types is not None:
            self.notification_event_types = notification_event_types
        if notification_time is not None:
            self.notification_time = notification_time
        if locations_failover_enabled is not None:
            self.locations_failover_enabled = locations_failover_enabled
        if error_tolerance is not None:
            self.error_tolerance = error_tolerance
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if service_type is not None:
            self.service_type = service_type
        if state is not None:
            self.state = state
        if details_location is not None:
            self.details_location = details_location
        if paused is not None:
            self.paused = paused
        if suspended is not None:
            self.suspended = suspended
        if last_invalid_check is not None:
            self.last_invalid_check = last_invalid_check
        if last_valid_check is not None:
            self.last_valid_check = last_valid_check
        if description is not None:
            self.description = description

    @property
    def timeout(self):
        """Gets the timeout of this HealthCheckDns.  # noqa: E501

        Timeout  # noqa: E501

        :return: The timeout of this HealthCheckDns.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthCheckDns.

        Timeout  # noqa: E501

        :param timeout: The timeout of this HealthCheckDns.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def record_type(self):
        """Gets the record_type of this HealthCheckDns.  # noqa: E501

        Record type  # noqa: E501

        :return: The record_type of this HealthCheckDns.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this HealthCheckDns.

        Record type  # noqa: E501

        :param record_type: The record_type of this HealthCheckDns.  # noqa: E501
        :type: DictionaryItem
        """

        self._record_type = record_type

    @property
    def query_domain(self):
        """Gets the query_domain of this HealthCheckDns.  # noqa: E501

        Query domain  # noqa: E501

        :return: The query_domain of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._query_domain

    @query_domain.setter
    def query_domain(self, query_domain):
        """Sets the query_domain of this HealthCheckDns.

        Query domain  # noqa: E501

        :param query_domain: The query_domain of this HealthCheckDns.  # noqa: E501
        :type: str
        """

        self._query_domain = query_domain

    @property
    def expected_response_value(self):
        """Gets the expected_response_value of this HealthCheckDns.  # noqa: E501

        Expected DNS record value  # noqa: E501

        :return: The expected_response_value of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._expected_response_value

    @expected_response_value.setter
    def expected_response_value(self, expected_response_value):
        """Sets the expected_response_value of this HealthCheckDns.

        Expected DNS record value  # noqa: E501

        :param expected_response_value: The expected_response_value of this HealthCheckDns.  # noqa: E501
        :type: str
        """

        self._expected_response_value = expected_response_value

    @property
    def recurse(self):
        """Gets the recurse of this HealthCheckDns.  # noqa: E501

        Recursive query  # noqa: E501

        :return: The recurse of this HealthCheckDns.  # noqa: E501
        :rtype: bool
        """
        return self._recurse

    @recurse.setter
    def recurse(self, recurse):
        """Sets the recurse of this HealthCheckDns.

        Recursive query  # noqa: E501

        :param recurse: The recurse of this HealthCheckDns.  # noqa: E501
        :type: bool
        """

        self._recurse = recurse

    @property
    def notification_types(self):
        """Gets the notification_types of this HealthCheckDns.  # noqa: E501

        Notification types enabled for a health check  # noqa: E501

        :return: The notification_types of this HealthCheckDns.  # noqa: E501
        :rtype: list[DictionaryItem]
        """
        return self._notification_types

    @notification_types.setter
    def notification_types(self, notification_types):
        """Sets the notification_types of this HealthCheckDns.

        Notification types enabled for a health check  # noqa: E501

        :param notification_types: The notification_types of this HealthCheckDns.  # noqa: E501
        :type: list[DictionaryItem]
        """

        self._notification_types = notification_types

    @property
    def notification_event_types(self):
        """Gets the notification_event_types of this HealthCheckDns.  # noqa: E501

        Event types with enabled notification  # noqa: E501

        :return: The notification_event_types of this HealthCheckDns.  # noqa: E501
        :rtype: list[DictionaryItem]
        """
        return self._notification_event_types

    @notification_event_types.setter
    def notification_event_types(self, notification_event_types):
        """Sets the notification_event_types of this HealthCheckDns.

        Event types with enabled notification  # noqa: E501

        :param notification_event_types: The notification_event_types of this HealthCheckDns.  # noqa: E501
        :type: list[DictionaryItem]
        """

        self._notification_event_types = notification_event_types

    @property
    def notification_time(self):
        """Gets the notification_time of this HealthCheckDns.  # noqa: E501

        Time when notification is sent  # noqa: E501

        :return: The notification_time of this HealthCheckDns.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._notification_time

    @notification_time.setter
    def notification_time(self, notification_time):
        """Sets the notification_time of this HealthCheckDns.

        Time when notification is sent  # noqa: E501

        :param notification_time: The notification_time of this HealthCheckDns.  # noqa: E501
        :type: DictionaryItem
        """

        self._notification_time = notification_time

    @property
    def locations_failover_enabled(self):
        """Gets the locations_failover_enabled of this HealthCheckDns.  # noqa: E501

        Use random substitute locations in case of location breakdown  # noqa: E501

        :return: The locations_failover_enabled of this HealthCheckDns.  # noqa: E501
        :rtype: bool
        """
        return self._locations_failover_enabled

    @locations_failover_enabled.setter
    def locations_failover_enabled(self, locations_failover_enabled):
        """Sets the locations_failover_enabled of this HealthCheckDns.

        Use random substitute locations in case of location breakdown  # noqa: E501

        :param locations_failover_enabled: The locations_failover_enabled of this HealthCheckDns.  # noqa: E501
        :type: bool
        """

        self._locations_failover_enabled = locations_failover_enabled

    @property
    def error_tolerance(self):
        """Gets the error_tolerance of this HealthCheckDns.  # noqa: E501

        How many (%) locations have to report an error to consider it a breakdown  # noqa: E501

        :return: The error_tolerance of this HealthCheckDns.  # noqa: E501
        :rtype: int
        """
        return self._error_tolerance

    @error_tolerance.setter
    def error_tolerance(self, error_tolerance):
        """Sets the error_tolerance of this HealthCheckDns.

        How many (%) locations have to report an error to consider it a breakdown  # noqa: E501

        :param error_tolerance: The error_tolerance of this HealthCheckDns.  # noqa: E501
        :type: int
        """

        self._error_tolerance = error_tolerance

    @property
    def id(self):
        """Gets the id of this HealthCheckDns.  # noqa: E501

        Id  # noqa: E501

        :return: The id of this HealthCheckDns.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthCheckDns.

        Id  # noqa: E501

        :param id: The id of this HealthCheckDns.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this HealthCheckDns.  # noqa: E501

        Interval  # noqa: E501

        :return: The interval of this HealthCheckDns.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this HealthCheckDns.

        Interval  # noqa: E501

        :param interval: The interval of this HealthCheckDns.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def name(self):
        """Gets the name of this HealthCheckDns.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthCheckDns.

        Name  # noqa: E501

        :param name: The name of this HealthCheckDns.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this HealthCheckDns.  # noqa: E501

        Address  # noqa: E501

        :return: The address of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this HealthCheckDns.

        Address  # noqa: E501

        :param address: The address of this HealthCheckDns.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def service_type(self):
        """Gets the service_type of this HealthCheckDns.  # noqa: E501

        Type  # noqa: E501

        :return: The service_type of this HealthCheckDns.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this HealthCheckDns.

        Type  # noqa: E501

        :param service_type: The service_type of this HealthCheckDns.  # noqa: E501
        :type: DictionaryItem
        """

        self._service_type = service_type

    @property
    def state(self):
        """Gets the state of this HealthCheckDns.  # noqa: E501

        State  # noqa: E501

        :return: The state of this HealthCheckDns.  # noqa: E501
        :rtype: DictionaryItem
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this HealthCheckDns.

        State  # noqa: E501

        :param state: The state of this HealthCheckDns.  # noqa: E501
        :type: DictionaryItem
        """

        self._state = state

    @property
    def details_location(self):
        """Gets the details_location of this HealthCheckDns.  # noqa: E501

        Details url  # noqa: E501

        :return: The details_location of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._details_location

    @details_location.setter
    def details_location(self, details_location):
        """Sets the details_location of this HealthCheckDns.

        Details url  # noqa: E501

        :param details_location: The details_location of this HealthCheckDns.  # noqa: E501
        :type: str
        """

        self._details_location = details_location

    @property
    def paused(self):
        """Gets the paused of this HealthCheckDns.  # noqa: E501

        Is paused  # noqa: E501

        :return: The paused of this HealthCheckDns.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this HealthCheckDns.

        Is paused  # noqa: E501

        :param paused: The paused of this HealthCheckDns.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def suspended(self):
        """Gets the suspended of this HealthCheckDns.  # noqa: E501

        Is suspended  # noqa: E501

        :return: The suspended of this HealthCheckDns.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this HealthCheckDns.

        Is suspended  # noqa: E501

        :param suspended: The suspended of this HealthCheckDns.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def last_invalid_check(self):
        """Gets the last_invalid_check of this HealthCheckDns.  # noqa: E501

        Last invalid check  # noqa: E501

        :return: The last_invalid_check of this HealthCheckDns.  # noqa: E501
        :rtype: datetime
        """
        return self._last_invalid_check

    @last_invalid_check.setter
    def last_invalid_check(self, last_invalid_check):
        """Sets the last_invalid_check of this HealthCheckDns.

        Last invalid check  # noqa: E501

        :param last_invalid_check: The last_invalid_check of this HealthCheckDns.  # noqa: E501
        :type: datetime
        """

        self._last_invalid_check = last_invalid_check

    @property
    def last_valid_check(self):
        """Gets the last_valid_check of this HealthCheckDns.  # noqa: E501

        Last valid check  # noqa: E501

        :return: The last_valid_check of this HealthCheckDns.  # noqa: E501
        :rtype: datetime
        """
        return self._last_valid_check

    @last_valid_check.setter
    def last_valid_check(self, last_valid_check):
        """Sets the last_valid_check of this HealthCheckDns.

        Last valid check  # noqa: E501

        :param last_valid_check: The last_valid_check of this HealthCheckDns.  # noqa: E501
        :type: datetime
        """

        self._last_valid_check = last_valid_check

    @property
    def description(self):
        """Gets the description of this HealthCheckDns.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this HealthCheckDns.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HealthCheckDns.

        Description  # noqa: E501

        :param description: The description of this HealthCheckDns.  # noqa: E501
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
        if issubclass(HealthCheckDns, dict):
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
        if not isinstance(other, HealthCheckDns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthCheckDns):
            return True

        return self.to_dict() != other.to_dict()
