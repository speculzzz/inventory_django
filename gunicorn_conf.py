bind = "unix:/tmp/inventory.sock"
workers = 4
worker_class = "gevent"
timeout = 120
max_requests = 500
max_requests_jitter = 50
