import time
'''
def foo():
    print('print from foo')
    with open('log.txt', 'a') as f:
        local_time = time.asctime(time.localtime(time.time()))
        log_msg = 'foo [local time] {}'.format(local_time)
        f.write(log_msg+'\n')

def bar():
    print('print from bar')
    with open('log.txt', 'a') as f:
        local_time = time.asctime(time.localtime(time.time()))
        log_msg = 'bar [local time] {}'.format(local_time)
        f.write(log_msg+'\n')

foo()
bar()
'''
######################################################
'''
def log(func):
    with open('log.txt', 'a') as f:
        local_time = time.asctime(time.localtime(time.time()))
        log_msg = '{} [local time] {}'.format(func, local_time)
        print(log_msg)
        f.write(log_msg+'\n')

def foo():
    print('print from foo')

def bar():
    print('print from bar')

log(foo)
log(bar)
'''
######################################################
'''
def log(func):
    def wrapper():
        with open('log.txt', 'a') as f:
            local_time = time.asctime(time.localtime(time.time()))
            log_msg = '{} [local time] {}'.format(func, local_time)
            print(log_msg)
            f.write(log_msg+'\n')

        return func
    return wrapper

def foo():
    print('print from foo')

foo = log(foo)
foo()
foo()
foo()
'''
######################################################
'''
def log(func):
    def wrapper():
        with open('log.txt', 'a') as f:
            local_time = time.asctime(time.localtime(time.time()))
            log_msg = '{} [local time] {}'.format(func, local_time)
            print(log_msg)
            f.write(log_msg+'\n')

        return func
    return wrapper

@log
def foo():
    print('print from foo')

foo()
foo()
foo()
'''
######################################################
'''
def log(func):
    def wrapper(*args):
        with open('log.txt', 'a') as f:
            local_time = time.asctime(time.localtime(time.time()))
            log_msg = '{} [local time] {}, parameter: {}'.format(func, local_time,  ', '.join(args))
            print(log_msg)
            f.write(log_msg+'\n')

        return func(*args)
    return wrapper

@log
def foo(par):
    print('print from foo, parameter: ' + par)

@log
def bar(par1, par2):
    print('print from bar, parameter: {}, {}'.format(par1, par2))

foo('hello')
bar('hello', 'decorator')
'''
######################################################
'''
def log(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            local_time = time.asctime(time.localtime(time.time()))
            log_msg = '{} [local time] {}, parameter: {}'.format(func, local_time,  ', '.join(args))
            log_msg += '\nkeyword parameter: {}\n'.format(kwargs)
            print(log_msg)
            f.write(log_msg+'\n')

        return func(*args, **kwargs)
    return wrapper

@log
def foo(par):
    print('print from foo, parameter: ' + par)

@log
def bar(par1='par1', par2='par2'):
    print('print from bar, parameter: {}, {}'.format(par1, par2))

foo('hello')
bar(par1='hello', par2='decorator')
'''
######################################################

class log():
    def __init__(self, func):
        self.func = func

    def wrapper(self, *args, **kwargs):
        with open('log.txt', 'a') as f:
            local_time = time.asctime(time.localtime(time.time()))
            log_msg = '{} [local time] {}, parameter: {}'.format(self.func, local_time,  ', '.join(args))
            log_msg += '\nkeyword parameter: {}\n'.format(kwargs)
            print(log_msg)
            f.write(log_msg+'\n')

        return self.func(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.wrapper(*args, **kwargs)

@log
def foo(par):
    print('print from foo, parameter: ' + par)

@log
def bar(par1='par1', par2='par2'):
    print('print from bar, parameter: {}, {}'.format(par1, par2))

foo('hello')
bar(par1='hello', par2='decorator')