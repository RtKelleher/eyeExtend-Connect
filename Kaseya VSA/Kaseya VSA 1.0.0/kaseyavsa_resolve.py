"""
Copyright © 2020 Forescout Technologies, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging

credentials = {}
vsa_server_details = {}
response = {}

credentials["username"] = params["connect_kaseyavsa_username"]
credentials["password"] = params["connect_kaseyavsa_password"]

vsa_server_details["address"] = params["connect_kaseyavsa_server_ipaddress"]
vsa_server_details["port"] = params["connect_kaseyavsa_server_port"]

code, client, session_token = KASEYAVSA_API_LIB.KASEYAVSA_HTTP_CLIENT(credentials, vsa_server_details, ssl_context)

kaseyavsa_property_map = {
    "AgentId": "connect_kaseyavsa_agentid",
    "AssetId": "connect_kaseyavsa_assetid",
    "OSName": "connect_kaseyavsa_osname",
    "MachineGroup": "connect_kaseyavsa_machine_group",
    "LastSeenDate": "connect_kaseyavsa_last_seen_date"
}


logging.debug("RESOLVE: Login to VSA Server [{}] returned code [{}]".format(vsa_server_details["address"], code))

if code == 200:
    properties = []
    if "mac" in params:
        mac = ':'.join(params["mac"][i:i + 2] for i in range(0, 12, 2))
        logging.debug("Attempting API Query for MAC [{}]".format(mac))
        query_code, query_results = KASEYAVSA_API_LIB.KASEYAVSA_QUERY_ASSETS(client, vsa_server_details, session_token, mac)
        if not query_results["TotalRecords"] == 0:
            host_details = query_results["Result"][0]

            logging.debug("API Query returned code [{}] and response [{}]".format(query_code, query_results))

            properties = {}
            for key, value in host_details.items():
                if key in kaseyavsa_property_map:
                    if key != "LastSeenDate":
                        if value != "":
                            properties[kaseyavsa_property_map[key]] = str(value)
                        else:
                            properties[kaseyavsa_property_map[key]] = "None"
                    else:
                        _date_time_obj = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        properties[kaseyavsa_property_map[key]] = int(datetime.datetime.timestamp(_date_time_obj))

            response["properties"] = properties
        else:
            response["error"] = "Could not find this endpoint in the Kaseya VSA Server."
    else:
        response["error"] = "No MAC address to query the endpoint."
else:
    response["error"] = "API Connection Failed, check configuration."

logging.debug("Returning response object to infrastructure. response=[{}]".format(response))