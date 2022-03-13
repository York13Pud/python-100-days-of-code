import time
current_time = time.time()
print(current_time)

# This function will determine the time taken to run either the fast or slow functions:
def speed_calc_decorator(function_called_from):
  def wrapper_function():
        start_time = time.time()
        function_called_from()
        end_time = time.time()
        print(f"{function_called_from.__name__} run time: {float(end_time - start_time):.2f} seconds")
        print(f"{function_called_from.__name__} run time: {float((end_time - start_time)/60):.2f} minutes")
  return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()