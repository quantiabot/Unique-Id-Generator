import datetime

target="2025-11-19 18:00:00"
convert=datetime.datetime.strptime(target,"%Y-%m-%d %H:%M:%S")
now=datetime.datetime.now()

result=int(now.timestamp() * 1000)
seconds=now.timestamp()

different=str(now - convert).replace(" ", "").replace(":", "").replace(".", "")[:-6]

generated=str(result)[::-1]
final=generated+different

print(final)
