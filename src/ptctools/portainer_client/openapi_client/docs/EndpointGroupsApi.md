# openapi_client.EndpointGroupsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_group_add_endpoint**](EndpointGroupsApi.md#endpoint_group_add_endpoint) | **PUT** /endpoint_groups/{id}/endpoints/{endpointId} | Add an environment(endpoint) to an environment(endpoint) group
[**endpoint_group_delete**](EndpointGroupsApi.md#endpoint_group_delete) | **DELETE** /endpoint_groups/{id} | Remove an environment(endpoint) group
[**endpoint_group_delete_endpoint**](EndpointGroupsApi.md#endpoint_group_delete_endpoint) | **DELETE** /endpoint_groups/{id}/endpoints/{endpointId} | Removes environment(endpoint) from an environment(endpoint) group
[**endpoint_group_list**](EndpointGroupsApi.md#endpoint_group_list) | **GET** /endpoint_groups | List Environment(Endpoint) groups
[**endpoint_group_update**](EndpointGroupsApi.md#endpoint_group_update) | **PUT** /endpoint_groups/{id} | Update an environment(endpoint) group
[**endpoint_groups_id_get**](EndpointGroupsApi.md#endpoint_groups_id_get) | **GET** /endpoint_groups/{id} | Inspect an Environment(Endpoint) group
[**endpoint_groups_post**](EndpointGroupsApi.md#endpoint_groups_post) | **POST** /endpoint_groups | Create an Environment(Endpoint) Group


# **endpoint_group_add_endpoint**
> endpoint_group_add_endpoint(id, endpoint_id)

Add an environment(endpoint) to an environment(endpoint) group

Add an environment(endpoint) to an environment(endpoint) group
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    id = 56 # int | EndpointGroup identifier
    endpoint_id = 56 # int | Environment(Endpoint) identifier

    try:
        # Add an environment(endpoint) to an environment(endpoint) group
        api_instance.endpoint_group_add_endpoint(id, endpoint_id)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_group_add_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**404** | EndpointGroup not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete**
> endpoint_group_delete(id)

Remove an environment(endpoint) group

Remove an environment(endpoint) group.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    id = 56 # int | EndpointGroup identifier

    try:
        # Remove an environment(endpoint) group
        api_instance.endpoint_group_delete(id)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_group_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**404** | EndpointGroup not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_delete_endpoint**
> endpoint_group_delete_endpoint(id, endpoint_id)

Removes environment(endpoint) from an environment(endpoint) group

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    id = 56 # int | EndpointGroup identifier
    endpoint_id = 56 # int | Environment(Endpoint) identifier

    try:
        # Removes environment(endpoint) from an environment(endpoint) group
        api_instance.endpoint_group_delete_endpoint(id, endpoint_id)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_group_delete_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **endpoint_id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**404** | EndpointGroup not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_list**
> List[PortainerEndpointGroup] endpoint_group_list()

List Environment(Endpoint) groups

List all environment(endpoint) groups based on the current user authorizations. Will
return all environment(endpoint) groups if using an administrator account otherwise it will
only return authorized environment(endpoint) groups.
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_endpoint_group import PortainerEndpointGroup
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)

    try:
        # List Environment(Endpoint) groups
        api_response = api_instance.endpoint_group_list()
        print("The response of EndpointGroupsApi->endpoint_group_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_group_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortainerEndpointGroup]**](PortainerEndpointGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Environment(Endpoint) group |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_group_update**
> PortainerEndpointGroup endpoint_group_update(id, body)

Update an environment(endpoint) group

Update an environment(endpoint) group.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpointgroups_endpoint_group_update_payload import EndpointgroupsEndpointGroupUpdatePayload
from openapi_client.models.portainer_endpoint_group import PortainerEndpointGroup
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    id = 56 # int | EndpointGroup identifier
    body = openapi_client.EndpointgroupsEndpointGroupUpdatePayload() # EndpointgroupsEndpointGroupUpdatePayload | EndpointGroup details

    try:
        # Update an environment(endpoint) group
        api_response = api_instance.endpoint_group_update(id, body)
        print("The response of EndpointGroupsApi->endpoint_group_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_group_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EndpointGroup identifier | 
 **body** | [**EndpointgroupsEndpointGroupUpdatePayload**](EndpointgroupsEndpointGroupUpdatePayload.md)| EndpointGroup details | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | EndpointGroup not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_groups_id_get**
> PortainerEndpointGroup endpoint_groups_id_get(id)

Inspect an Environment(Endpoint) group

Retrieve details abont an environment(endpoint) group.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_endpoint_group import PortainerEndpointGroup
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    id = 56 # int | Environment(Endpoint) group identifier

    try:
        # Inspect an Environment(Endpoint) group
        api_response = api_instance.endpoint_groups_id_get(id)
        print("The response of EndpointGroupsApi->endpoint_groups_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_groups_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) group identifier | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | EndpointGroup not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_groups_post**
> PortainerEndpointGroup endpoint_groups_post(body)

Create an Environment(Endpoint) Group

Create a new environment(endpoint) group.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpointgroups_endpoint_group_create_payload import EndpointgroupsEndpointGroupCreatePayload
from openapi_client.models.portainer_endpoint_group import PortainerEndpointGroup
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointGroupsApi(api_client)
    body = openapi_client.EndpointgroupsEndpointGroupCreatePayload() # EndpointgroupsEndpointGroupCreatePayload | Environment(Endpoint) Group details

    try:
        # Create an Environment(Endpoint) Group
        api_response = api_instance.endpoint_groups_post(body)
        print("The response of EndpointGroupsApi->endpoint_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointGroupsApi->endpoint_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointgroupsEndpointGroupCreatePayload**](EndpointgroupsEndpointGroupCreatePayload.md)| Environment(Endpoint) Group details | 

### Return type

[**PortainerEndpointGroup**](PortainerEndpointGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

