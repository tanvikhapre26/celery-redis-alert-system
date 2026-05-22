from celery import Celery
import time

app = Celery (
	'alert',
	broker= 'redis://localhost:6379/0'
)

@app.task
def process_alert(device, temperature ):
	print(f" Checking {device}")
	time.sleep(5)

	if temperature > 40:
		print(f" ALERT: HIGH temperature in {device}")
	else:
		print(f"{device} Normal")