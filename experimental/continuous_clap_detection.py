#import multiprocessing
#import sys
#sys.path.append('/Users/diher/git/proyecto_primos/src')
#import detect_clap

from multiprocessing import Process, Queue, Pool, Pipe
from pipe_audio_input import record, test
import time

def receiveSoundData(parent_conn):
    print(parent_conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=record, args=(child_conn,))
    p2 = Process(target=receiveSoundData, args=(parent_conn,))
    p1.start()
    p2.start()
    print(parent_conn.recv())
    #print(receiveSoundData(child_conn))
    # q = Queue()
    # p = Process(target=receiveSoundData, args=(q,))
    # p.start()
    #     # prints "[42, None, 'hello']"

    # num_proc = 2
    # consumer_pool = Pool(num_proc)
    # results = []

    # for _ in range(num_proc):
    #     results.append(consumer_pool.apply_async(p, args= (receiveSoundData,)))
    # print(results)
    p2.join()
    p1.join()
# recorded_data = multiprocessing.Queue(100)

# def process(recorded_data):
#     while True:
#         data = recorded_data.get()
#         #clap = detect_clap.Clap(sys.argv[1])
#         #clap.detectClap()

# def record(recorded_data):
#     for data in input_stream:
#         recorded_data.put(data)

# producer = multiprocessing.Process(target=record, 
#                                    args=(recorded_data,))
# producer.start()


# num_proc = 2
# consumer_pool = multiprocessing.Pool(num_proc)
# results = []

# for _ in range(num_proc):
#     results.append(consumer_pool.apply_async(process, args= (recorded_data,)))

# producer.join()

# for result in results:
#     print(result)

# consumer_pool.terminate()