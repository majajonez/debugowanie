from time import perf_counter_ns

def debug(funkcja):
    def wewnetrzna(*args):
        print("nazwa f: " + str(funkcja.__name__))           # wypisanie nazwy wywolanej funkcji
        t = perf_counter_ns()
        w = funkcja(*args)
        t = perf_counter_ns() - t
        print('parametry funkcji:')
        for a in args:
            print(a)                                        # wypisanie parametrów funkcji
        print("wynik: " + str(w))                           # wypisanie wyniku funkcji
        print("czas w milisekundach: " + str(t /1000000))      # czas wykonywania funkcji
        return w
    return wewnetrzna
