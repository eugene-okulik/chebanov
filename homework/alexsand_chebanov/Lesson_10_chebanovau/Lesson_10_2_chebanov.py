def repeat_me(number):
    def finish_me(func):
        def wrapper(*args, **kwargs):
            for i in range(number):
                func(*args, **kwargs)

        return wrapper

    return finish_me


@repeat_me(2)
def example(text):
    print(text)


example('print me')
