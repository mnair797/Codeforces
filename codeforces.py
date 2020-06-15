import requests
import json
import pandas as pd
url="https://codeforces.com/api/problemset.problems"
JSONContent = requests.get(url).json()
#content = json.dumps(JSONContent, indent = 4, sort_keys=True)
dataset = pd.DataFrame(JSONContent)
dataset.to_csv(codeforces.csv, False)
