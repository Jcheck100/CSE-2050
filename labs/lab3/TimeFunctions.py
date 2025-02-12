import time
def time_function(func, args, n_trials = 10):
    time_list = []
    while n_trials != 0:
        start = time.time()
        func(args)
        totaltime = time.time() - start
        time_list.append(totaltime)
        n_trials -= 1
    return sum(time_list)/len(time_list)
    
    
def time_function_flexible(func, args, n_trials = 10):
    time_list = []
    while n_trials != 0:
        start = time.time()
        func(*args)
        totaltime = time.time() - start
        time_list.append(totaltime)
        n_trials -= 1
    return sum(time_list)/len(time_list)