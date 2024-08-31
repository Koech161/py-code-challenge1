def apply_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('after')
    return wrapper
@apply_decorator
def decorator_func():
    print('Decorator Applied')  
decorator_func()    