# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PurgeMessageQueueResult(Model):
    """Result of a device message queue purge operation.

    :param total_messages_purged:
    :type total_messages_purged: int
    :param device_id: The ID of the device whose messages are being purged.
    :type device_id: str
    :param module_id: The ID of the device whose messages are being purged.
    :type module_id: str
    """

    _attribute_map = {
        'total_messages_purged': {'key': 'totalMessagesPurged', 'type': 'int'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
    }

    def __init__(self, total_messages_purged=None, device_id=None, module_id=None):
        super(PurgeMessageQueueResult, self).__init__()
        self.total_messages_purged = total_messages_purged
        self.device_id = device_id
        self.module_id = module_id
