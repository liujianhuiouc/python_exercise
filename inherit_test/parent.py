


class Parent(object):

    def __init__(self, name, score, **kwargs):
        # print('parent')
        print(name)
        print(score)
        print(kwargs)


    def say_something(self):
        print(self.generate())

    def generate(self):
        return "parent"

    def say_bye(self):
        print("bye")



class Child(Parent):

    def __init__(self, aaa, **kwargs):
        print(aaa)
        print(kwargs)
        super(Child, self).__init__(**kwargs)

    def generate(self):
        self.say_bye()
        return "child"

class Wrapper(object):

    def __init__(self, class_impl_class):
        self.class_impl_class = class_impl_class

    def print_hello(self):

        self.class_impl_class().say_something()



if __name__ == "__main__":
    child = Child(score=10, name="liujianhui", a='a', b='b', aaa='aaa')