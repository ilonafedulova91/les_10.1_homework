from functools import wraps

def log(filename=None):
    """ This is a logger decorator """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def logging(message):
                if filename:
                    with open(filename, 'a') as f:
                        f.write(message + '\n')
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                logging(f'{func.__name__} ok')
                return result
            except Exception as e:
                logging(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}')
                raise
        return wrapper
    return decorator