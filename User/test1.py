import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

res = r.set("bike:2", "Process 134")
print(res)

res = r.get("bike:2")
print(res)
# >>> "Process 134"

