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


class Role(Model):
    """Describes a role on the cluster.

    :param name: The name of the role.
    :type name: str
    :param min_instance_count: The minimum instance count of the cluster.
    :type min_instance_count: int
    :param target_instance_count: The instance count of the cluster.
    :type target_instance_count: int
    :param hardware_profile: The hardware profile.
    :type hardware_profile: ~azure.mgmt.hdinsight.models.HardwareProfile
    :param os_profile: The operating system profile.
    :type os_profile: ~azure.mgmt.hdinsight.models.OsProfile
    :param virtual_network_profile: The virtual network profile.
    :type virtual_network_profile:
     ~azure.mgmt.hdinsight.models.VirtualNetworkProfile
    :param data_disks_groups: The data disks groups for the role.
    :type data_disks_groups:
     list[~azure.mgmt.hdinsight.models.DataDisksGroups]
    :param script_actions: The list of script actions on the role.
    :type script_actions: list[~azure.mgmt.hdinsight.models.ScriptAction]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'min_instance_count': {'key': 'minInstanceCount', 'type': 'int'},
        'target_instance_count': {'key': 'targetInstanceCount', 'type': 'int'},
        'hardware_profile': {'key': 'hardwareProfile', 'type': 'HardwareProfile'},
        'os_profile': {'key': 'osProfile', 'type': 'OsProfile'},
        'virtual_network_profile': {'key': 'virtualNetworkProfile', 'type': 'VirtualNetworkProfile'},
        'data_disks_groups': {'key': 'dataDisksGroups', 'type': '[DataDisksGroups]'},
        'script_actions': {'key': 'scriptActions', 'type': '[ScriptAction]'},
    }

    def __init__(self, *, name: str=None, min_instance_count: int=None, target_instance_count: int=None, hardware_profile=None, os_profile=None, virtual_network_profile=None, data_disks_groups=None, script_actions=None, **kwargs) -> None:
        super(Role, self).__init__(**kwargs)
        self.name = name
        self.min_instance_count = min_instance_count
        self.target_instance_count = target_instance_count
        self.hardware_profile = hardware_profile
        self.os_profile = os_profile
        self.virtual_network_profile = virtual_network_profile
        self.data_disks_groups = data_disks_groups
        self.script_actions = script_actions
