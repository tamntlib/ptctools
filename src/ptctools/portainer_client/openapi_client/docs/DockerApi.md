# openapi_client.DockerApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**docker_container_gpus_inspect**](DockerApi.md#docker_container_gpus_inspect) | **GET** /docker/{environmentId}/containers/{containerId}/gpus | Fetch container gpus data
[**docker_dashboard**](DockerApi.md#docker_dashboard) | **GET** /docker/{environmentId}/dashboard | Get counters for the dashboard
[**docker_images_list**](DockerApi.md#docker_images_list) | **GET** /docker/{environmentId}/images | Fetch images


# **docker_container_gpus_inspect**
> ContainersContainerGpusResponse docker_container_gpus_inspect(environment_id, container_id)

Fetch container gpus data

**Access policy**:

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.containers_container_gpus_response import ContainersContainerGpusResponse
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DockerApi(api_client)
    environment_id = 56 # int | Environment identifier
    container_id = 56 # int | Container identifier

    try:
        # Fetch container gpus data
        api_response = api_instance.docker_container_gpus_inspect(environment_id, container_id)
        print("The response of DockerApi->docker_container_gpus_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerApi->docker_container_gpus_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **int**| Environment identifier | 
 **container_id** | **int**| Container identifier | 

### Return type

[**ContainersContainerGpusResponse**](ContainersContainerGpusResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**404** | Environment or container not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_dashboard**
> DockerDashboardResponse docker_dashboard(environment_id)

Get counters for the dashboard

**Access policy**: restricted

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.docker_dashboard_response import DockerDashboardResponse
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DockerApi(api_client)
    environment_id = 56 # int | Environment identifier

    try:
        # Get counters for the dashboard
        api_response = api_instance.docker_dashboard(environment_id)
        print("The response of DockerApi->docker_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerApi->docker_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **int**| Environment identifier | 

### Return type

[**DockerDashboardResponse**](DockerDashboardResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_images_list**
> List[ImagesImageResponse] docker_images_list(environment_id, with_usage=with_usage)

Fetch images

**Access policy**:

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.images_image_response import ImagesImageResponse
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DockerApi(api_client)
    environment_id = 56 # int | Environment identifier
    with_usage = True # bool | Include image usage information (optional)

    try:
        # Fetch images
        api_response = api_instance.docker_images_list(environment_id, with_usage=with_usage)
        print("The response of DockerApi->docker_images_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerApi->docker_images_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **int**| Environment identifier | 
 **with_usage** | **bool**| Include image usage information | [optional] 

### Return type

[**List[ImagesImageResponse]**](ImagesImageResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

