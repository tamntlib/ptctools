# PortainerEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amt_device_guid** | **str** | The identifier of the AMT Device associated with this environment(endpoint) | [optional] 
**authorized_teams** | **List[int]** |  | [optional] 
**authorized_users** | **List[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**azure_credentials** | [**PortainerAzureCredentials**](PortainerAzureCredentials.md) |  | [optional] 
**compose_syntax_max_version** | **str** | Maximum version of docker-compose | [optional] 
**container_engine** | **str** | ContainerEngine represents the container engine type. This can be &#39;docker&#39; or &#39;podman&#39; when interacting directly with these environmentes, otherwise &#39;&#39; for kubernetes environments. | [optional] 
**edge_checkin_interval** | **int** | The check in interval for edge agent (in seconds) | [optional] 
**edge_id** | **str** | The identifier of the edge agent associated with this environment(endpoint) | [optional] 
**edge_key** | **str** | The key which is used to map the agent to Portainer | [optional] 
**enable_gpu_management** | **bool** |  | [optional] 
**gpus** | [**List[PortainerPair]**](PortainerPair.md) |  | [optional] 
**group_id** | **int** | Environment(Endpoint) group identifier | [optional] 
**heartbeat** | **bool** | Heartbeat indicates the heartbeat status of an edge environment | [optional] 
**id** | **int** | Environment(Endpoint) Identifier | [optional] 
**is_edge_device** | **bool** | Deprecated v2.18 | [optional] 
**kubernetes** | [**PortainerKubernetesData**](PortainerKubernetesData.md) | Associated Kubernetes data | [optional] 
**name** | **str** | Environment(Endpoint) name | [optional] 
**post_init_migrations** | [**PortainerEndpointPostInitMigrations**](PortainerEndpointPostInitMigrations.md) | Whether we need to run any \&quot;post init migrations\&quot;. | [optional] 
**public_url** | **str** | URL or IP address where exposed containers will be reachable | [optional] 
**snapshots** | [**List[PortainerDockerSnapshot]**](PortainerDockerSnapshot.md) | List of snapshots | [optional] 
**status** | [**PortainerEndpointStatus**](PortainerEndpointStatus.md) | The status of the environment(endpoint) (1 - up, 2 - down) | [optional] 
**tls** | **bool** | Deprecated fields Deprecated in DBVersion &#x3D;&#x3D; 4 | [optional] 
**tlsca_cert** | **str** |  | [optional] 
**tls_cert** | **str** |  | [optional] 
**tls_config** | [**PortainerTLSConfiguration**](PortainerTLSConfiguration.md) |  | [optional] 
**tls_key** | **str** |  | [optional] 
**tag_ids** | **List[int]** | List of tag identifiers to which this environment(endpoint) is associated | [optional] 
**tags** | **List[str]** | Deprecated in DBVersion &#x3D;&#x3D; 22 | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) | List of team identifiers authorized to connect to this environment(endpoint) | [optional] 
**type** | [**PortainerEndpointType**](PortainerEndpointType.md) | Environment(Endpoint) environment(endpoint) type. 1 for a Docker environment(endpoint), 2 for an agent on Docker environment(endpoint) or 3 for an Azure environment(endpoint). | [optional] 
**url** | **str** | URL or IP address of the Docker host associated to this environment(endpoint) | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) | List of user identifiers authorized to connect to this environment(endpoint) | [optional] 
**user_trusted** | **bool** | Whether the device has been trusted or not by the user | [optional] 
**agent** | [**PortainerEndpointAgent**](PortainerEndpointAgent.md) |  | [optional] 
**edge** | [**PortainerEnvironmentEdgeSettings**](PortainerEnvironmentEdgeSettings.md) |  | [optional] 
**last_check_in_date** | **int** | LastCheckInDate mark last check-in date on checkin | [optional] 
**query_date** | **int** | QueryDate of each query with the endpoints list | [optional] 
**security_settings** | [**PortainerEndpointSecuritySettings**](PortainerEndpointSecuritySettings.md) | Environment(Endpoint) specific security settings | [optional] 

## Example

```python
from openapi_client.models.portainer_endpoint import PortainerEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEndpoint from a JSON string
portainer_endpoint_instance = PortainerEndpoint.from_json(json)
# print the JSON string representation of the object
print(PortainerEndpoint.to_json())

# convert the object into a dict
portainer_endpoint_dict = portainer_endpoint_instance.to_dict()
# create an instance of PortainerEndpoint from a dict
portainer_endpoint_from_dict = PortainerEndpoint.from_dict(portainer_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


