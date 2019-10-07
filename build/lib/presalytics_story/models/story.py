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


class Story(object):
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
        'created_at': 'datetime',
        'created_by': 'str',
        'id': 'str',
        'updated_at': 'datetime',
        'updated_by': 'str',
        'ooxml_automation_id': 'str',
        'outline': 'str',
        'outline_history': 'StoryOutlineHistory',
        'revision': 'int',
        'title': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'id': 'id',
        'updated_at': 'updated_at',
        'updated_by': 'updated_by',
        'ooxml_automation_id': 'ooxml_automation_id',
        'outline': 'outline',
        'outline_history': 'outline_history',
        'revision': 'revision',
        'title': 'title'
    }

    def __init__(self, created_at=None, created_by=None, id=None, updated_at=None, updated_by=None, ooxml_automation_id=None, outline=None, outline_history=None, revision=None, title=None):  # noqa: E501
        """Story - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._created_by = None
        self._id = None
        self._updated_at = None
        self._updated_by = None
        self._ooxml_automation_id = None
        self._outline = None
        self._outline_history = None
        self._revision = None
        self._title = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if id is not None:
            self.id = id
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
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
    def created_at(self):
        """Gets the created_at of this Story.  # noqa: E501


        :return: The created_at of this Story.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Story.


        :param created_at: The created_at of this Story.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Story.  # noqa: E501


        :return: The created_by of this Story.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Story.


        :param created_by: The created_by of this Story.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def id(self):
        """Gets the id of this Story.  # noqa: E501


        :return: The id of this Story.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Story.


        :param id: The id of this Story.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this Story.  # noqa: E501


        :return: The updated_at of this Story.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Story.


        :param updated_at: The updated_at of this Story.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Story.  # noqa: E501


        :return: The updated_by of this Story.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Story.


        :param updated_by: The updated_by of this Story.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def ooxml_automation_id(self):
        """Gets the ooxml_automation_id of this Story.  # noqa: E501


        :return: The ooxml_automation_id of this Story.  # noqa: E501
        :rtype: str
        """
        return self._ooxml_automation_id

    @ooxml_automation_id.setter
    def ooxml_automation_id(self, ooxml_automation_id):
        """Sets the ooxml_automation_id of this Story.


        :param ooxml_automation_id: The ooxml_automation_id of this Story.  # noqa: E501
        :type: str
        """

        self._ooxml_automation_id = ooxml_automation_id

    @property
    def outline(self):
        """Gets the outline of this Story.  # noqa: E501


        :return: The outline of this Story.  # noqa: E501
        :rtype: str
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this Story.


        :param outline: The outline of this Story.  # noqa: E501
        :type: str
        """

        self._outline = outline

    @property
    def outline_history(self):
        """Gets the outline_history of this Story.  # noqa: E501


        :return: The outline_history of this Story.  # noqa: E501
        :rtype: StoryOutlineHistory
        """
        return self._outline_history

    @outline_history.setter
    def outline_history(self, outline_history):
        """Sets the outline_history of this Story.


        :param outline_history: The outline_history of this Story.  # noqa: E501
        :type: StoryOutlineHistory
        """

        self._outline_history = outline_history

    @property
    def revision(self):
        """Gets the revision of this Story.  # noqa: E501


        :return: The revision of this Story.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Story.


        :param revision: The revision of this Story.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def title(self):
        """Gets the title of this Story.  # noqa: E501


        :return: The title of this Story.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Story.


        :param title: The title of this Story.  # noqa: E501
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
        if not isinstance(other, Story):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
