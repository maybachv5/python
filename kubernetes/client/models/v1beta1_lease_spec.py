# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1LeaseSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'acquire_time': 'datetime',
        'holder_identity': 'str',
        'lease_duration_seconds': 'int',
        'lease_transitions': 'int',
        'renew_time': 'datetime'
    }

    attribute_map = {
        'acquire_time': 'acquireTime',
        'holder_identity': 'holderIdentity',
        'lease_duration_seconds': 'leaseDurationSeconds',
        'lease_transitions': 'leaseTransitions',
        'renew_time': 'renewTime'
    }

    def __init__(self, acquire_time=None, holder_identity=None, lease_duration_seconds=None, lease_transitions=None, renew_time=None):
        """
        V1beta1LeaseSpec - a model defined in Swagger
        """

        self._acquire_time = None
        self._holder_identity = None
        self._lease_duration_seconds = None
        self._lease_transitions = None
        self._renew_time = None
        self.discriminator = None

        if acquire_time is not None:
          self.acquire_time = acquire_time
        if holder_identity is not None:
          self.holder_identity = holder_identity
        if lease_duration_seconds is not None:
          self.lease_duration_seconds = lease_duration_seconds
        if lease_transitions is not None:
          self.lease_transitions = lease_transitions
        if renew_time is not None:
          self.renew_time = renew_time

    @property
    def acquire_time(self):
        """
        Gets the acquire_time of this V1beta1LeaseSpec.
        acquireTime is a time when the current lease was acquired.

        :return: The acquire_time of this V1beta1LeaseSpec.
        :rtype: datetime
        """
        return self._acquire_time

    @acquire_time.setter
    def acquire_time(self, acquire_time):
        """
        Sets the acquire_time of this V1beta1LeaseSpec.
        acquireTime is a time when the current lease was acquired.

        :param acquire_time: The acquire_time of this V1beta1LeaseSpec.
        :type: datetime
        """

        self._acquire_time = acquire_time

    @property
    def holder_identity(self):
        """
        Gets the holder_identity of this V1beta1LeaseSpec.
        holderIdentity contains the identity of the holder of a current lease.

        :return: The holder_identity of this V1beta1LeaseSpec.
        :rtype: str
        """
        return self._holder_identity

    @holder_identity.setter
    def holder_identity(self, holder_identity):
        """
        Sets the holder_identity of this V1beta1LeaseSpec.
        holderIdentity contains the identity of the holder of a current lease.

        :param holder_identity: The holder_identity of this V1beta1LeaseSpec.
        :type: str
        """

        self._holder_identity = holder_identity

    @property
    def lease_duration_seconds(self):
        """
        Gets the lease_duration_seconds of this V1beta1LeaseSpec.
        leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.

        :return: The lease_duration_seconds of this V1beta1LeaseSpec.
        :rtype: int
        """
        return self._lease_duration_seconds

    @lease_duration_seconds.setter
    def lease_duration_seconds(self, lease_duration_seconds):
        """
        Sets the lease_duration_seconds of this V1beta1LeaseSpec.
        leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.

        :param lease_duration_seconds: The lease_duration_seconds of this V1beta1LeaseSpec.
        :type: int
        """

        self._lease_duration_seconds = lease_duration_seconds

    @property
    def lease_transitions(self):
        """
        Gets the lease_transitions of this V1beta1LeaseSpec.
        leaseTransitions is the number of transitions of a lease between holders.

        :return: The lease_transitions of this V1beta1LeaseSpec.
        :rtype: int
        """
        return self._lease_transitions

    @lease_transitions.setter
    def lease_transitions(self, lease_transitions):
        """
        Sets the lease_transitions of this V1beta1LeaseSpec.
        leaseTransitions is the number of transitions of a lease between holders.

        :param lease_transitions: The lease_transitions of this V1beta1LeaseSpec.
        :type: int
        """

        self._lease_transitions = lease_transitions

    @property
    def renew_time(self):
        """
        Gets the renew_time of this V1beta1LeaseSpec.
        renewTime is a time when the current holder of a lease has last updated the lease.

        :return: The renew_time of this V1beta1LeaseSpec.
        :rtype: datetime
        """
        return self._renew_time

    @renew_time.setter
    def renew_time(self, renew_time):
        """
        Sets the renew_time of this V1beta1LeaseSpec.
        renewTime is a time when the current holder of a lease has last updated the lease.

        :param renew_time: The renew_time of this V1beta1LeaseSpec.
        :type: datetime
        """

        self._renew_time = renew_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1LeaseSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
