import requests
from pprint import pprint
import json

def batch_get():
	post_data = [
		#parameters can be used with a batch
		{"method":"GET", "relative_url":"events/search/?location.address=San Francisco&page=1"},
		{"method":"GET", "relative_url":"users/me"},
		#expansions can be used with a batch
		{"method":"GET", "relative_url":"users/me/owned_event_attendees/?expand=orders"}
	]
	post_data = json.dumps(post_data)
	batch = requests.post("https://www.eventbriteapi.com/v3/batch/",
						  headers={
							   "Authorization": "Bearer TOKEN",
						  },
						  data={'batch': post_data})

	pprint(batch.json())


batch_get()