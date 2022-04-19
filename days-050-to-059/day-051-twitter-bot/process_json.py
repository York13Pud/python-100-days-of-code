class ProcessJson():
    def __init__(self, json_to_process):
        """This class will process the contents of the JSON file into a single object to reduce the number of variables needed."""
        
        # --- Time the test was run:
        self.datetime = json_to_process["timestamp"].split("T")
        self.date = self.datetime[0]
        self.time = self.datetime[1].replace("Z", "")
        
        # --- Details about the results:
        self.home_isp = json_to_process["isp"]
        self.home_public_ip = json_to_process["interface"]["externalIp"]
        self.home_on_vpn = json_to_process["interface"]["isVpn"]
        self.home_ping_jitter = float(json_to_process["ping"]["jitter"])
        self.home_ping_latency = float(json_to_process["ping"]["latency"])
        self.home_upload_speed_bits = float(json_to_process["upload"]["bandwidth"])
        self.home_upload_time = float(json_to_process["upload"]["elapsed"])
        self.home_download_speed_bits = float(json_to_process["download"]["bandwidth"])
        self.home_download_time = float(json_to_process["download"]["elapsed"])
        
        # --- Details of the server that was tested against:
        self.test_server_id = json_to_process["server"]["id"]
        self.test_server_host = json_to_process["server"]["host"]
        self.test_server_port = json_to_process["server"]["port"]
        self.test_server_name = json_to_process["server"]["name"]
        self.test_server_location = json_to_process["server"]["location"]
        self.test_server_country = json_to_process["server"]["country"]
        self.test_server_ip = json_to_process["server"]["ip"]
        
        # --- Results references:
        self.result_id = json_to_process["result"]["id"]
        self.result_url = json_to_process["result"]["url"]
        self.result_persisted = json_to_process["result"]["persisted"]