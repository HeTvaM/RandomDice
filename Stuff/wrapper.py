class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def check_amount(func):
    def wrapper(*args, **kwargs):
        if args[0].amount >= 18:
            return

        res = func(args, kwargs)

        return res
    return wrapper
