from dynatrace_workbench import *

url = ''

dyna_env = dynatrace_workbench.init()
response = dyna_env.get_request(url)
print(response.content)