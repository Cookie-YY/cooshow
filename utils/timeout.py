import signal
from functools import wraps


def timeout(seconds, error_message="timeout"):
    def decorator(func):
        def _handle_timeout(signum, frame):  # 调用时signal.signal会把接收到的信号(signum)，和当前进程栈状况(stack frame)传进来
            raise TimeoutError(error_message)

        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator
