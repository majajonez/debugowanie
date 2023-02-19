from time import perf_counter_ns

def debug(function):
    def internal_f(*args):
        print("name f: " + str(function.__name__))           # wypisanie nazwy wywolanej funkcji
        t = perf_counter_ns()
        r = function(*args)
        t = perf_counter_ns() - t
        print('function parameters:')
        for a in args:
            print(a)                                        # wypisanie parametrów funkcji
        print("result: " + str(r))                           # wypisanie wyniku funkcji
        print("time in milliseconds: " + str(t /1000000))      # czas wykonywania funkcji
        return r
    return internal_f
