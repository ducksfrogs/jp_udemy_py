def print_more(func):
    def wrapper(*args, **kwargs):
        print('funk:', func.__name__)
        print('args:', args)
        print('kargs:', args)
        result = func(*args, **kwargs)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_more
def add_num(a, b):
    return a + b

f = print_info(add_num)

r = f(10,20)
print(r)
