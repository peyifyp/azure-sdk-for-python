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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.storage_sync_services_operations import StorageSyncServicesOperations
from .operations.sync_groups_operations import SyncGroupsOperations
from .operations.cloud_endpoints_operations import CloudEndpointsOperations
from .operations.server_endpoints_operations import ServerEndpointsOperations
from .operations.registered_servers_operations import RegisteredServersOperations
from .operations.workflows_operations import WorkflowsOperations
from . import models


class StorageSyncManagementClientConfiguration(AzureConfiguration):
    """Configuration for StorageSyncManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://azure.microsoft.com'

        super(StorageSyncManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-storagesync/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class StorageSyncManagementClient(SDKClient):
    """Microsoft Storage Sync Service API

    :ivar config: Configuration for client.
    :vartype config: StorageSyncManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storagesync.operations.Operations
    :ivar storage_sync_services: StorageSyncServices operations
    :vartype storage_sync_services: azure.mgmt.storagesync.operations.StorageSyncServicesOperations
    :ivar sync_groups: SyncGroups operations
    :vartype sync_groups: azure.mgmt.storagesync.operations.SyncGroupsOperations
    :ivar cloud_endpoints: CloudEndpoints operations
    :vartype cloud_endpoints: azure.mgmt.storagesync.operations.CloudEndpointsOperations
    :ivar server_endpoints: ServerEndpoints operations
    :vartype server_endpoints: azure.mgmt.storagesync.operations.ServerEndpointsOperations
    :ivar registered_servers: RegisteredServers operations
    :vartype registered_servers: azure.mgmt.storagesync.operations.RegisteredServersOperations
    :ivar workflows: Workflows operations
    :vartype workflows: azure.mgmt.storagesync.operations.WorkflowsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = StorageSyncManagementClientConfiguration(credentials, subscription_id, base_url)
        super(StorageSyncManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-04-02'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_sync_services = StorageSyncServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sync_groups = SyncGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cloud_endpoints = CloudEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_endpoints = ServerEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registered_servers = RegisteredServersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workflows = WorkflowsOperations(
            self._client, self.config, self._serialize, self._deserialize)
