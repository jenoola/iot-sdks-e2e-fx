# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Twin(Model):
    """Twin Representation.

    :param device_id: The deviceId uniquely identifies the device in the IoT
     hub's identity registry. A case-sensitive string (up to 128 char long) of
     ASCII 7-bit alphanumeric chars + {'-', ':', '.', '+', '%', '_', '#', '*',
     '?', '!', '(', ')', ',', '=', '@', ';', '$', '''}.
    :type device_id: str
    :param module_id: Gets and sets the Module Id.
    :type module_id: str
    :param tags: A JSON document read and written by the solution back end.
     Tags are not visible to device apps.
    :type tags: dict[str, object]
    :param properties: Gets and sets the Twin properties.
    :type properties: ~service20180630modified.models.TwinProperties
    :param etag: Twin's ETag
    :type etag: str
    :param version: Version for device twin, including tags and desired
     properties
    :type version: long
    :param device_etag: Device's ETag
    :type device_etag: str
    :param status: Gets the corresponding Device's Status. Possible values
     include: 'enabled', 'disabled'
    :type status: str or ~service20180630modified.models.enum
    :param status_reason: Reason, if any, for the corresponding Device to be
     in specified Status
    :type status_reason: str
    :param status_update_time: Time when the corresponding Device's Status was
     last updated
    :type status_update_time: datetime
    :param connection_state: Corresponding Device's ConnectionState. Possible
     values include: 'Disconnected', 'Connected'
    :type connection_state: str or ~service20180630modified.models.enum
    :param last_activity_time: The last time the device connected, received or
     sent a message. In ISO8601 datetime format in UTC, for example,
     2015-01-28T16:24:48.789Z. This does not update if the device uses the
     HTTP/1 protocol to perform messaging operations.
    :type last_activity_time: datetime
    :param cloud_to_device_message_count: Number of messages sent to the
     corresponding Device from the Cloud
    :type cloud_to_device_message_count: int
    :param authentication_type: Corresponding Device's authentication type.
     Possible values include: 'sas', 'selfSigned', 'certificateAuthority',
     'none'
    :type authentication_type: str or ~service20180630modified.models.enum
    :param x509_thumbprint: Corresponding Device's X509 thumbprint
    :type x509_thumbprint: ~service20180630modified.models.X509Thumbprint
    """

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{object}'},
        'properties': {'key': 'properties', 'type': 'TwinProperties'},
        'etag': {'key': 'etag', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'},
        'device_etag': {'key': 'deviceEtag', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_reason': {'key': 'statusReason', 'type': 'str'},
        'status_update_time': {'key': 'statusUpdateTime', 'type': 'iso-8601'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'int'},
        'authentication_type': {'key': 'authenticationType', 'type': 'str'},
        'x509_thumbprint': {'key': 'x509Thumbprint', 'type': 'X509Thumbprint'},
    }

    def __init__(self, device_id=None, module_id=None, tags=None, properties=None, etag=None, version=None, device_etag=None, status=None, status_reason=None, status_update_time=None, connection_state=None, last_activity_time=None, cloud_to_device_message_count=None, authentication_type=None, x509_thumbprint=None):
        super(Twin, self).__init__()
        self.device_id = device_id
        self.module_id = module_id
        self.tags = tags
        self.properties = properties
        self.etag = etag
        self.version = version
        self.device_etag = device_etag
        self.status = status
        self.status_reason = status_reason
        self.status_update_time = status_update_time
        self.connection_state = connection_state
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication_type = authentication_type
        self.x509_thumbprint = x509_thumbprint
