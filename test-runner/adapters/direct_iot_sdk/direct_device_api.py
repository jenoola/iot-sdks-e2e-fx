# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from adapters.abstract_device_api import AbstractDeviceApi
from azure.iot.hub.devicesdk import DeviceClientSync
from azure.iot.hub.devicesdk.auth.authentication_provider_factory import from_connection_string

object_list = []


class DeviceApi(AbstractDeviceApi):
    def __init__(self):
        self.auth_provider = None
        self.client = None

    def connect(self, transport, connection_string, ca_certificate):
        print("connecting using " + transport)
        self.auth_provider = from_connection_string(connection_string)
        if ca_certificate and "cert" in ca_certificate:
            self.auth_provider.ca_cert = ca_certificate["cert"]
        self.client = DeviceClientSync.from_authentication_provider(self.auth_provider, transport)
        object_list.append(self)
        self.client.connect()

    def connect_async(self, transport, connection_string, ca_certificate):
        raise NotImplementedError

    def disconnect(self):
        if self in object_list:
            object_list.remove(self)

        self.client.disconnect()
        self.client = None

        self.auth_provider.disconnect()
        self.auth_provider = None

    def disconnect_async(self):
        raise NotImplementedError

    def send_event(self, body):
        raise NotImplementedError

    def send_event_async(self, body):
        raise NotImplementedError

    def enable_c2d(self):
        raise NotImplementedError

    def receive_c2d_async(self, body):
        raise NotImplementedError

    def enable_methods(self):
        raise NotImplementedError

    def roundtrip_method_async(self, method_name, status_code, request_payload, response_payload):
        raise NotImplementedError
