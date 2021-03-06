# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Module(Model):
    """Module identity on a device.

    :param module_id:
    :type module_id: str
    :param managed_by:
    :type managed_by: str
    :param device_id:
    :type device_id: str
    :param generation_id:
    :type generation_id: str
    :param etag:
    :type etag: str
    :param connection_state: Possible values include: 'Disconnected',
     'Connected'
    :type connection_state: str or ~service20180630.models.enum
    :param connection_state_updated_time:
    :type connection_state_updated_time: datetime
    :param last_activity_time:
    :type last_activity_time: datetime
    :param cloud_to_device_message_count:
    :type cloud_to_device_message_count: int
    :param authentication:
    :type authentication: ~service20180630.models.AuthenticationMechanism
    """

    _attribute_map = {
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'generation_id': {'key': 'generationId', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'connection_state_updated_time': {'key': 'connectionStateUpdatedTime', 'type': 'iso-8601'},
        'last_activity_time': {'key': 'lastActivityTime', 'type': 'iso-8601'},
        'cloud_to_device_message_count': {'key': 'cloudToDeviceMessageCount', 'type': 'int'},
        'authentication': {'key': 'authentication', 'type': 'AuthenticationMechanism'},
    }

    def __init__(self, module_id=None, managed_by=None, device_id=None, generation_id=None, etag=None, connection_state=None, connection_state_updated_time=None, last_activity_time=None, cloud_to_device_message_count=None, authentication=None):
        super(Module, self).__init__()
        self.module_id = module_id
        self.managed_by = managed_by
        self.device_id = device_id
        self.generation_id = generation_id
        self.etag = etag
        self.connection_state = connection_state
        self.connection_state_updated_time = connection_state_updated_time
        self.last_activity_time = last_activity_time
        self.cloud_to_device_message_count = cloud_to_device_message_count
        self.authentication = authentication
