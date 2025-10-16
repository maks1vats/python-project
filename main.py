def safe_run(func):
    def inner(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            func(a, b)
        else:
            print("Not good")

    return inner


@safe_run
def mnozh(a, b):
    return a * b


mnozh(1, 47)
mnozh("hello", 47)
mnozh("hello", "artem")
