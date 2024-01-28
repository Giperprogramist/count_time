import time


def count_time(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        print(func(*args, **kwargs))
        end_time = time.time() - start_time
        print(f"Function time: {end_time}")

    return warpper


@count_time
def list_numb(n):
    list(range(n))


list_numb(900000000)
