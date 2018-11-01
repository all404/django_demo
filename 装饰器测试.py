def my_decorator(func):
    print("装饰器被初始化")

    def wrapper(*args, **kwargs):
        print('装饰器被调用之前')
        result = func(*args, **kwargs)
        print('装饰器被调用之后')
        return result

    return wrapper


def my_decorator2(func):
    print("装饰器222被初始化")

    def wrapper(*args, **kwargs):
        print('装饰器222被调用之前')
        result = func(*args, **kwargs)
        print('装饰器222被调用之后')
        return result

    return wrapper


@my_decorator  # func_demo = my_decorator(func_demo)
@my_decorator2
def func_demo():
    print("方法被调用...")
    return "Haha"

# func_demo = my_decorator(func_demo)


if __name__ == '__main__':
    func_demo()
