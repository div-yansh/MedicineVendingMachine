from ibm_botocore.client import Config
import ibm_boto3


cos = ibm_boto3.client(service_name='s3',
    ibm_api_key_id="kvejlZivvjbl31RiJqthqlyKw815YRktG8krMtGLQ-WD",
    ibm_service_instance_id='378edde2-e61d-448d-a8c1-bd4fc9eba143',
    ibm_auth_endpoint="https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.jp-tok.cloud-object-storage.appdomain.cloud')


cos.upload_file(Filename='C:/Projects/MedicineVendingMachine/prescription template/prescription1.jpeg',Bucket='helloworld999',Key='img.jpeg')



'''
{
  "apikey": "kvejlZivvjbl31RiJqthqlyKw815YRktG8krMtGLQ-WD",
  "cos_hmac_keys": {
    "access_key_id": "d72bc69772404c7faa39bc2590dee285",
    "secret_access_key": "b2134a508c0912c0d652273adc12290c359841ac97f2405c"
  },
  "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "iam_apikey_description": "Auto-generated for key d72bc697-7240-4c7f-aa39-bc2590dee285",
  "iam_apikey_name": "helloworld9999",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/0d29d31f9f444ba7b2a0f59df644ea5f::serviceid:ServiceId-378edde2-e61d-448d-a8c1-bd4fc9eba143",
  "resource_instance_id": "crn:v1:bluemix:public:cloud-object-storage:global:a/0d29d31f9f444ba7b2a0f59df644ea5f:16adfc73-b074-4747-b396-f764f10cb542::"
}
'''