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


class ContainerCodePackageProperties(Model):
    """Describes a container and its runtime properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the code package.
    :type name: str
    :param image: Required. The Container image to use.
    :type image: str
    :param image_registry_credential: Image registry credential.
    :type image_registry_credential:
     ~azure.servicefabric.models.ImageRegistryCredential
    :param entrypoint: Override for the default entry point in the container.
    :type entrypoint: str
    :param commands: Command array to execute within the container in exec
     form.
    :type commands: list[str]
    :param environment_variables: The environment variables to set in this
     container
    :type environment_variables:
     list[~azure.servicefabric.models.EnvironmentVariable]
    :param settings: The settings to set in this container. The setting file
     path can be fetched from environment variable "Fabric_SettingPath". The
     path for Windows container is "C:\\\\secrets". The path for Linux
     container is "/var/secrets".
    :type settings: list[~azure.servicefabric.models.Setting]
    :param labels: The labels to set in this container.
    :type labels: list[~azure.servicefabric.models.ContainerLabel]
    :param endpoints: The endpoints exposed by this container.
    :type endpoints: list[~azure.servicefabric.models.EndpointProperties]
    :param resources: Required. This type describes the resource requirements
     for a container or a service.
    :type resources: ~azure.servicefabric.models.ResourceRequirements
    :param volume_refs: The volumes to be attached to the container.
    :type volume_refs: list[~azure.servicefabric.models.ContainerVolume]
    :ivar instance_view: Runtime information of a container instance.
    :vartype instance_view: ~azure.servicefabric.models.ContainerInstanceView
    :param diagnostics: Reference to sinks in DiagnosticsDescription.
    :type diagnostics: ~azure.servicefabric.models.DiagnosticsRef
    """

    _validation = {
        'name': {'required': True},
        'image': {'required': True},
        'resources': {'required': True},
        'instance_view': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'image': {'key': 'image', 'type': 'str'},
        'image_registry_credential': {'key': 'imageRegistryCredential', 'type': 'ImageRegistryCredential'},
        'entrypoint': {'key': 'entrypoint', 'type': 'str'},
        'commands': {'key': 'commands', 'type': '[str]'},
        'environment_variables': {'key': 'environmentVariables', 'type': '[EnvironmentVariable]'},
        'settings': {'key': 'settings', 'type': '[Setting]'},
        'labels': {'key': 'labels', 'type': '[ContainerLabel]'},
        'endpoints': {'key': 'endpoints', 'type': '[EndpointProperties]'},
        'resources': {'key': 'resources', 'type': 'ResourceRequirements'},
        'volume_refs': {'key': 'volumeRefs', 'type': '[ContainerVolume]'},
        'instance_view': {'key': 'instanceView', 'type': 'ContainerInstanceView'},
        'diagnostics': {'key': 'diagnostics', 'type': 'DiagnosticsRef'},
    }

    def __init__(self, **kwargs):
        super(ContainerCodePackageProperties, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.image = kwargs.get('image', None)
        self.image_registry_credential = kwargs.get('image_registry_credential', None)
        self.entrypoint = kwargs.get('entrypoint', None)
        self.commands = kwargs.get('commands', None)
        self.environment_variables = kwargs.get('environment_variables', None)
        self.settings = kwargs.get('settings', None)
        self.labels = kwargs.get('labels', None)
        self.endpoints = kwargs.get('endpoints', None)
        self.resources = kwargs.get('resources', None)
        self.volume_refs = kwargs.get('volume_refs', None)
        self.instance_view = None
        self.diagnostics = kwargs.get('diagnostics', None)