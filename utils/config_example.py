webhook = "url_webhook.com"
auth_token = "token_zabbix"

url = "url_zabbix.com"
headers = {
    'Content-Type': 'application/json-rpc'
}
params = {
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "output": "extend",
        "history": 3,
        "itemids": "",
        "sortfield": "clock",
        "sortorder": "DESC",
        "limit": 1500
    },
    "auth": auth_token,  
    "id": 1
}