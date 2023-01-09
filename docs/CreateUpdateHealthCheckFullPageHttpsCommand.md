# CreateUpdateHealthCheckFullPageHttpsCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_method_id** | **int** | Health check http method type (Dictionary 166) | [default to 1440]
**content_regular_expression** | **str** | The content has to match the expression (GET and POST methods only) | [optional] [default to '']
**content_negative_regular_expression** | **str** | The content cannot match the expression (GET and POST methods only) | [optional] [default to '']
**port** | **int** | Port | [default to 80]
**page_timeout** | **int** | Time limit for the main page body [ms] | [default to 7000]
**element_timeout** | **int** | Time limit for each page elements [ms] | [default to 5000]
**elements_total_timeout** | **int** | Time limit for all page elements [ms] | [default to 10000]
**fetch_page_elements** | **bool** | Fetch page elements | 
**max_redirects** | **int** | Maximum length of HTTP redirects sequence | [default to 5]
**max_parallel_requests** | **int** | Maximum number of HTTP requests run in parallel | [default to 6]
**generate_har** | **bool** | Generate a HAR file for each check | [default to True]
**allowed_element_error_count** | **int** | Number of elements that may not be fetched correctly | [optional] [default to 0]
**content_size_limit** | **int** | Content size limit (bytes) | [optional] [default to 2097152]
**ignore_html_parsing_time** | **bool** | Ignore HTML code processing time in results | [default to True]
**save_cookies** | **bool** | Save cookies between checks | [default to False]
**disable_content_encoding** | **bool** | Disable HTTP transfer compression | [default to False]
**content** | **str** | Content | [optional] [default to '']
**content_type** | **str** | Content type | [optional] [default to '']
**ignored_elements_filter** | **str** | Ignore errors for elements with URLs matching the expression (only if page elements are fetched) | [optional] [default to '']
**elements_filter** | **str** | Do not fetch elements with URLs that match the expression | [optional] [default to '']
**error_tolerance** | **int** | How many (%) locations have to report an error to consider it a breakdown | [default to 51]
**name** | **str** | Health check name | [default to '']
**address** | **str** | URL or IP address of the monitored service | [default to '']
**interval** | **int** | Time interval between health checks, in seconds | [default to 60]
**paused** | **bool** | Is paused | [default to False]
**locations_failover_enabled** | **bool** | Use random substitute locations in case of location breakdown | [default to True]
**notification_type_ids** | **list[int]** | Notification types enabled for a health check | [optional] 
**notification_event_type_ids** | **list[int]** | Event types with enabled notification | [optional] 
**notification_time_id** | **int** | Time when notification is sent | [default to 1594]
**description** | **str** | Description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


