
from collections import deque


class TaskScheduler(object):
    def __init__(self):
        self._queue = deque()
        self._actors = {}


    def new_actor(self, name, actor):
        self._actors[name] = actor
        self._queue.append((actor, None))


    def send(self, name, msg):
        if name not in self._actors:
            raise RuntimeError('actor name %s not exists' % name)

        self._queue.append((self._actors[name], msg))


    def run(self):
        while self._queue:
            try:
                actor, msg = self._queue.popleft()
                actor.send(msg)
            except StopIteration as e:
                print('exception', e)


def printer():
    while 1:
        msg = yield
        print('msg is ', msg)

def counter(scheduler):
    while 1:
        n = yield
        if n == 0:
            return

        scheduler.send('printer', n)
        scheduler.send('counter', n-1)


if __name__ == '__main__':
    actor_scheduler = TaskScheduler()
    actor_scheduler.new_actor('printer', printer())
    actor_scheduler.new_actor('counter', counter(actor_scheduler))

    actor_scheduler.send('counter', 10)
    actor_scheduler.run()