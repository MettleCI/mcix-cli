# Login to IBM Cloud then select {profile} ➜ 'Log in to CLI and API' and copy the IBM Cloud CLI connmection string

$> ibmcloud login -a https://cloud.ibm.com -u passcode -p RqMQnXEY5J
API endpoint: https://cloud.ibm.com
Authenticating...
OK

Targeted account Data Migrators (a10baca9e4e04198ab97bb29d4496180) <-> 392500

Select a region (or press enter to skip):
1. au-syd
2. in-che
3. jp-osa
4. jp-tok
5. eu-de
6. eu-es
7. eu-gb
8. ca-tor
9. us-south
10. us-east
11. br-sao
Enter a number> 1
Targeted region au-syd

API endpoint:     https://cloud.ibm.com
Region:           au-syd
User:             john.mckeever@datamigrators.com
Account:          Data Migrators (a10baca9e4e04198ab97bb29d4496180) <-> 392500
Resource group:   No resource group targeted, use 'ibmcloud target -g RESOURCE_GROUP'

$> ibmcloud iam api-key-create cliapikey -d "My CLI API key" --file ibm_cloud_key_file
Creating API key cliapikey under a10baca9e4e04198ab97bb29d4496180 as john.mckeever@datamigrators.com...
OK
API key cliapikey was created
Successfully save API key information to ibm_cloud_key_file

$> cat ibm_cloud_key_file
{
        "name": "cliapikey",
        "description": "My CLI API key",
        "apikey": "BThtN-4po2E81OpJb376jew95rKEhnASZOIz7E-KeGei",         <--- The value you need (without quotes) 
        "createdAt": "2024-11-13T02:48+0000",
        "locked": false,
        "uuid": ""
}%