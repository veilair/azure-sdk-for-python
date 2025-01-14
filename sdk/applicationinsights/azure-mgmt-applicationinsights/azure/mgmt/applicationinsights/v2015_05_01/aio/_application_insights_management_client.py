# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ApplicationInsightsManagementClientConfiguration
from .operations import Operations
from .operations import AnnotationsOperations
from .operations import APIKeysOperations
from .operations import ExportConfigurationsOperations
from .operations import ComponentCurrentBillingFeaturesOperations
from .operations import ComponentQuotaStatusOperations
from .operations import ComponentFeatureCapabilitiesOperations
from .operations import ComponentAvailableFeaturesOperations
from .operations import ProactiveDetectionConfigurationsOperations
from .operations import ComponentsOperations
from .operations import WorkItemConfigurationsOperations
from .operations import FavoritesOperations
from .operations import WebTestLocationsOperations
from .operations import WebTestsOperations
from .operations import AnalyticsItemsOperations
from .operations import WorkbooksOperations
from .operations import MyWorkbooksOperations
from .. import models


class ApplicationInsightsManagementClient(object):
    """Composite Swagger for Application Insights Management Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.Operations
    :ivar annotations: AnnotationsOperations operations
    :vartype annotations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.AnnotationsOperations
    :ivar api_keys: APIKeysOperations operations
    :vartype api_keys: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.APIKeysOperations
    :ivar export_configurations: ExportConfigurationsOperations operations
    :vartype export_configurations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ExportConfigurationsOperations
    :ivar component_current_billing_features: ComponentCurrentBillingFeaturesOperations operations
    :vartype component_current_billing_features: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentCurrentBillingFeaturesOperations
    :ivar component_quota_status: ComponentQuotaStatusOperations operations
    :vartype component_quota_status: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentQuotaStatusOperations
    :ivar component_feature_capabilities: ComponentFeatureCapabilitiesOperations operations
    :vartype component_feature_capabilities: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentFeatureCapabilitiesOperations
    :ivar component_available_features: ComponentAvailableFeaturesOperations operations
    :vartype component_available_features: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentAvailableFeaturesOperations
    :ivar proactive_detection_configurations: ProactiveDetectionConfigurationsOperations operations
    :vartype proactive_detection_configurations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ProactiveDetectionConfigurationsOperations
    :ivar components: ComponentsOperations operations
    :vartype components: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentsOperations
    :ivar work_item_configurations: WorkItemConfigurationsOperations operations
    :vartype work_item_configurations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WorkItemConfigurationsOperations
    :ivar favorites: FavoritesOperations operations
    :vartype favorites: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.FavoritesOperations
    :ivar web_test_locations: WebTestLocationsOperations operations
    :vartype web_test_locations: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WebTestLocationsOperations
    :ivar web_tests: WebTestsOperations operations
    :vartype web_tests: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WebTestsOperations
    :ivar analytics_items: AnalyticsItemsOperations operations
    :vartype analytics_items: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.AnalyticsItemsOperations
    :ivar workbooks: WorkbooksOperations operations
    :vartype workbooks: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WorkbooksOperations
    :ivar my_workbooks: MyWorkbooksOperations operations
    :vartype my_workbooks: azure.mgmt.applicationinsights.v2015_05_01.aio.operations.MyWorkbooksOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
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
        self._config = ApplicationInsightsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.annotations = AnnotationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.api_keys = APIKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.export_configurations = ExportConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.component_current_billing_features = ComponentCurrentBillingFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.component_quota_status = ComponentQuotaStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.component_feature_capabilities = ComponentFeatureCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.component_available_features = ComponentAvailableFeaturesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.proactive_detection_configurations = ProactiveDetectionConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.components = ComponentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.work_item_configurations = WorkItemConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.favorites = FavoritesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_test_locations = WebTestLocationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_tests = WebTestsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.analytics_items = AnalyticsItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workbooks = WorkbooksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.my_workbooks = MyWorkbooksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ApplicationInsightsManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
