# !/usr/bin/env python
# -*- coding:utf-8 -*-



import time
import types
import threading
from Queue import Queue


class ForkJoinPool(object):
    def __init__(self, worker_size=1):
        self._queue = Queue()
        self._worker_size = worker_size
        self.create_worker()

    def create_worker(self):
        for i in range(self._worker_size):
            ForkJoinThread(self._queue).start()

    def put(self, task, msg):
        assert isinstance(task, ForkJoinTask)
        self._queue.put((task, msg))


class ForkJoinThread(threading.Thread):
    def __init__(self, queue):
        super(ForkJoinThread, self).__init__()
        self._queue = queue
        self.name = 'forkjoin_thread'
        self.daemon = True

    def push(self, task, msg):
        self._queue.put((task, msg))

    def run(self):
        while 1:
            try:
                task, msg = self._queue.get()
                assert isinstance(task, ForkJoinTask)

                if not task.can_be_run():
                    self._queue.put((task, msg))
                    continue

                #print('task dispatch message %s' % (msg))
                task.do_execute(msg)
                task.set_sub_tasks_can_run()
            except StopIteration:
                pass
            except Exception as e:
                print('error')
                print(e)


class ForkJoinTask(object):

    def __init__(self, parent_task=None):
        self._parent_task = parent_task
        self._sub_tasks_can_ben_run_state = False
        self._sub_tasks = []
        self._event = threading.Event()
        self._status = 0
        self._result = None
        self._coroutine = None
        self._lock = None
        self._elapse = 0


    def elapse(self):
        return self._elapse

    def is_done(self):
        return self._status > 0

    def get(self):
        self._event.wait()
        return self.get_raw_result()

    def do_execute(self, msg=None):
        self._elapse = time.time()

        if self._coroutine is not None:
            with self._lock:
                self._coroutine.send(msg)
            #self._coroutine.send(msg)
            return

        result = self.execute()
        if isinstance(result, types.GeneratorType):
            assert self._coroutine is None
            self._coroutine = result
            self._lock = threading.RLock()
            next(result)

        else:
            self.set_raw_result(result)

    def ready(self):
        return self._sub_task_all_done()

    def execute(self):
        pass

    def get_raw_result(self):
        return self._result

    def set_raw_result(self, result):
        self._result = result
        self._set_completion(1)

    def can_be_run(self):
        if self._parent_task is None:
            return True

        return self._parent_task._sub_task_can_be_run()

    def set_sub_tasks_can_run(self):
        self._sub_tasks_can_ben_run_state = True

    def _sub_task_can_be_run(self):
        return self._sub_tasks_can_ben_run_state

    def _sub_task_all_done(self):
        for task in self._sub_tasks:
            if not task.is_done():
                return False

        return True

    def get_sub_task_results(self):
        results = []

        for task in self._sub_tasks:
            results.append(task.get())

        return results

    def _append_sub_task(self, task):
        assert isinstance(task, ForkJoinTask)
        self._sub_tasks.append(task)

    def join(self):
        self._event.wait()

    def _set_completion(self, status):
        self._status = status
        self._elapse = time.time() - self._elapse
        self._notify()

    def _notify(self):
        self._event.set()

        if self._parent_task is not None:
            thread = threading.current_thread()
            assert isinstance(thread, ForkJoinThread)
            thread.push(self._parent_task, self.get_raw_result())


    def fork(self):
        thread = threading.current_thread()
        assert isinstance(thread, ForkJoinThread)

        if self._parent_task is not None:
            self._parent_task._append_sub_task(self)

        thread.push(self, None)



class SumTask(ForkJoinTask):
    def __init__(self, start, end, parent_task=None, throttle=5):
        super(SumTask, self).__init__(parent_task)
        self._start = start
        self._end = end
        self._throttle = throttle

    def execute(self):
        #print("start %s, end %s" % (self._start, self._end))

        if self._end - self._start <= self._throttle:
            result = self._end - self._start
            self.set_raw_result(result)
            return

        median = (self._end + self._start) / 2
        left = SumTask(self._start, median, self, self._throttle)
        right = SumTask(median, self._end, self, self._throttle)
        left.fork()
        right.fork()

        while not self.ready():
            yield

        results = self.get_sub_task_results()

        sum_n = reduce(lambda x, y: x+y, results, 0)
        self.set_raw_result(sum_n)


class DirectSumTask(ForkJoinTask):
    def __init__(self, start, end, throttle=5):
        super(DirectSumTask, self).__init__()
        self._start = start
        self._end = end
        self.throttle = throttle

    def execute(self):
        return self._end - self._start


class RecursiveTask(ForkJoinTask):
    def __init__(self, parent_task=None):
        super(RecursiveTask, self).__init__(parent_task)

    def execute(self):
        pass

    def compute(self):
        pass


class CountTask(object):

    def __init__(self, start, end, scheduler, parent_task=None, threshold=5):
        super(CountTask, self).__init__()
        self._start = start
        self._end = end
        self._scheduler = scheduler
        self._parent_task = parent_task
        self._threshold = threshold
        self._inner_coroutine = self.compute()
        self._sub_tasks = []
        self._event = threading.Event()
        self._handle_state = 0
        self._result = None

    def start(self):
        self._scheduler.push(self._inner_coroutine, None)

    def coroutine(self):
        return self._inner_coroutine

    def compute(self):
        print('before compute')

        if self._end - self._start <= self._threshold:
            self._set_result(self._end - self._start)
            return

        try:
            while not self.ready():
                try:
                    print('before yield')
                    yield
                finally:
                    print('finally')
                    self._handle_subtasks()
        finally:
            print('outer fin')

        self._sum()

    def ready(self):
        if self._handle_state == 0:
            return False

        for task in self._sub_tasks:
            if not task.has_result():
                return False

        return True

    def _sum(self):
        sum_numeric = 0
        for task in self._sub_tasks:
            sum_numeric += task.result()

        self._set_result(sum_numeric)

    def _generate_tasks(self):
        median = (self._end + self._start) / 2
        left_count_task = CountTask(self._start, median, self._scheduler,
                                    self._inner_coroutine, self._threshold)
        right_count_task = CountTask(median, self._end, self._scheduler,
                                     self._inner_coroutine, self._threshold)
        return [left_count_task, right_count_task]


    def _handle_subtasks(self):
        if self._handle_state == 1:
            return

        self._sub_tasks.extend(self._generate_tasks())

        for task in self._sub_tasks:
            self._scheduler.push(task.coroutine(), None)

        self._handle_state = 1

    def _set_result(self, result):
        self._result = result
        self._notify()

    def _notify(self):
        if self._parent_task is not None:
            self._scheduler.push(self._parent_task, self._result)

        self._event.set()

    def has_result(self):
        return self._result is not None

    def result(self):
        self._event.wait()
        return self._result

    def __repr__(self):
        "(%s, %s)" % (self._start, self._end)



if __name__ == '__main__':
    forkjoinpool = ForkJoinPool(3)

    num = 100000000
    direct_sum_task = DirectSumTask(0, num)
    forkjoinpool.put(direct_sum_task, None)
    print('direct sum task', direct_sum_task.get())

    sum_task = SumTask(0, num, throttle=500000)
    forkjoinpool.put(sum_task, None)
    print('sum task result', sum_task.get())

    print(sum_task.elapse())


    event = threading.Event()
    event.wait()


