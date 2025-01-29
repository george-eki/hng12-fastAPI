

from fastapi import FastAPI
from datetime import datetime
from datetime import timezone


app = FastAPI()

@app.get ("/")
def get_info():
	return {
	  "email": "g_ekhaesomi@yahoo.com",
	  "current_datetime": datetime.now(timezone.utc).isoformat(),
	  "github_url": "https://github.com/george-eki"
	}
