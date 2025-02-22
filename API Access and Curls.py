'''
https://github.com/calbergs/spotify-api/blob/master/setup/spotify_api_access.md
from https://github.com/calbergs/spotify-api/tree/master?tab=readme-ov-file

http%3A%2F%2Flocalhost%3A8888%2Fcallback%2F
https://accounts.spotify.com/authorize?client_id=84f1a1a15da644ef919dad43b738875d&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8888%2Fcallback%2F&scope=user-read-recently-played

AQA8ni224Af3iLSZx8SVPECk0stQvgNo7WAufUqkCQ0Rv8VysnIxboz1fltgxvJ7N8_Jax0TLdbEBqIsi90AjDdpYNC28c3nGLUmLDTqkx3e9csQ31uTw-3ukaTpOaUYGUWVQIA_79xiLzu88JsNCBf_nyP6M6AMWUDXz-OGcZVY-9z0EZpKdzq91moUAATO-A64ey3zRD6jcoqJu0s
'''
client: 84f1a1a15da644ef919dad43b738875d
secret: 60f8a7091a1641deb129073485998f8d


curl_command = 'curl.exe -d client_id=84f1a1a15da644ef919dad43b738875d -d client_secret=60f8a7091a1641deb129073485998f8d -d grant_type=authorization_code -d code=AQA8ni224Af3iLSZx8SVPECk0stQvgNo7WAufUqkCQ0Rv8VysnIxboz1fltgxvJ7N8_Jax0TLdbEBqIsi90AjDdpYNC28c3nGLUmLDTqkx3e9csQ31uTw-3ukaTpOaUYGUWVQIA_79xiLzu88JsNCBf_nyP6M6AMWUDXz-OGcZVY-9z0EZpKdzq91moUAATO-A64ey3zRD6jcoqJu0s -d redirect_uri=http%3A%2F%2Flocalhost%3A8888%2Fcallback%2F https://accounts.spotify.com/api/token'

response = {"access_token":"BQAUHMqcCJsYLI0UzUMqc8laQt42T4TfHLUN_5zkiMDCmBE9WyP244Undx0bW4ETsg5bqnL74-W1WtJL6ViZ0Ju334rHmHjI4E3dxMwUdVNSyH90NJzHmWUURAtdTPi9t9UIZsrcynG8A4u8j6r9ENObVT9qQoqaMygyokCTqmfDGSIpo7n7eR58EqwIbgs5qrrfaVM4livcUZQHbilJ",
            "token_type":"Bearer",
            "expires_in":3600,
            "refresh_token":"AQA0W1dGlQPhwx7UG0_vpe_U_sMMjoWN-rhpLEPbfcsFWGBUsg3aEBKmlpROgAyfxOKJ52QZpSjlrG-7AuyBH0y0-yqge9zxpyoF5-toNaa-MJc3OQIAgTJ0S7I-H77NM68",
            "scope":"user-read-recently-played"}

# Base64 client:secret --> ODRmMWExYTE1ZGE2NDRlZjkxOWRhZDQzYjczODg3NWQ6NjBmOGE3MDkxYTE2NDFkZWIxMjkwNzM0ODU5OThmOGQ=
# Access token is what we define as spotify_token in our code
# Refresh token will be used to generate a new access token on each run as the access token expires after one hour