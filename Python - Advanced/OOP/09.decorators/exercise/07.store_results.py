class store_results:
    def __init__(self, func_ref):
        self.func_ref = func_ref

    def __call__(self, *args, **kwargs):
        with open('results.txt', 'a') as file:
            file.write(f"Function '{self.func_ref.__name__}' was called. Result: {self.func_ref(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
