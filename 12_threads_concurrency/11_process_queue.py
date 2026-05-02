from multiprocessing import Process, Queue

def prepare_coffee(queue):
    queue.put("Espresso coffee is ready")



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_coffee, args=(queue,))
    p.start()
    p.join()
    print(queue.get())