# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IpAddress(Model):
    """Specifies the IP address of the network interaface.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar ip_address: Specifies the IP address of the network interface.
    :vartype ip_address: str
    """

    _validation = {
        'ip_address': {'readonly': True},
    }

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(IpAddress, self).__init__(**kwargs)
        self.ip_address = None
