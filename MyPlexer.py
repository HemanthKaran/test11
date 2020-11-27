class MyPlexer:
    class MyDecorator:
        def __init__(self):
            self.registery = []

        def __call__(self, m, **kwargs):
            print(self)
            self.registery.append(m)

            def w(my_arg):
                print("invoke the methods in registery based on input paramter")

            return w

    def __init__(self):
        self.route = self.MyDecorator()

    def run(self):
        print("arguments ", )
        for m in self.route.registery:
            ip = input()
            if ip == 'hello':
                print("Hello, World!")
            elif ip == 'bye':
                print("bye")

        # get the commandline arguments here and
        # parse based on the arguments invoke function in
        # registry
