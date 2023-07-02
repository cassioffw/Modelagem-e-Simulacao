import time
import psutil as ps


def random():
    current_time = int(time.time())
    cpu_percent = ps.cpu_percent(1)
    memory = ps.virtual_memory()[3]
    memory_available = ps.virtual_memory().available
    seed = hash((current_time, cpu_percent, memory, memory_available))

    a = 1
    c = 1
    m = 2**32

    seed = (a * seed + c) % m
    return seed / m
