class A:
    def executor(self, fn_name):
        print(getattr(self, fn_name))
        getattr(self, fn_name)()

    def do_something(self):
        print('done')

a = A()
a.executor('do_something')

exec("import os")
exec("os.system('python --version')")
