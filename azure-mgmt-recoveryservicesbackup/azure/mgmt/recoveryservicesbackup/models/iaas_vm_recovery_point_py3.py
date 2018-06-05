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

from .recovery_point_py3 import RecoveryPoint


class IaasVMRecoveryPoint(RecoveryPoint):
    """IaaS VM workload specific backup copy.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_type: Type of the backup copy.
    :type recovery_point_type: str
    :param recovery_point_time: Time at which this backup copy was created.
    :type recovery_point_time: datetime
    :param recovery_point_additional_info: Additional information associated
     with this backup copy.
    :type recovery_point_additional_info: str
    :param source_vm_storage_type: Storage type of the VM whose backup copy is
     created.
    :type source_vm_storage_type: str
    :param is_source_vm_encrypted: Identifies whether the VM was encrypted
     when the backup copy is created.
    :type is_source_vm_encrypted: bool
    :param key_and_secret: Required details for recovering an encrypted VM.
     Applicable only when IsSourceVMEncrypted is true.
    :type key_and_secret:
     ~azure.mgmt.recoveryservicesbackup.models.KeyAndSecretDetails
    :param is_instant_ilr_session_active: Is the session to recover items from
     this backup copy still active.
    :type is_instant_ilr_session_active: bool
    :param recovery_point_tier_details: Recovery point tier information.
    :type recovery_point_tier_details:
     list[~azure.mgmt.recoveryservicesbackup.models.RecoveryPointTierInformation]
    :param is_managed_virtual_machine: Whether VM is with Managed Disks
    :type is_managed_virtual_machine: bool
    :param virtual_machine_size: Virtual Machine Size
    :type virtual_machine_size: str
    :param original_storage_account_option: Original SA Option
    :type original_storage_account_option: bool
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_type': {'key': 'recoveryPointType', 'type': 'str'},
        'recovery_point_time': {'key': 'recoveryPointTime', 'type': 'iso-8601'},
        'recovery_point_additional_info': {'key': 'recoveryPointAdditionalInfo', 'type': 'str'},
        'source_vm_storage_type': {'key': 'sourceVMStorageType', 'type': 'str'},
        'is_source_vm_encrypted': {'key': 'isSourceVMEncrypted', 'type': 'bool'},
        'key_and_secret': {'key': 'keyAndSecret', 'type': 'KeyAndSecretDetails'},
        'is_instant_ilr_session_active': {'key': 'isInstantIlrSessionActive', 'type': 'bool'},
        'recovery_point_tier_details': {'key': 'recoveryPointTierDetails', 'type': '[RecoveryPointTierInformation]'},
        'is_managed_virtual_machine': {'key': 'isManagedVirtualMachine', 'type': 'bool'},
        'virtual_machine_size': {'key': 'virtualMachineSize', 'type': 'str'},
        'original_storage_account_option': {'key': 'originalStorageAccountOption', 'type': 'bool'},
    }

    def __init__(self, *, recovery_point_type: str=None, recovery_point_time=None, recovery_point_additional_info: str=None, source_vm_storage_type: str=None, is_source_vm_encrypted: bool=None, key_and_secret=None, is_instant_ilr_session_active: bool=None, recovery_point_tier_details=None, is_managed_virtual_machine: bool=None, virtual_machine_size: str=None, original_storage_account_option: bool=None, **kwargs) -> None:
        super(IaasVMRecoveryPoint, self).__init__(**kwargs)
        self.recovery_point_type = recovery_point_type
        self.recovery_point_time = recovery_point_time
        self.recovery_point_additional_info = recovery_point_additional_info
        self.source_vm_storage_type = source_vm_storage_type
        self.is_source_vm_encrypted = is_source_vm_encrypted
        self.key_and_secret = key_and_secret
        self.is_instant_ilr_session_active = is_instant_ilr_session_active
        self.recovery_point_tier_details = recovery_point_tier_details
        self.is_managed_virtual_machine = is_managed_virtual_machine
        self.virtual_machine_size = virtual_machine_size
        self.original_storage_account_option = original_storage_account_option
        self.object_type = 'IaasVMRecoveryPoint'