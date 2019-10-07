# coding: utf-8

"""
    Communcations

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class StoryAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ooxml_automation_id': 'str',
        'outline': 'str',
        'outline_history': 'StoryOutlineHistory',
        'revision': 'int',
        'title': 'str'
    }

    attribute_map = {
        'ooxml_automation_id': 'ooxml_automation_id',
        'outline': 'outline',
        'outline_history': 'outline_history',
        'revision': 'revision',
        'title': 'title'
    }

    def __init__(self, ooxml_automation_id=None, outline=None, outline_history=None, revision=None, title=None):  # noqa: E501
        """StoryAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._ooxml_automation_id = None
        self._outline = None
        self._outline_history = None
        self._revision = None
        self._title = None
        self.discriminator = None

        if ooxml_automation_id is not None:
            self.ooxml_automation_id = ooxml_automation_id
        if outline is not None:
            self.outline = outline
        if outline_history is not None:
            self.outline_history = outline_history
        if revision is not None:
            self.revision = revision
        if title is not None:
            self.title = title

    @property
    def ooxml_automation_id(self):
        """Gets the ooxml_automation_id of this StoryAllOf.  # noqa: E501


        :return: The ooxml_automation_id of this StoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ooxml_automation_id

    @ooxml_automation_id.setter
    def ooxml_automation_id(self, ooxml_automation_id):
        """Sets the ooxml_automation_id of this StoryAllOf.


        :param ooxml_automation_id: The ooxml_automation_id of this StoryAllOf.  # noqa: E501
        :type: str
        """

        self._ooxml_automation_id = ooxml_automation_id

    @property
    def outline(self):
        """Gets the outline of this StoryAllOf.  # noqa: E501


        :return: The outline of this StoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this StoryAllOf.


        :param outline: The outline of this StoryAllOf.  # noqa: E501
        :type: str
        """

        self._outline = outline

    @property
    def outline_history(self):
        """Gets the outline_history of this StoryAllOf.  # noqa: E501


        :return: The outline_history of this StoryAllOf.  # noqa: E501
        :rtype: StoryOutlineHistory
        """
        return self._outline_history

    @outline_history.setter
    def outline_history(self, outline_history):
        """Sets the outline_history of this StoryAllOf.


        :param outline_history: The outline_history of this StoryAllOf.  # noqa: E501
        :type: StoryOutlineHistory
        """

        self._outline_history = outline_history

    @property
    def revision(self):
        """Gets the revision of this StoryAllOf.  # noqa: E501


        :return: The revision of this StoryAllOf.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this StoryAllOf.


        :param revision: The revision of this StoryAllOf.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def title(self):
        """Gets the title of this StoryAllOf.  # noqa: E501


        :return: The title of this StoryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StoryAllOf.


        :param title: The title of this StoryAllOf.  # noqa: E501
        :type: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoryAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
