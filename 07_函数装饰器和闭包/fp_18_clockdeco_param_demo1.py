import time
from fp_17_clockdeco_param import clock


@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.123)
