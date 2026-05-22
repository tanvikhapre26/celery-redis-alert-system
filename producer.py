from task import process_alert

device = [
	("sensor 1",35),
	("sensor 2",45),
	("sensor 3",50)
]
for d,  t in device:
	process_alert.delay(d,t)
	print("all alerts submitted")