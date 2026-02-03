# openapi_client.LdapApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**l_dap_check**](LdapApi.md#l_dap_check) | **POST** /ldap/check | Test LDAP connectivity


# **l_dap_check**
> l_dap_check(body)

Test LDAP connectivity

Test LDAP connectivity using LDAP details
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.ldap_check_payload import LdapCheckPayload
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
    api_instance = openapi_client.LdapApi(api_client)
    body = openapi_client.LdapCheckPayload() # LdapCheckPayload | details

    try:
        # Test LDAP connectivity
        api_instance.l_dap_check(body)
    except Exception as e:
        print("Exception when calling LdapApi->l_dap_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapCheckPayload**](LdapCheckPayload.md)| details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

