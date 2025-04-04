def skill(trigger=None, priority=0, retries=1, backoff="none"):
    def wrapper(func):
        func._trigger = trigger
        func._priority = priority
        func._retries = retries
        func._backoff = backoff
        return func
    return wrapper