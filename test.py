# import requests

# # def admin_create_role(token):
# #     url = "https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/roles"
# #     headers = {
# #         "cache-control": "no-cache",
# #         "content-type": "application/json",
# #         "Authorization": f"Bearer {token}"
# #     }
# #     data = {
# #         "name": "kjdfsdjlf",
# #         "description": "Supersuesdfkldshfjr access"
# #     }

# #     response = requests.post(url, headers=headers, json=data)

# #     print(response.status_code)
# #     print(response.json())

# # admin_create_role("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InF3VWp0ZVhISU1xeTRCNnNLSDRqSSJ9.eyJpc3MiOiJodHRwczovL2Rldi12Z3dvbDRycmtieXJpNXNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMaVJXdG0zM0hlY2VxdzdLODMzcWRVQzJxT1FKVGJKV0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtdmd3b2w0cnJrYnlyaTVzbS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTczODA2NTkzOSwiZXhwIjoxNzM4MTUyMzM5LCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIHJlYWQ6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX2N1c3RvbV9ibG9ja3MgZGVsZXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBjcmVhdGU6dXNlcl90aWNrZXRzIHJlYWQ6Y2xpZW50cyB1cGRhdGU6Y2xpZW50cyBkZWxldGU6Y2xpZW50cyBjcmVhdGU6Y2xpZW50cyByZWFkOmNsaWVudF9rZXlzIHVwZGF0ZTpjbGllbnRfa2V5cyBkZWxldGU6Y2xpZW50X2tleXMgY3JlYXRlOmNsaWVudF9rZXlzIHJlYWQ6Y29ubmVjdGlvbnMgdXBkYXRlOmNvbm5lY3Rpb25zIGRlbGV0ZTpjb25uZWN0aW9ucyBjcmVhdGU6Y29ubmVjdGlvbnMgcmVhZDpyZXNvdXJjZV9zZXJ2ZXJzIHVwZGF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGRlbGV0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGNyZWF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIHJlYWQ6ZGV2aWNlX2NyZWRlbnRpYWxzIHVwZGF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgZGVsZXRlOmRldmljZV9jcmVkZW50aWFscyBjcmVhdGU6ZGV2aWNlX2NyZWRlbnRpYWxzIHJlYWQ6cnVsZXMgdXBkYXRlOnJ1bGVzIGRlbGV0ZTpydWxlcyBjcmVhdGU6cnVsZXMgcmVhZDpydWxlc19jb25maWdzIHVwZGF0ZTpydWxlc19jb25maWdzIGRlbGV0ZTpydWxlc19jb25maWdzIHJlYWQ6aG9va3MgdXBkYXRlOmhvb2tzIGRlbGV0ZTpob29rcyBjcmVhdGU6aG9va3MgcmVhZDphY3Rpb25zIHVwZGF0ZTphY3Rpb25zIGRlbGV0ZTphY3Rpb25zIGNyZWF0ZTphY3Rpb25zIHJlYWQ6ZW1haWxfcHJvdmlkZXIgdXBkYXRlOmVtYWlsX3Byb3ZpZGVyIGRlbGV0ZTplbWFpbF9wcm92aWRlciBjcmVhdGU6ZW1haWxfcHJvdmlkZXIgYmxhY2tsaXN0OnRva2VucyByZWFkOnN0YXRzIHJlYWQ6aW5zaWdodHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpsb2dzX3VzZXJzIHJlYWQ6c2hpZWxkcyBjcmVhdGU6c2hpZWxkcyB1cGRhdGU6c2hpZWxkcyBkZWxldGU6c2hpZWxkcyByZWFkOmFub21hbHlfYmxvY2tzIGRlbGV0ZTphbm9tYWx5X2Jsb2NrcyB1cGRhdGU6dHJpZ2dlcnMgcmVhZDp0cmlnZ2VycyByZWFkOmdyYW50cyBkZWxldGU6Z3JhbnRzIHJlYWQ6Z3VhcmRpYW5fZmFjdG9ycyB1cGRhdGU6Z3VhcmRpYW5fZmFjdG9ycyByZWFkOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGRlbGV0ZTpndWFyZGlhbl9lbnJvbGxtZW50cyBjcmVhdGU6Z3VhcmRpYW5fZW5yb2xsbWVudF90aWNrZXRzIHJlYWQ6dXNlcl9pZHBfdG9rZW5zIGNyZWF0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIGRlbGV0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIHJlYWQ6Y3VzdG9tX2RvbWFpbnMgZGVsZXRlOmN1c3RvbV9kb21haW5zIGNyZWF0ZTpjdXN0b21fZG9tYWlucyB1cGRhdGU6Y3VzdG9tX2RvbWFpbnMgcmVhZDplbWFpbF90ZW1wbGF0ZXMgY3JlYXRlOmVtYWlsX3RlbXBsYXRlcyB1cGRhdGU6ZW1haWxfdGVtcGxhdGVzIHJlYWQ6bWZhX3BvbGljaWVzIHVwZGF0ZTptZmFfcG9saWNpZXMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgZGVsZXRlOnJvbGVzIHVwZGF0ZTpyb2xlcyByZWFkOnByb21wdHMgdXBkYXRlOnByb21wdHMgcmVhZDpicmFuZGluZyB1cGRhdGU6YnJhbmRpbmcgZGVsZXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIHJlYWQ6bGltaXRzIHVwZGF0ZTpsaW1pdHMgY3JlYXRlOnJvbGVfbWVtYmVycyByZWFkOnJvbGVfbWVtYmVycyBkZWxldGU6cm9sZV9tZW1iZXJzIHJlYWQ6ZW50aXRsZW1lbnRzIHJlYWQ6YXR0YWNrX3Byb3RlY3Rpb24gdXBkYXRlOmF0dGFja19wcm90ZWN0aW9uIHJlYWQ6b3JnYW5pemF0aW9uc19zdW1tYXJ5IGNyZWF0ZTphdXRoZW50aWNhdGlvbl9tZXRob2RzIHJlYWQ6YXV0aGVudGljYXRpb25fbWV0aG9kcyB1cGRhdGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyBkZWxldGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyByZWFkOm9yZ2FuaXphdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbnMgZGVsZXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcnMgZGVsZXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIGNyZWF0ZTpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgcmVhZDpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbl9jb25uZWN0aW9ucyBkZWxldGU6b3JnYW5pemF0aW9uX2Nvbm5lY3Rpb25zIGNyZWF0ZTpvcmdhbml6YXRpb25fbWVtYmVyX3JvbGVzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBkZWxldGU6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBjcmVhdGU6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIHJlYWQ6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIGRlbGV0ZTpvcmdhbml6YXRpb25faW52aXRhdGlvbnMgcmVhZDpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV9jb25maWcgdXBkYXRlOnNjaW1fY29uZmlnIGRlbGV0ZTpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV90b2tlbiByZWFkOnNjaW1fdG9rZW4gZGVsZXRlOnNjaW1fdG9rZW4gZGVsZXRlOnBob25lX3Byb3ZpZGVycyBjcmVhdGU6cGhvbmVfcHJvdmlkZXJzIHJlYWQ6cGhvbmVfcHJvdmlkZXJzIHVwZGF0ZTpwaG9uZV9wcm92aWRlcnMgZGVsZXRlOnBob25lX3RlbXBsYXRlcyBjcmVhdGU6cGhvbmVfdGVtcGxhdGVzIHJlYWQ6cGhvbmVfdGVtcGxhdGVzIHVwZGF0ZTpwaG9uZV90ZW1wbGF0ZXMgY3JlYXRlOmVuY3J5cHRpb25fa2V5cyByZWFkOmVuY3J5cHRpb25fa2V5cyB1cGRhdGU6ZW5jcnlwdGlvbl9rZXlzIGRlbGV0ZTplbmNyeXB0aW9uX2tleXMgcmVhZDpzZXNzaW9ucyBkZWxldGU6c2Vzc2lvbnMgcmVhZDpyZWZyZXNoX3Rva2VucyBkZWxldGU6cmVmcmVzaF90b2tlbnMgY3JlYXRlOnNlbGZfc2VydmljZV9wcm9maWxlcyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlcyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVzIGRlbGV0ZTpzZWxmX3NlcnZpY2VfcHJvZmlsZXMgY3JlYXRlOnNzb19hY2Nlc3NfdGlja2V0cyBkZWxldGU6c3NvX2FjY2Vzc190aWNrZXRzIHJlYWQ6Zm9ybXMgdXBkYXRlOmZvcm1zIGRlbGV0ZTpmb3JtcyBjcmVhdGU6Zm9ybXMgcmVhZDpmbG93cyB1cGRhdGU6Zmxvd3MgZGVsZXRlOmZsb3dzIGNyZWF0ZTpmbG93cyByZWFkOmZsb3dzX3ZhdWx0IHJlYWQ6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgdXBkYXRlOmZsb3dzX3ZhdWx0X2Nvbm5lY3Rpb25zIGRlbGV0ZTpmbG93c192YXVsdF9jb25uZWN0aW9ucyBjcmVhdGU6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgcmVhZDpmbG93c19leGVjdXRpb25zIGRlbGV0ZTpmbG93c19leGVjdXRpb25zIHJlYWQ6Y29ubmVjdGlvbnNfb3B0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnNfb3B0aW9ucyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlX2N1c3RvbV90ZXh0cyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVfY3VzdG9tX3RleHRzIHJlYWQ6Y2xpZW50X2NyZWRlbnRpYWxzIGNyZWF0ZTpjbGllbnRfY3JlZGVudGlhbHMgdXBkYXRlOmNsaWVudF9jcmVkZW50aWFscyBkZWxldGU6Y2xpZW50X2NyZWRlbnRpYWxzIHJlYWQ6b3JnYW5pemF0aW9uX2NsaWVudF9ncmFudHMgY3JlYXRlOm9yZ2FuaXphdGlvbl9jbGllbnRfZ3JhbnRzIGRlbGV0ZTpvcmdhbml6YXRpb25fY2xpZW50X2dyYW50cyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkxpUld0bTMzSGVjZXF3N0s4MzNxZFVDMnFPUUpUYkpXIn0.KCBn7IpMBDHMpBbYEkh1AzSyq0u1PzKu1uw8BNg1I0cqcGvu0agxI87JApaqp-OLv89AO6RW0sPp3oTRYd7fEOrwlxMqwMxb32EDt3i8WD-mu0s69yndR_YDoAgF8C56iJyUOwBcmLT9J3GFTI6_tr9cn1Qdryz9fSna6kMVe3dksI20ST3beCllXuP1sezfx7LAXAXM9Kv_fN7DxfeK_Qj2E4GGCEJwd5RtjjF9mGL7qG2q4nWlU3aDvddrP2HJAg-_7XORnU00F1-81P2wN_dq7dgPE-CFQ0tsYGNWvvS5LFJCeODhwV_Uxa4jJK0m4M2be3372eV9eA_hBsbxWw")
# # # name = 'mauank'
# # # descrip = 'nfkjef'
# # # data = str({"name": f"{name}","description": f"{descrip}"})
# # # print(data)
# # # print(type(data))
# token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InF3VWp0ZVhISU1xeTRCNnNLSDRqSSJ9.eyJpc3MiOiJodHRwczovL2Rldi12Z3dvbDRycmtieXJpNXNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMaVJXdG0zM0hlY2VxdzdLODMzcWRVQzJxT1FKVGJKV0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtdmd3b2w0cnJrYnlyaTVzbS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTczODA2NTkzOSwiZXhwIjoxNzM4MTUyMzM5LCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIHJlYWQ6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX2N1c3RvbV9ibG9ja3MgZGVsZXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBjcmVhdGU6dXNlcl90aWNrZXRzIHJlYWQ6Y2xpZW50cyB1cGRhdGU6Y2xpZW50cyBkZWxldGU6Y2xpZW50cyBjcmVhdGU6Y2xpZW50cyByZWFkOmNsaWVudF9rZXlzIHVwZGF0ZTpjbGllbnRfa2V5cyBkZWxldGU6Y2xpZW50X2tleXMgY3JlYXRlOmNsaWVudF9rZXlzIHJlYWQ6Y29ubmVjdGlvbnMgdXBkYXRlOmNvbm5lY3Rpb25zIGRlbGV0ZTpjb25uZWN0aW9ucyBjcmVhdGU6Y29ubmVjdGlvbnMgcmVhZDpyZXNvdXJjZV9zZXJ2ZXJzIHVwZGF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGRlbGV0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGNyZWF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIHJlYWQ6ZGV2aWNlX2NyZWRlbnRpYWxzIHVwZGF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgZGVsZXRlOmRldmljZV9jcmVkZW50aWFscyBjcmVhdGU6ZGV2aWNlX2NyZWRlbnRpYWxzIHJlYWQ6cnVsZXMgdXBkYXRlOnJ1bGVzIGRlbGV0ZTpydWxlcyBjcmVhdGU6cnVsZXMgcmVhZDpydWxlc19jb25maWdzIHVwZGF0ZTpydWxlc19jb25maWdzIGRlbGV0ZTpydWxlc19jb25maWdzIHJlYWQ6aG9va3MgdXBkYXRlOmhvb2tzIGRlbGV0ZTpob29rcyBjcmVhdGU6aG9va3MgcmVhZDphY3Rpb25zIHVwZGF0ZTphY3Rpb25zIGRlbGV0ZTphY3Rpb25zIGNyZWF0ZTphY3Rpb25zIHJlYWQ6ZW1haWxfcHJvdmlkZXIgdXBkYXRlOmVtYWlsX3Byb3ZpZGVyIGRlbGV0ZTplbWFpbF9wcm92aWRlciBjcmVhdGU6ZW1haWxfcHJvdmlkZXIgYmxhY2tsaXN0OnRva2VucyByZWFkOnN0YXRzIHJlYWQ6aW5zaWdodHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpsb2dzX3VzZXJzIHJlYWQ6c2hpZWxkcyBjcmVhdGU6c2hpZWxkcyB1cGRhdGU6c2hpZWxkcyBkZWxldGU6c2hpZWxkcyByZWFkOmFub21hbHlfYmxvY2tzIGRlbGV0ZTphbm9tYWx5X2Jsb2NrcyB1cGRhdGU6dHJpZ2dlcnMgcmVhZDp0cmlnZ2VycyByZWFkOmdyYW50cyBkZWxldGU6Z3JhbnRzIHJlYWQ6Z3VhcmRpYW5fZmFjdG9ycyB1cGRhdGU6Z3VhcmRpYW5fZmFjdG9ycyByZWFkOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGRlbGV0ZTpndWFyZGlhbl9lbnJvbGxtZW50cyBjcmVhdGU6Z3VhcmRpYW5fZW5yb2xsbWVudF90aWNrZXRzIHJlYWQ6dXNlcl9pZHBfdG9rZW5zIGNyZWF0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIGRlbGV0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIHJlYWQ6Y3VzdG9tX2RvbWFpbnMgZGVsZXRlOmN1c3RvbV9kb21haW5zIGNyZWF0ZTpjdXN0b21fZG9tYWlucyB1cGRhdGU6Y3VzdG9tX2RvbWFpbnMgcmVhZDplbWFpbF90ZW1wbGF0ZXMgY3JlYXRlOmVtYWlsX3RlbXBsYXRlcyB1cGRhdGU6ZW1haWxfdGVtcGxhdGVzIHJlYWQ6bWZhX3BvbGljaWVzIHVwZGF0ZTptZmFfcG9saWNpZXMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgZGVsZXRlOnJvbGVzIHVwZGF0ZTpyb2xlcyByZWFkOnByb21wdHMgdXBkYXRlOnByb21wdHMgcmVhZDpicmFuZGluZyB1cGRhdGU6YnJhbmRpbmcgZGVsZXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIHJlYWQ6bGltaXRzIHVwZGF0ZTpsaW1pdHMgY3JlYXRlOnJvbGVfbWVtYmVycyByZWFkOnJvbGVfbWVtYmVycyBkZWxldGU6cm9sZV9tZW1iZXJzIHJlYWQ6ZW50aXRsZW1lbnRzIHJlYWQ6YXR0YWNrX3Byb3RlY3Rpb24gdXBkYXRlOmF0dGFja19wcm90ZWN0aW9uIHJlYWQ6b3JnYW5pemF0aW9uc19zdW1tYXJ5IGNyZWF0ZTphdXRoZW50aWNhdGlvbl9tZXRob2RzIHJlYWQ6YXV0aGVudGljYXRpb25fbWV0aG9kcyB1cGRhdGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyBkZWxldGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyByZWFkOm9yZ2FuaXphdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbnMgZGVsZXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcnMgZGVsZXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIGNyZWF0ZTpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgcmVhZDpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbl9jb25uZWN0aW9ucyBkZWxldGU6b3JnYW5pemF0aW9uX2Nvbm5lY3Rpb25zIGNyZWF0ZTpvcmdhbml6YXRpb25fbWVtYmVyX3JvbGVzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBkZWxldGU6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBjcmVhdGU6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIHJlYWQ6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIGRlbGV0ZTpvcmdhbml6YXRpb25faW52aXRhdGlvbnMgcmVhZDpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV9jb25maWcgdXBkYXRlOnNjaW1fY29uZmlnIGRlbGV0ZTpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV90b2tlbiByZWFkOnNjaW1fdG9rZW4gZGVsZXRlOnNjaW1fdG9rZW4gZGVsZXRlOnBob25lX3Byb3ZpZGVycyBjcmVhdGU6cGhvbmVfcHJvdmlkZXJzIHJlYWQ6cGhvbmVfcHJvdmlkZXJzIHVwZGF0ZTpwaG9uZV9wcm92aWRlcnMgZGVsZXRlOnBob25lX3RlbXBsYXRlcyBjcmVhdGU6cGhvbmVfdGVtcGxhdGVzIHJlYWQ6cGhvbmVfdGVtcGxhdGVzIHVwZGF0ZTpwaG9uZV90ZW1wbGF0ZXMgY3JlYXRlOmVuY3J5cHRpb25fa2V5cyByZWFkOmVuY3J5cHRpb25fa2V5cyB1cGRhdGU6ZW5jcnlwdGlvbl9rZXlzIGRlbGV0ZTplbmNyeXB0aW9uX2tleXMgcmVhZDpzZXNzaW9ucyBkZWxldGU6c2Vzc2lvbnMgcmVhZDpyZWZyZXNoX3Rva2VucyBkZWxldGU6cmVmcmVzaF90b2tlbnMgY3JlYXRlOnNlbGZfc2VydmljZV9wcm9maWxlcyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlcyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVzIGRlbGV0ZTpzZWxmX3NlcnZpY2VfcHJvZmlsZXMgY3JlYXRlOnNzb19hY2Nlc3NfdGlja2V0cyBkZWxldGU6c3NvX2FjY2Vzc190aWNrZXRzIHJlYWQ6Zm9ybXMgdXBkYXRlOmZvcm1zIGRlbGV0ZTpmb3JtcyBjcmVhdGU6Zm9ybXMgcmVhZDpmbG93cyB1cGRhdGU6Zmxvd3MgZGVsZXRlOmZsb3dzIGNyZWF0ZTpmbG93cyByZWFkOmZsb3dzX3ZhdWx0IHJlYWQ6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgdXBkYXRlOmZsb3dzX3ZhdWx0X2Nvbm5lY3Rpb25zIGRlbGV0ZTpmbG93c192YXVsdF9jb25uZWN0aW9ucyBjcmVhdGU6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgcmVhZDpmbG93c19leGVjdXRpb25zIGRlbGV0ZTpmbG93c19leGVjdXRpb25zIHJlYWQ6Y29ubmVjdGlvbnNfb3B0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnNfb3B0aW9ucyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlX2N1c3RvbV90ZXh0cyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVfY3VzdG9tX3RleHRzIHJlYWQ6Y2xpZW50X2NyZWRlbnRpYWxzIGNyZWF0ZTpjbGllbnRfY3JlZGVudGlhbHMgdXBkYXRlOmNsaWVudF9jcmVkZW50aWFscyBkZWxldGU6Y2xpZW50X2NyZWRlbnRpYWxzIHJlYWQ6b3JnYW5pemF0aW9uX2NsaWVudF9ncmFudHMgY3JlYXRlOm9yZ2FuaXphdGlvbl9jbGllbnRfZ3JhbnRzIGRlbGV0ZTpvcmdhbml6YXRpb25fY2xpZW50X2dyYW50cyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkxpUld0bTMzSGVjZXF3N0s4MzNxZFVDMnFPUUpUYkpXIn0.KCBn7IpMBDHMpBbYEkh1AzSyq0u1PzKu1uw8BNg1I0cqcGvu0agxI87JApaqp-OLv89AO6RW0sPp3oTRYd7fEOrwlxMqwMxb32EDt3i8WD-mu0s69yndR_YDoAgF8C56iJyUOwBcmLT9J3GFTI6_tr9cn1Qdryz9fSna6kMVe3dksI20ST3beCllXuP1sezfx7LAXAXM9Kv_fN7DxfeK_Qj2E4GGCEJwd5RtjjF9mGL7qG2q4nWlU3aDvddrP2HJAg-_7XORnU00F1-81P2wN_dq7dgPE-CFQ0tsYGNWvvS5LFJCeODhwV_Uxa4jJK0m4M2be3372eV9eA_hBsbxWw'

# from fastapi import Depends, HTTPException, status
# from fastapi import FastAPI,Security
# # from .config import get_settings
# import jwt 
# # from .server import server
# from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer # 👈 new imports
# from typing import Optional # 👈 new imports
# from functools import lru_cache

# from pydantic_settings import BaseSettings
# print('<<<<<<<<<<<<<<<<<<<<<')
# class Settings(BaseSettings):
#     auth0_domain: str
#     auth0_api_audience: str
#     auth0_issuer: str
#     auth0_algorithms: str

#     class Config:
#         env_file = ".env"

# @lru_cache()
# def get_settings():
#     return Settings()

# class UnauthorizedException(HTTPException):
#     def __init__(self, detail: str, **kwargs):
# # """Returns HTTP 403"""
#         super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

# class UnauthenticatedException(HTTPException):
#     def __init__(self):
#         super().__init__(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
#         )
# print("))))))))))))))))))))))))))s")
# class VerifyToken:
#     """Does all the token verification using PyJWT"""

#     def __init__(self):
#         self.config = get_settings()

#         # This gets the JWKS from a given URL and does processing so you can
#         # use any of the keys available
#         jwks_url = f'https://{self.config.auth0_domain}/.well-known/jwks.json'
#         self.jwks_client = jwt.PyJWKClient(jwks_url)

#     print(")((((((((((((()))))))))))))")
#     async def verify(self,
#                      security_scopes: SecurityScopes,
#                      token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
#                      ):
#         print("verify function")
#         if token is None:
#             raise UnauthenticatedException

#         # This gets the 'kid' from the passed token
#         try:
#             signing_key = self.jwks_client.get_signing_key_from_jwt(
#                 token.credentials
#             ).key
#         except jwt.exceptions.PyJWKClientError as error:
#             raise UnauthorizedException(str(error))
#         except jwt.exceptions.DecodeError as error:
#             raise UnauthorizedException(str(error))

#         try:
#             payload = jwt.decode(
#                 token.credentials,
#                 signing_key,
#                 algorithms=self.config.auth0_algorithms,
#                 audience=self.config.auth0_api_audience,
#                 issuer=self.config.auth0_issuer,
#             )
#         except Exception as error:
#             raise UnauthorizedException(str(error))
    
#         print(payload)
#         print(">>>>>>>>>>>>>>>>>>>>>>>")
#         return payload
# auth = VerifyToken()
# server = FastAPI()
# @server.get("/api/private")
# def private(auth_result: str = Security(auth.verify)): # 👈 Use Security and the verify method to protect your endpoints
#     """A valid access token is required to access this route"""
#     return auth_result
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InF3VWp0ZVhISU1xeTRCNnNLSDRqSSJ9.eyJpc3MiOiJodHRwczovL2Rldi12Z3dvbDRycmtieXJpNXNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMaVJXdG0zM0hlY2VxdzdLODMzcWRVQzJxT1FKVGJKV0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtdmd3b2w0cnJrYnlyaTVzbS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTczODA2NTkzOSwiZXhwIjoxNzM4MTUyMzM5LCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIHJlYWQ6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX2N1c3RvbV9ibG9ja3MgZGVsZXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBjcmVhdGU6dXNlcl90aWNrZXRzIHJlYWQ6Y2xpZW50cyB1cGRhdGU6Y2xpZW50cyBkZWxldGU6Y2xpZW50cyBjcmVhdGU6Y2xpZW50cyByZWFkOmNsaWVudF9rZXlzIHVwZGF0ZTpjbGllbnRfa2V5cyBkZWxldGU6Y2xpZW50X2tleXMgY3JlYXRlOmNsaWVudF9rZXlzIHJlYWQ6Y29ubmVjdGlvbnMgdXBkYXRlOmNvbm5lY3Rpb25zIGRlbGV0ZTpjb25uZWN0aW9ucyBjcmVhdGU6Y29ubmVjdGlvbnMgcmVhZDpyZXNvdXJjZV9zZXJ2ZXJzIHVwZGF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGRlbGV0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGNyZWF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIHJlYWQ6ZGV2aWNlX2NyZWRlbnRpYWxzIHVwZGF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgZGVsZXRlOmRldmljZV9jcmVkZW50aWFscyBjcmVhdGU6ZGV2aWNlX2NyZWRlbnRpYWxzIHJlYWQ6cnVsZXMgdXBkYXRlOnJ1bGVzIGRlbGV0ZTpydWxlcyBjcmVhdGU6cnVsZXMgcmVhZDpydWxlc19jb25maWdzIHVwZGF0ZTpydWxlc19jb25maWdzIGRlbGV0ZTpydWxlc19jb25maWdzIHJlYWQ6aG9va3MgdXBkYXRlOmhvb2tzIGRlbGV0ZTpob29rcyBjcmVhdGU6aG9va3MgcmVhZDphY3Rpb25zIHVwZGF0ZTphY3Rpb25zIGRlbGV0ZTphY3Rpb25zIGNyZWF0ZTphY3Rpb25zIHJlYWQ6ZW1haWxfcHJvdmlkZXIgdXBkYXRlOmVtYWlsX3Byb3ZpZGVyIGRlbGV0ZTplbWFpbF9wcm92aWRlciBjcmVhdGU6ZW1haWxfcHJvdmlkZXIgYmxhY2tsaXN0OnRva2VucyByZWFkOnN0YXRzIHJlYWQ6aW5zaWdodHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpsb2dzX3VzZXJzIHJlYWQ6c2hpZWxkcyBjcmVhdGU6c2hpZWxkcyB1cGRhdGU6c2hpZWxkcyBkZWxldGU6c2hpZWxkcyByZWFkOmFub21hbHlfYmxvY2tzIGRlbGV0ZTphbm9tYWx5X2Jsb2NrcyB1cGRhdGU6dHJpZ2dlcnMgcmVhZDp0cmlnZ2VycyByZWFkOmdyYW50cyBkZWxldGU6Z3JhbnRzIHJlYWQ6Z3VhcmRpYW5fZmFjdG9ycyB1cGRhdGU6Z3VhcmRpYW5fZmFjdG9ycyByZWFkOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGRlbGV0ZTpndWFyZGlhbl9lbnJvbGxtZW50cyBjcmVhdGU6Z3VhcmRpYW5fZW5yb2xsbWVudF90aWNrZXRzIHJlYWQ6dXNlcl9pZHBfdG9rZW5zIGNyZWF0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIGRlbGV0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIHJlYWQ6Y3VzdG9tX2RvbWFpbnMgZGVsZXRlOmN1c3RvbV9kb21haW5zIGNyZWF0ZTpjdXN0b21fZG9tYWlucyB1cGRhdGU6Y3VzdG9tX2RvbWFpbnMgcmVhZDplbWFpbF90ZW1wbGF0ZXMgY3JlYXRlOmVtYWlsX3RlbXBsYXRlcyB1cGRhdGU6ZW1haWxfdGVtcGxhdGVzIHJlYWQ6bWZhX3BvbGljaWVzIHVwZGF0ZTptZmFfcG9saWNpZXMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgZGVsZXRlOnJvbGVzIHVwZGF0ZTpyb2xlcyByZWFkOnByb21wdHMgdXBkYXRlOnByb21wdHMgcmVhZDpicmFuZGluZyB1cGRhdGU6YnJhbmRpbmcgZGVsZXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIHJlYWQ6bGltaXRzIHVwZGF0ZTpsaW1pdHMgY3JlYXRlOnJvbGVfbWVtYmVycyByZWFkOnJvbGVfbWVtYmVycyBkZWxldGU6cm9sZV9tZW1iZXJzIHJlYWQ6ZW50aXRsZW1lbnRzIHJlYWQ6YXR0YWNrX3Byb3RlY3Rpb24gdXBkYXRlOmF0dGFja19wcm90ZWN0aW9uIHJlYWQ6b3JnYW5pemF0aW9uc19zdW1tYXJ5IGNyZWF0ZTphdXRoZW50aWNhdGlvbl9tZXRob2RzIHJlYWQ6YXV0aGVudGljYXRpb25fbWV0aG9kcyB1cGRhdGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyBkZWxldGU6YXV0aGVudGljYXRpb25fbWV0aG9kcyByZWFkOm9yZ2FuaXphdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbnMgZGVsZXRlOm9yZ2FuaXphdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcnMgZGVsZXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJzIGNyZWF0ZTpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgcmVhZDpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgdXBkYXRlOm9yZ2FuaXphdGlvbl9jb25uZWN0aW9ucyBkZWxldGU6b3JnYW5pemF0aW9uX2Nvbm5lY3Rpb25zIGNyZWF0ZTpvcmdhbml6YXRpb25fbWVtYmVyX3JvbGVzIHJlYWQ6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBkZWxldGU6b3JnYW5pemF0aW9uX21lbWJlcl9yb2xlcyBjcmVhdGU6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIHJlYWQ6b3JnYW5pemF0aW9uX2ludml0YXRpb25zIGRlbGV0ZTpvcmdhbml6YXRpb25faW52aXRhdGlvbnMgcmVhZDpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV9jb25maWcgdXBkYXRlOnNjaW1fY29uZmlnIGRlbGV0ZTpzY2ltX2NvbmZpZyBjcmVhdGU6c2NpbV90b2tlbiByZWFkOnNjaW1fdG9rZW4gZGVsZXRlOnNjaW1fdG9rZW4gZGVsZXRlOnBob25lX3Byb3ZpZGVycyBjcmVhdGU6cGhvbmVfcHJvdmlkZXJzIHJlYWQ6cGhvbmVfcHJvdmlkZXJzIHVwZGF0ZTpwaG9uZV9wcm92aWRlcnMgZGVsZXRlOnBob25lX3RlbXBsYXRlcyBjcmVhdGU6cGhvbmVfdGVtcGxhdGVzIHJlYWQ6cGhvbmVfdGVtcGxhdGVzIHVwZGF0ZTpwaG9uZV90ZW1wbGF0ZXMgY3JlYXRlOmVuY3J5cHRpb25fa2V5cyByZWFkOmVuY3J5cHRpb25fa2V5cyB1cGRhdGU6ZW5jcnlwdGlvbl9rZXlzIGRlbGV0ZTplbmNyeXB0aW9uX2tleXMgcmVhZDpzZXNzaW9ucyBkZWxldGU6c2Vzc2lvbnMgcmVhZDpyZWZyZXNoX3Rva2VucyBkZWxldGU6cmVmcmVzaF90b2tlbnMgY3JlYXRlOnNlbGZfc2VydmljZV9wcm9maWxlcyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlcyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVzIGRlbGV0ZTpzZWxmX3NlcnZpY2VfcHJvZmlsZXMgY3JlYXRlOnNzb19hY2Nlc3NfdGlja2V0cyBkZWxldGU6c3NvX2FjY2Vzc190aWNrZXRzIHJlYWQ6Zm9ybXMgdXBkYXRlOmZvcm1zIGRlbGV0ZTpmb3JtcyBjcmVhdGU6Zm9ybXMgcmVhZDpmbG93cyB1cGRhdGU6Zmxvd3MgZGVsZXRlOmZsb3dzIGNyZWF0ZTpmbG93cyByZWFkOmZsb3dzX3ZhdWx0IHJlYWQ6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgdXBkYXRlOmZsb3dzX3ZhdWx0X2Nvbm5lY3Rpb25zIGRlbGV0ZTpmbG93c192YXVsdF9jb25uZWN0aW9ucyBjcmVhdGU6Zmxvd3NfdmF1bHRfY29ubmVjdGlvbnMgcmVhZDpmbG93c19leGVjdXRpb25zIGRlbGV0ZTpmbG93c19leGVjdXRpb25zIHJlYWQ6Y29ubmVjdGlvbnNfb3B0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnNfb3B0aW9ucyByZWFkOnNlbGZfc2VydmljZV9wcm9maWxlX2N1c3RvbV90ZXh0cyB1cGRhdGU6c2VsZl9zZXJ2aWNlX3Byb2ZpbGVfY3VzdG9tX3RleHRzIHJlYWQ6Y2xpZW50X2NyZWRlbnRpYWxzIGNyZWF0ZTpjbGllbnRfY3JlZGVudGlhbHMgdXBkYXRlOmNsaWVudF9jcmVkZW50aWFscyBkZWxldGU6Y2xpZW50X2NyZWRlbnRpYWxzIHJlYWQ6b3JnYW5pemF0aW9uX2NsaWVudF9ncmFudHMgY3JlYXRlOm9yZ2FuaXphdGlvbl9jbGllbnRfZ3JhbnRzIGRlbGV0ZTpvcmdhbml6YXRpb25fY2xpZW50X2dyYW50cyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsImF6cCI6IkxpUld0bTMzSGVjZXF3N0s4MzNxZFVDMnFPUUpUYkpXIn0.KCBn7IpMBDHMpBbYEkh1AzSyq0u1PzKu1uw8BNg1I0cqcGvu0agxI87JApaqp-OLv89AO6RW0sPp3oTRYd7fEOrwlxMqwMxb32EDt3i8WD-mu0s69yndR_YDoAgF8C56iJyUOwBcmLT9J3GFTI6_tr9cn1Qdryz9fSna6kMVe3dksI20ST3beCllXuP1sezfx7LAXAXM9Kv_fN7DxfeK_Qj2E4GGCEJwd5RtjjF9mGL7qG2q4nWlU3aDvddrP2HJAg-_7XORnU00F1-81P2wN_dq7dgPE-CFQ0tsYGNWvvS5LFJCeODhwV_Uxa4jJK0m4M2be3372eV9eA_hBsbxWw'
# import requests
# import requests
# # Define your Auth0 Management API credentials
# DOMAIN = "dev-vgwol4rrkbyri5sm.us.auth0.com"  # e.g., your-tenant-name.us.auth0.com
# CLIENT_ID = "BxxmEvkITReWi9zNi3kCH1dN07SyosyR"
# CLIENT_SECRET = "BXmzzrpCMO3TPL4GRZUqa9WyvY5lnzSoqSwwvCJi3C9gBejUwgrjt_kdy99hljtJ"

# # Default role ID (replace with your actual Role ID from Auth0)
# DEFAULT_ROLE_ID = "rol_a1GnXsQJ0x5k6aGG"

# # Function to get a Management API token
# def get_management_api_token():
#     print('get_management')
#     url = f"https://{DOMAIN}/oauth/token"
#     payload ={"client_id":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","client_secret":"BXmzzrpCMO3TPL4GRZUqa9WyvY5lnzSoqSwwvCJi3C9gBejUwgrjt_kdy99hljtJ","audience":"https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/","grant_type":"client_credentials"}
#     response = requests.post(url, json=payload)
#     response.raise_for_status()
#     return response.json()["access_token"]

# # Function to assign a default role to a user
# def assign_role_to_user(user_id, role_id, management_api_token):
#     print('adign role')
#     # /api679930608691b45039cb4e39/v2/users/{id}/roles
#     url = f"https://{DOMAIN}/api/v2/users/{user_id}/roles"
#     headers = {"Authorization": f"Bearer {token}"}
#     payload = {"roles": [role_id]}
#     response = requests.post(url, json=payload, headers=headers)
#     response.raise_for_status()

# # Main function to handle role assignment
# def assign_default_role(event):
#     print('assign default role')
#     try:
#         # Get the Management API token
#         management_api_token = get_management_api_token()

#         # Assign the default role to the user
#         assign_role_to_user(event["user_id"], DEFAULT_ROLE_ID, management_api_token)
#         print(f"Assigned default role to user: {event['email']}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error assigning default role: {e}")
#         raise Exception("Failed to assign default role to user.")

# # Example usage
# # if _name_ == "_main_":
# #     # Simulating the event object from Auth0
# user_id = 'auth0|'
# email = 'test@gmail.com'
# event = {"user_id": f"{user_id}", "email": f"{email}",}
# assign_default_role(event)
# import requests
# payload_token = {"client_id":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","client_secret":"BXmzzrpCMO3TPL4GRZUqa9WyvY5lnzSoqSwwvCJi3C9gBejUwgrjt_kdy99hljtJ","audience":"https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/","grant_type":"client_credentials"}
# response_token = requests.post("https://dev-vgwol4rrkbyri5sm.us.auth0.com/oauth/token", payload_token)
# print(response_token.json())
# import requests

# # Define variables
# auth0_domain = "dev-vgwol4rrkbyri5sm.us.auth0.com"
# org_id = "org_aLcJT0uNXhLc74Ay"
# user_id = "auth0|6799c0d5c9712fb29560c7b6"
# access_token = f"{token}"
# role_ids = 'rol_a1GnXsQJ0x5k6aGG'

# # API endpoint
# url = 'https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/organizations/org_aLcJT0uNXhLc74Ay/members/auth0|679930608691b45039cb4e39/roles'

# # Headers
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Cache-Control": "no-cache",
#     "Content-Type": "application/json"
# }

# # Payload
# data = {"roles": role_ids}

# # Make the POST request
# response = requests.post(url, headers=headers, json=data)

# # Print response
# print(response.status_code)
# # print(response.json())
# import requests

# def assign_role(user_id, domain, client_id, client_secret, role_id):
#     # Get Auth0 management API token
#     # token_url = 'https://dev-vgwol4rrkbyri5sm.us.auth0.com/oauth/token'
#     # token_payload = {
#     #     "client_id": client_id,
#     #     "client_secret": client_secret,
#     #     "audience": f"https://{domain}/api/v2/",
#     #     "grant_type": "client_credentials"
#     # }
#     payload_token  = {"client_id":"LiRWtm33Heceqw7K833qdUC2qOQJTbJW","client_secret":"HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er","audience":"https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/","grant_type":"client_credentials"}
#     response_token = requests.post("https://dev-vgwol4rrkbyri5sm.us.auth0.com/oauth/token", payload_token)
#     # print(response_token.json()['access_token'])
#     access_token = response_token.json()['access_token']
#     response_token.raise_for_status()
#     # access_token = token_response.json()["access_token"]
    
#     # Assign role to user
#     assign_role_url = f"https://{domain}/api/v2/users/{user_id}/roles"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     data = {"roles": [role_id]}
    
#     try:
#         response = requests.post(assign_role_url, json=data, headers=headers)
#         response.raise_for_status()
#         print("Role assigned successfully.")
#     except requests.exceptions.RequestException as e:
#         print(f"Error assigning role: {e}")



# DOMAIN = "dev-vgwol4rrkbyri5sm.us.auth0.com" 
# CLIENT_ID = "BxxmEvkITReWi9zNi3kCH1dN07SyosyR"
# CLIENT_SECRET = "HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er"
# DEFAULT_ROLE_ID = "rol_a1GnXsQJ0x5k6aGG"

# # Default role ID (replace with your actual Role ID from Auth0)
# user_id = "auth0|6799cb298aea20c2a60787d0"     
# print(assign_role(user_id, DOMAIN, CLIENT_ID, CLIENT_SECRET, DEFAULT_ROLE_ID))
# # import requests
# # payload_token = {"client_id":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","client_secret":"BXmzzrpCMO3TPL4GRZUqa9WyvY5lnzSoqSwwvCJi3C9gBejUwgrjt_kdy99hljtJ","audience":"https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/","grant_type":"client_credentials"}
# # response_token = requests.post("https://dev-vgwol4rrkbyri5sm.us.auth0.com/oauth/token", payload_token)
# # print(response_token.json())
# import requests
# import json

# headers = {
#   ,
#   "token-type": "Bearer",
#   "content-type": "application/json"
# }
#  CLIENT_ID = "BxxmEvkITReWi9zNi3kCH1dN07SyosyR"
# CLIENT_SECRET = "HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er"

# headers = {"content-type":"application/json" ,'Authorization': f"Bearer {access_token}"}
# url = "https://dev-vgwol4rrkbyri5sm.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api/groups"
# data = {
#     "client_id": "LiRWtm33Heceqw7K833qdUC2qOQJTbJW",
#     "client_secret": "HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er",
#     "audience": "urn:auth0-authz-api",
#     "grant_type": "client_credentials"
# }

# print(headers)
# d=json.dumps(data)
# print(d)
# payload = "{\"client_id\":\"LiRWtm33Heceqw7K833qdUC2qOQJTbJW\",\"client_secret\":\"HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er\",\"audience\":\"urn:auth0-authz-api\",\"grant_type\":\"client_credentials\"}"

# access_token = { 'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InF3VWp0ZVhISU1xeTRCNnNLSDRqSSJ9.eyJpc3MiOiJodHRwczovL2Rldi12Z3dvbDRycmtieXJpNXNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMaVJXdG0zM0hlY2VxdzdLODMzcWRVQzJxT1FKVGJKV0BjbGllbnRzIiwiYXVkIjoidXJuOmF1dGgwLWF1dGh6LWFwaSIsImlhdCI6MTczODE0NjY2NCwiZXhwIjoxNzM4MjMzMDY0LCJzY29wZSI6InJlYWQ6dXNlcnMgcmVhZDphcHBsaWNhdGlvbnMgcmVhZDpjb25uZWN0aW9ucyByZWFkOmNvbmZpZ3VyYXRpb24gdXBkYXRlOmNvbmZpZ3VyYXRpb24gcmVhZDpncm91cHMgY3JlYXRlOmdyb3VwcyB1cGRhdGU6Z3JvdXBzIGRlbGV0ZTpncm91cHMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgdXBkYXRlOnJvbGVzIGRlbGV0ZTpyb2xlcyByZWFkOnBlcm1pc3Npb25zIGNyZWF0ZTpwZXJtaXNzaW9ucyB1cGRhdGU6cGVybWlzc2lvbnMgZGVsZXRlOnBlcm1pc3Npb25zIHJlYWQ6cmVzb3VyY2Utc2VydmVyIGNyZWF0ZTpyZXNvdXJjZS1zZXJ2ZXIgdXBkYXRlOnJlc291cmNlLXNlcnZlciBkZWxldGU6cmVzb3VyY2Utc2VydmVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiYXpwIjoiTGlSV3RtMzNIZWNlcXc3SzgzM3FkVUMycU9RSlRiSlciLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnVzZXJzIiwicmVhZDphcHBsaWNhdGlvbnMiLCJyZWFkOmNvbm5lY3Rpb25zIiwicmVhZDpjb25maWd1cmF0aW9uIiwidXBkYXRlOmNvbmZpZ3VyYXRpb24iLCJyZWFkOmdyb3VwcyIsImNyZWF0ZTpncm91cHMiLCJ1cGRhdGU6Z3JvdXBzIiwiZGVsZXRlOmdyb3VwcyIsInJlYWQ6cm9sZXMiLCJjcmVhdGU6cm9sZXMiLCJ1cGRhdGU6cm9sZXMiLCJkZWxldGU6cm9sZXMiLCJyZWFkOnBlcm1pc3Npb25zIiwiY3JlYXRlOnBlcm1pc3Npb25zIiwidXBkYXRlOnBlcm1pc3Npb25zIiwiZGVsZXRlOnBlcm1pc3Npb25zIiwicmVhZDpyZXNvdXJjZS1zZXJ2ZXIiLCJjcmVhdGU6cmVzb3VyY2Utc2VydmVyIiwidXBkYXRlOnJlc291cmNlLXNlcnZlciIsImRlbGV0ZTpyZXNvdXJjZS1zZXJ2ZXIiXX0.LeOGd1LXLcU_ihd5hlUUuwFrpPETn1OmQYCOSxYbQGix5EvPa5GeVJ2i14LPKhVJkPGz3XtWFcehYpJCO2x5PtOR_6I8zbolPjeWV2JEyihA9SCX1YlOqe_WYuq4a_cBLm5ry4Jv-SVxN26rH02J6oNnJQjmNNd8ykcK8Dk--CqnTGM0fO9_JqKCTwn2Yuebq2tu7DdYnGgCtvCfHfOnOiBgofOXUYR5CS3YbRp0md794lRF5OznO2BfL8UuejScj6eNuq08nEGKYMTke9ZXazg3-zmgD8Q_VH_6Sp7zFiV1Ou9I7MqaC7m0v9iO4reWrmdAySHArNrVWHbx-ZF3gg" }
# data = { 'content-type': "application/json"}
# response = requests("GET", "/", headers=headers, )
# response = requests.post(url,data=json.dumps(data), headers=headers)

# print(response.json())

# token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InF3VWp0ZVhISU1xeTRCNnNLSDRqSSJ9.eyJpc3MiOiJodHRwczovL2Rldi12Z3dvbDRycmtieXJpNXNtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJMaVJXdG0zM0hlY2VxdzdLODMzcWRVQzJxT1FKVGJKV0BjbGllbnRzIiwiYXVkIjoidXJuOmF1dGgwLWF1dGh6LWFwaSIsImlhdCI6MTczODE0ODQ2MCwiZXhwIjoxNzM4MjM0ODYwLCJzY29wZSI6InJlYWQ6dXNlcnMgcmVhZDphcHBsaWNhdGlvbnMgcmVhZDpjb25uZWN0aW9ucyByZWFkOmNvbmZpZ3VyYXRpb24gdXBkYXRlOmNvbmZpZ3VyYXRpb24gcmVhZDpncm91cHMgY3JlYXRlOmdyb3VwcyB1cGRhdGU6Z3JvdXBzIGRlbGV0ZTpncm91cHMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgdXBkYXRlOnJvbGVzIGRlbGV0ZTpyb2xlcyByZWFkOnBlcm1pc3Npb25zIGNyZWF0ZTpwZXJtaXNzaW9ucyB1cGRhdGU6cGVybWlzc2lvbnMgZGVsZXRlOnBlcm1pc3Npb25zIHJlYWQ6cmVzb3VyY2Utc2VydmVyIGNyZWF0ZTpyZXNvdXJjZS1zZXJ2ZXIgdXBkYXRlOnJlc291cmNlLXNlcnZlciBkZWxldGU6cmVzb3VyY2Utc2VydmVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwiYXpwIjoiTGlSV3RtMzNIZWNlcXc3SzgzM3FkVUMycU9RSlRiSlciLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnVzZXJzIiwicmVhZDphcHBsaWNhdGlvbnMiLCJyZWFkOmNvbm5lY3Rpb25zIiwicmVhZDpjb25maWd1cmF0aW9uIiwidXBkYXRlOmNvbmZpZ3VyYXRpb24iLCJyZWFkOmdyb3VwcyIsImNyZWF0ZTpncm91cHMiLCJ1cGRhdGU6Z3JvdXBzIiwiZGVsZXRlOmdyb3VwcyIsInJlYWQ6cm9sZXMiLCJjcmVhdGU6cm9sZXMiLCJ1cGRhdGU6cm9sZXMiLCJkZWxldGU6cm9sZXMiLCJyZWFkOnBlcm1pc3Npb25zIiwiY3JlYXRlOnBlcm1pc3Npb25zIiwidXBkYXRlOnBlcm1pc3Npb25zIiwiZGVsZXRlOnBlcm1pc3Npb25zIiwicmVhZDpyZXNvdXJjZS1zZXJ2ZXIiLCJjcmVhdGU6cmVzb3VyY2Utc2VydmVyIiwidXBkYXRlOnJlc291cmNlLXNlcnZlciIsImRlbGV0ZTpyZXNvdXJjZS1zZXJ2ZXIiXX0.i1hEgrVNK1XsexIYqzB38JNAw1_H9STr9iqLYxq6DYKhzOMk7EGys-QMu7f9ZvwQzDIPHQiTJk_mWOlmNzTo6slFCG5bkwrO1WvraBzgUN4-ISTN7b2mmVBuJj18Ph4Et95EzrGXQyejF7zDn9gqPk4O1n-xEtTpjIbWJUMaVAYW5GBDkyZHUDuaeYYXGTkWdGzg_RWrMViji45xTPYkfgbJJYOV68gloLYsjzGzhO8wrJVW3HStWAtQI-MYAGdcz4uU6GSHbVeXXtuMbomJMRz_VmlSZtVk--DTWwjC_ntBu8IL5S3GYLLDjNUEwairHd4MVrposDspSrAX7Ug1vg"
# api_url = 'https://dev-vgwol4rrkbyri5sm.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api/groups'
# auth_token = token

# # Set the headers for authentication and content type
# headers = {
#     "Authorization": f"Bearer {auth_token}",
#     "Content-Type": "application/json"
# }

# # Make the GET request to fetch the groups
# response = requests.get(api_url, headers=headers)

# # Check if the request was successful

#     # Parse the response JSON
# groups = response.json()
# print(groups)
# print(groups["roles"][0])


# # import requests
# # import json

# # # Replace with actual values
# # extension_url = "https://dev-vgwol4rrkbyri5sm.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api"
# # group_id = "0cc4a247-210c-4f3b-8912-65ba81d15718"
# # access_token = token
# # user_id = "auth0|6799c9978aea20c2a607868d"

# # # url = f"https://{extension_url}/groups/{group_id}/members"
# # url = "https://dev-vgwol4rrkbyri5sm.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api/groups/0cc4a247-210c-4f3b-8912-65ba81d15718/members"

# # url = url

# # # Headers
# # headers = {
# #     "Authorization": f"Bearer {access_token}",
# #     "Content-Type": "application/json"
# # }

# # # Data
# # data = json.dumps([user_id])

# # # Send PATCH request
# # try:
# #     response = requests.patch(url, headers=headers, data=data)
    
# #     if response.status_code == 204:
# #         print("✅ Member added successfully! (204 No Content)")
# #     elif response.status_code == 200:
# #         print("✅ Member added successfully:", response.json())
# #     else:
# #         print(f"⚠️ Failed to update members. Status code: {response.status_code}")
# #         print("Response:", response.text)

# # except requests.exceptions.RequestException as e:
# #     print("❌ Error:", e)
# groups = {"groups":[{"_id":"0cc4a247-210c-4f3b-8912-65ba81d15718","name":"users","description":"Default Roles and permissions","members":[]},{"_id":"cfd5f00a-0f44-4b22-966e-bf22d8f6f40d","name":"Manager","description":"Management Group","roles":["12eea30d-fb38-4138-b7bc-b4f0723069a2"]}],"roles":[{"applicationType":"client","applicationId":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","description":"USER ROLE","name":"USER","permissions":[],"_id":"c56d1d6b-8307-470d-8ecd-450186f9b6a2"},{"applicationType":"client","applicationId":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","description":"ADMIN ROLE","name":"ADMIN","permissions":[],"_id":"12eea30d-fb38-4138-b7bc-b4f0723069a2"}],"permissions":[{"_id":"dac9478d-de0b-483b-a2d0-a3ed38d78888","applicationType":"client","applicationId":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","description":"Access read/write permission","name":"read/write"},{"applicationType":"client","applicationId":"BxxmEvkITReWi9zNi3kCH1dN07SyosyR","description":"Access write permission","name":"write","_id":"bd28a123-919e-44db-a10e-878415b326b7"}]}

# print(groups["groups"][0]['_id'])
#assign default role to the user
# def assign_default_role(user_id):
#     payload_token  = {"client_id":f"{CLIENT_ID_API}","client_secret":f"{CLIENT_SECRET_API}","audience":"https://dev-vgwol4rrkbyri5sm.us.auth0.com/api/v2/","grant_type":"client_credentials"}
#     response_token = requests.post(f"https://{DOMAIN}/oauth/token", payload_token)
#     if response_token.status_code==200:
#         access_token = response_token.json()['access_token']
#     else:
#         print("access_token")
#     response_token.raise_for_status()
#     # Assign role to user
#     assign_role_url = f"https://{DOMAIN}/api/v2/users/{user_id}/roles"
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Content-Type": "application/json"
#     }
#     DEFAULT_ROLE_ID = "rol_a1GnXsQJ0x5k6aGG"
#     data = {"roles": [DEFAULT_ROLE_ID]}
#     #excpetion handling
#     try:
#         response = requests.post(assign_role_url, json=data, headers=headers)
#         response.raise_for_status()
#         print("Default Role assigned successfully.")
#     except requests.exceptions.RequestException as e:
#         print(f"Error assigning role: {e}")




# import requests
# import json

# # API URL
# url = "https://dev-vgwol4rrkbyri5sm.us.auth0.com/oauth/token"

# # Headers
# headers = {
#     "Content-Type": "application/json"
# }

# # Request Body (Data)
# data = {
#     "client_id": "LiRWtm33Heceqw7K833qdUC2qOQJTbJW",
#     "client_secret": "HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er",
#     "audience": "urn:auth0-authz-api",
#     "grant_type": "client_credentials"
# }

# # Send POST request
# response = requests.post(url, headers=headers, json=data)

# # Handle response
# if response.status_code == 200:
#     token_info = response.json()
#     print("✅ Access Token:", token_info.get("access_token"))
# else:
#     print(f"❌ Failed to fetch token. Status code: {response.status_code}")
# #     print("Response:", response.text)
# DOMAIN = dev-vgwol4rrkbyri5sm.us.auth0.com 
# CLIENT_ID_API = LiRWtm33Heceqw7K833qdUC2qOQJTbJW
# CLIENT_SECRET_API = HiW4jGOwmShbMN1Kl7MfH19BGgQznNht9pmrNYpR1eVnNf7TGwNKVWHod92Xr3Er
# CLIENT_ID_APP = BxxmEvkITReWi9zNi3kCH1dN07SyosyR
# CLIENT_SECRET_APP = BXmzzrpCMO3TPL4GRZUqa9WyvY5lnzSoqSwwvCJi3C9gBejUwgrjt_kdy99hljtJ
# DEFAULT_ROLE_ID = rol_a1GnXsQJ0x5k6aGG
# URL_EXTENTION = https://dev-vgwol4rrkbyri5sm.us.webtask.run/adf6e2f2b84784b57522e3b19dfc9201/api
# # AUTH0_API_AUDIENCE = https://microapis.io/api/orders
# REDIRECT_URI_TOKEN = http://localhost:8000/token
# REDIRECT_URI_DOCS = http://localhost:8000/docs
# # AUTH0_ISSUER = https://your.domain.auth0.com/
# # AUTH0_ALGORITHMS = RS256