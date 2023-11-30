import requests

# Replace with your app's details
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'
team_id = 'cc'
guest_user_email = 'vi@gmail.com'

# Get access token
token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

# Add guest user to the team
teams_url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/memberships'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}
data = {
    'user@odata.bind': f'https://graph.microsoft.com/v1.0/users/{guest_user_email}'
}
response = requests.post(teams_url, headers=headers, json=data)

print(response.status_code, response.json())
