from multiprocessing import Process
import time


def test(a):
    time.sleep(10)
    print('子进程')


def main():
    print('主进程开始')
    p = Process(target=test,args=(1,))
    p.start()
    time.sleep(15)
    print('主进程结束')


if __name__ == '__main__':
    main()