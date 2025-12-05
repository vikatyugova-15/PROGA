# -*- coding: windows-1251 -*-

import json
import sys
import random
from cm_timer import cm_timer_1

path = 'data_light.json'

with open(path) as f:
    data = json.load(f)

def print_result(test):
    def wrapper(*args, **kwargs):
        result = test(*args, **kwargs)
        if isinstance(result, tuple):
            print(", ".join(map(str, result)))
        elif isinstance(result, dict):
            for k, v in result.items():
                print(f"{k} = {v}")
        else:
            print(result)
        return result
    return wrapper
     
@print_result
def f1(items):
    return sorted(set(item.get("job-name") for item in items if "job-name" in item))

@print_result
def f2(job_names):
    return list(filter(lambda job: 'программист' in job.lower(), job_names))

@print_result
def f3(programmer_jobs):
    return [job + ' с опытом Python' for job in programmer_jobs]

@print_result
def f4(jobs_with_python):
    job = jobs_with_python
    zp = [random.randint(100000, 200000) for i in jobs_with_python]
    return list(zip(job, zp))

# @print_result
# def f1(arg):
#     raise NotImplemented


# @print_result
# def f2(arg):
#     raise NotImplemented


# @print_result
# def f3(arg):
#     raise NotImplemented


# @print_result
# def f4(arg):
#     raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(
            f3(
                f2(
                    f1(data))))