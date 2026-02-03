# openapi_client.IntelApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_action**](IntelApi.md#device_action) | **POST** /open_amt/{id}/devices/{deviceId}/action | Execute out of band action on an AMT managed device
[**device_features**](IntelApi.md#device_features) | **POST** /open_amt/{id}/devices_features/{deviceId} | Enable features on an AMT managed device
[**open_amt_activate**](IntelApi.md#open_amt_activate) | **POST** /open_amt/{id}/activate | Activate OpenAMT device and associate to agent endpoint
[**open_amt_configure**](IntelApi.md#open_amt_configure) | **POST** /open_amt | Enable Portainer&#39;s OpenAMT capabilities
[**open_amt_devices**](IntelApi.md#open_amt_devices) | **GET** /open_amt/{id}/devices | Fetch OpenAMT managed devices information for endpoint
[**open_amt_host_info**](IntelApi.md#open_amt_host_info) | **GET** /open_amt/{id}/info | Request OpenAMT info from a node


# **device_action**
> device_action(id, device_id, body)

Execute out of band action on an AMT managed device

Execute out of band action on an AMT managed device
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.openamt_device_action_payload import OpenamtDeviceActionPayload
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
    api_instance = openapi_client.IntelApi(api_client)
    id = 56 # int | Environment identifier
    device_id = 56 # int | Device identifier
    body = openapi_client.OpenamtDeviceActionPayload() # OpenamtDeviceActionPayload | Device Action

    try:
        # Execute out of band action on an AMT managed device
        api_instance.device_action(id, device_id, body)
    except Exception as e:
        print("Exception when calling IntelApi->device_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **device_id** | **int**| Device identifier | 
 **body** | [**OpenamtDeviceActionPayload**](OpenamtDeviceActionPayload.md)| Device Action | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_features**
> device_features(id, device_id, body)

Enable features on an AMT managed device

Enable features on an AMT managed device
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.openamt_device_features_payload import OpenamtDeviceFeaturesPayload
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
    api_instance = openapi_client.IntelApi(api_client)
    id = 56 # int | Environment identifier
    device_id = 56 # int | Device identifier
    body = openapi_client.OpenamtDeviceFeaturesPayload() # OpenamtDeviceFeaturesPayload | Device Features

    try:
        # Enable features on an AMT managed device
        api_instance.device_features(id, device_id, body)
    except Exception as e:
        print("Exception when calling IntelApi->device_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **device_id** | **int**| Device identifier | 
 **body** | [**OpenamtDeviceFeaturesPayload**](OpenamtDeviceFeaturesPayload.md)| Device Features | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_amt_activate**
> open_amt_activate(id)

Activate OpenAMT device and associate to agent endpoint

Activate OpenAMT device and associate to agent endpoint
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IntelApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Activate OpenAMT device and associate to agent endpoint
        api_instance.open_amt_activate(id)
    except Exception as e:
        print("Exception when calling IntelApi->open_amt_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_amt_configure**
> open_amt_configure(body)

Enable Portainer's OpenAMT capabilities

Enable Portainer's OpenAMT capabilities
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.openamt_open_amt_configure_payload import OpenamtOpenAMTConfigurePayload
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
    api_instance = openapi_client.IntelApi(api_client)
    body = openapi_client.OpenamtOpenAMTConfigurePayload() # OpenamtOpenAMTConfigurePayload | OpenAMT Settings

    try:
        # Enable Portainer's OpenAMT capabilities
        api_instance.open_amt_configure(body)
    except Exception as e:
        print("Exception when calling IntelApi->open_amt_configure: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenamtOpenAMTConfigurePayload**](OpenamtOpenAMTConfigurePayload.md)| OpenAMT Settings | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_amt_devices**
> open_amt_devices(id)

Fetch OpenAMT managed devices information for endpoint

Fetch OpenAMT managed devices information for endpoint
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IntelApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Fetch OpenAMT managed devices information for endpoint
        api_instance.open_amt_devices(id)
    except Exception as e:
        print("Exception when calling IntelApi->open_amt_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_amt_host_info**
> open_amt_host_info(id)

Request OpenAMT info from a node

Request OpenAMT info from a node
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IntelApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Request OpenAMT info from a node
        api_instance.open_amt_host_info(id)
    except Exception as e:
        print("Exception when calling IntelApi->open_amt_host_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access settings |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

