import multiprocessing

MAX_REQUESTS = 1000
MAX_REQUESTS_JITTER = 50
LOG_FILE = "-"
BIND = "0.0.0.0"

TIMEOUT = 230
# https://learn.microsoft.com/en-us/troubleshoot/azure/app-service/web-apps-performance-faqs#why-does-my-request-time-out-after-230-seconds

num_cpus = multiprocessing.cpu_count()
workers = (num_cpus * 2) + 1
WORKER_CLASS = "uvicorn.workers.UvicornWorker"
