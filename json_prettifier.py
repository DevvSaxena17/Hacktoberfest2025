# json_prettifier.py
import json

data = '{"name":"Dev","event":"Hacktoberfest","year":2025}'
parsed = json.loads(data)
print(json.dumps(parsed, indent=4))
