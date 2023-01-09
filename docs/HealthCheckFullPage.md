# HealthCheckFullPage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_method** | [**DictionaryItem**](DictionaryItem.md) | Health check http method type | [optional] 
**content_regular_expression** | **str** | The content has to match the expression (GET and POST methods only) | [optional] 
**content_negative_regular_expression** | **str** | The content cannot match the expression (GET and POST methods only) | [optional] 
**port** | **int** | Port | [optional] 
**page_timeout** | **int** | Time limit for the main page body [ms] | [optional] 
**element_timeout** | **int** | Time limit for each page elements [ms] | [optional] 
**elements_total_timeout** | **int** | Time limit for all page elements [ms] | [optional] 
**fetch_page_elements** | **bool** | Fetch page elements | [optional] 
**max_redirects** | **int** | Maximum length of HTTP redirects sequence | [optional] 
**max_parallel_requests** | **int** | Maximum number of HTTP requests run in parallel | [optional] 
**generate_har** | **bool** | Generate a HAR file for each check | [optional] 
**allowed_element_error_count** | **int** | Number of elements that may not be fetched correctly | [optional] 
**content_size_limit** | **int** | Content size limit (bytes) | [optional] 
**ignore_html_parsing_time** | **bool** | Ignore HTML code processing time in results | [optional] 
**save_cookies** | **bool** | Save cookies between checks | [optional] 
**disable_content_encoding** | **bool** | Disable HTTP transfer compression | [optional] 
**content** | **str** | Content | [optional] 
**content_type** | **str** | Content type | [optional] 
**ignored_elements_filter** | **str** | Ignore errors for elements with URLs matching the expression (only if page elements are fetched) | [optional] 
**elements_filter** | **str** | Do not fetch elements with URLs that match the expression | [optional] 
**notification_types** | [**list[DictionaryItem]**](DictionaryItem.md) | Notification types enabled for a health check | [optional] 
**notification_event_types** | [**list[DictionaryItem]**](DictionaryItem.md) | Event types with enabled notification | [optional] 
**notification_time** | [**DictionaryItem**](DictionaryItem.md) | Time when notification is sent | [optional] 
**locations_failover_enabled** | **bool** | Use random substitute locations in case of location breakdown | [optional] 
**error_tolerance** | **int** | How many (%) locations have to report an error to consider it a breakdown | [optional] 
**id** | **int** | Id | [optional] 
**interval** | **int** | Interval | [optional] 
**name** | **str** | Name | [optional] 
**address** | **str** | Address | [optional] 
**service_type** | [**DictionaryItem**](DictionaryItem.md) | Type | [optional] 
**state** | [**DictionaryItem**](DictionaryItem.md) | State | [optional] 
**details_location** | **str** | Details url | [optional] 
**paused** | **bool** | Is paused | [optional] 
**suspended** | **bool** | Is suspended | [optional] 
**last_invalid_check** | **datetime** | Last invalid check | [optional] 
**last_valid_check** | **datetime** | Last valid check | [optional] 
**description** | **str** | Description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


