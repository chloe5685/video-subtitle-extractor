# 每次拉2个任务, 默认4
CELERYD_PREFETCH_MULTIPLIER = 2
CELERYD_FORCE_EXECV = True # 非常重要,有些情况下可以防止死锁
CELERYD_FORCE = True
# CELERYD_TASK_TIME_LIMIT = 60    # 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死

CELERY_TASK_ACKS_LATE = True
# BROKER_TRANSPORT_OPTIONS = {'socket_timeout': 5, 'visiblity_timeout': 20,'fanout_prefix': True,'fanout_patterns': True,}
# CELERY_REDIS_SOCKET_TIMEOUT = 10
BROKER_TRANSPORT_OPTIONS = {'socket_timeout': 30, 'visiblity_timeout': 30,'fanout_prefix': True,'fanout_patterns': True,}
CELERY_REDIS_SOCKET_TIMEOUT = 30
CELERY_REDIS_SOCKET_KEEPALIVE = True
CELERY_REDIS_RETRY_ON_TIMEOUT = True

# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True
