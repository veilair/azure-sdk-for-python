# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ComputeManagementClientConfiguration
from .operations import CloudServiceRoleInstancesOperations
from .operations import CloudServiceRolesOperations
from .operations import CloudServicesOperations
from .operations import CloudServicesUpdateDomainOperations
from .. import models


class ComputeManagementClient(object):
    """Compute Client.

    :ivar cloud_service_role_instances: CloudServiceRoleInstancesOperations operations
    :vartype cloud_service_role_instances: azure.mgmt.compute.v2020_10_01_preview.aio.operations.CloudServiceRoleInstancesOperations
    :ivar cloud_service_roles: CloudServiceRolesOperations operations
    :vartype cloud_service_roles: azure.mgmt.compute.v2020_10_01_preview.aio.operations.CloudServiceRolesOperations
    :ivar cloud_services: CloudServicesOperations operations
    :vartype cloud_services: azure.mgmt.compute.v2020_10_01_preview.aio.operations.CloudServicesOperations
    :ivar cloud_services_update_domain: CloudServicesUpdateDomainOperations operations
    :vartype cloud_services_update_domain: azure.mgmt.compute.v2020_10_01_preview.aio.operations.CloudServicesUpdateDomainOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ComputeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.cloud_service_role_instances = CloudServiceRoleInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_service_roles = CloudServiceRolesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_services = CloudServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_services_update_domain = CloudServicesUpdateDomainOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ComputeManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)