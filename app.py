from dynatrace_workbench import *

url = 'https://buo56994.dev.dynatracelabs.com/api/v2/apiTokens'

dyna_env = dynatrace_workbench.init()
response = dyna_env.get_request(url)
print(response.content)