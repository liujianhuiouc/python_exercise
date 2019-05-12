

import thread_pool

class Student():
    def run(self, *args, **kwargs):
        print(args)
        print('1234')


if __name__ == '__main__':
    student = Student()
    #student.run([student])
    pool = thread_pool.ThreadPool(3)
    requests = thread_pool.makeRequests(student.run, [[]])
    pool.putRequest(requests[0])
    pool.wait()