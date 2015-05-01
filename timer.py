import datetime
import gevent
import random
import time


def timer(timeout):
    time.sleep(random.random() * timeout)
    return datetime.datetime.now()

def spawn_timers(count, timeout):
	jobs = [gevent.spawn(timer, timeout) for x in xrange(0, count)]
	gevent.joinall(jobs, timeout=timeout)
	return [job.value for job in jobs]

if __name__ == '__main__':
    print spawn_timers(3, 10)
