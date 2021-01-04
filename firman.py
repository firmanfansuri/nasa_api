import json
from urllib import request

def write_sol_data(sol, sol_obj):
	try:
		pre_mn = round(sol_obj['PRE']['mn'])
		pre_mx = round(sol_obj['PRE']['mx'])
		print(f"On Sol {sol} the temperatures ranged from error AT ॰C to error AT ॰C with an atmospheric pressure of {pre_mn} Pa to {pre_mx} Pa")
	except:
		pass

nama = "Firman Fansuri Akmal"
nim = "1808001010003"
api_key = "shYQH9r4WKyhxxJOQ8XkXUFMTcH4o42ZAvqi49uo"
url = "https://api.nasa.gov/insight_weather/?api_key="+api_key+"&feedtype=json&ver=1.0"

response = request.urlopen(url)
data = json.loads(response.read())

print("Tugas Sistem Paralel & Terdistribusi")
print("Nama: "+ nama)
print("NIM: "+ nim)

for sol in data['sol_keys']:
	write_sol_data(sol, data[sol])
