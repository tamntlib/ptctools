# openapi_client.SettingsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_inspect**](SettingsApi.md#settings_inspect) | **GET** /settings | Retrieve Portainer settings
[**settings_public**](SettingsApi.md#settings_public) | **GET** /settings/public | Retrieve Portainer public settings
[**settings_update**](SettingsApi.md#settings_update) | **PUT** /settings | Update Portainer settings


# **settings_inspect**
> PortainerSettings settings_inspect()

Retrieve Portainer settings

Retrieve Portainer settings.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_settings import PortainerSettings
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
    api_instance = openapi_client.SettingsApi(api_client)

    try:
        # Retrieve Portainer settings
        api_response = api_instance.settings_inspect()
        print("The response of SettingsApi->settings_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_inspect: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PortainerSettings**](PortainerSettings.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_public**
> SettingsPublicSettingsResponse settings_public()

Retrieve Portainer public settings

Retrieve public settings. Returns a small set of settings that are not reserved to administrators only.
**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.models.settings_public_settings_response import SettingsPublicSettingsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SettingsApi(api_client)

    try:
        # Retrieve Portainer public settings
        api_response = api_instance.settings_public()
        print("The response of SettingsApi->settings_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_public: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SettingsPublicSettingsResponse**](SettingsPublicSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update**
> PortainerSettings settings_update(body)

Update Portainer settings

Update Portainer settings.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_settings import PortainerSettings
from openapi_client.models.settings_settings_update_payload import SettingsSettingsUpdatePayload
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
    api_instance = openapi_client.SettingsApi(api_client)
    body = openapi_client.SettingsSettingsUpdatePayload() # SettingsSettingsUpdatePayload | New settings

    try:
        # Update Portainer settings
        api_response = api_instance.settings_update(body)
        print("The response of SettingsApi->settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSettingsUpdatePayload**](SettingsSettingsUpdatePayload.md)| New settings | 

### Return type

[**PortainerSettings**](PortainerSettings.md)

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

