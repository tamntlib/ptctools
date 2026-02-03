# openapi_client.AuthApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](AuthApi.md#authenticate_user) | **POST** /auth | Authenticate
[**logout**](AuthApi.md#logout) | **POST** /auth/logout | Logout
[**validate_o_auth**](AuthApi.md#validate_o_auth) | **POST** /auth/oauth/validate | Authenticate with OAuth


# **authenticate_user**
> AuthAuthenticateResponse authenticate_user(body)

Authenticate

**Access policy**: public
Use this environment(endpoint) to authenticate against Portainer using a username and password.

### Example


```python
import openapi_client
from openapi_client.models.auth_authenticate_payload import AuthAuthenticatePayload
from openapi_client.models.auth_authenticate_response import AuthAuthenticateResponse
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
    api_instance = openapi_client.AuthApi(api_client)
    body = openapi_client.AuthAuthenticatePayload() # AuthAuthenticatePayload | Credentials used for authentication

    try:
        # Authenticate
        api_response = api_instance.authenticate_user(body)
        print("The response of AuthApi->authenticate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->authenticate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthAuthenticatePayload**](AuthAuthenticatePayload.md)| Credentials used for authentication | 

### Return type

[**AuthAuthenticateResponse**](AuthAuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**422** | Invalid Credentials |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

**Access policy**: public

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
    api_instance = openapi_client.AuthApi(api_client)

    try:
        # Logout
        api_instance.logout()
    except Exception as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_o_auth**
> AuthAuthenticateResponse validate_o_auth(body)

Authenticate with OAuth

**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.models.auth_authenticate_response import AuthAuthenticateResponse
from openapi_client.models.auth_oauth_payload import AuthOauthPayload
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
    api_instance = openapi_client.AuthApi(api_client)
    body = openapi_client.AuthOauthPayload() # AuthOauthPayload | OAuth Credentials used for authentication

    try:
        # Authenticate with OAuth
        api_response = api_instance.validate_o_auth(body)
        print("The response of AuthApi->validate_o_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->validate_o_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthOauthPayload**](AuthOauthPayload.md)| OAuth Credentials used for authentication | 

### Return type

[**AuthAuthenticateResponse**](AuthAuthenticateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**422** | Invalid Credentials |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

