import multiprocessing
import sys
sys.path.append('/Users/diher/git/proyecto_primos/src')
import detect_clap

recorded_data = multiprocessing.Queue(100)

def find_claps(recorded_data):
    while True:
        data = recorded_data.get()
        clap = detect_clap.Clap(data)
        clap.detectClap()

def reord(recorded_data):
    for data in input_stream:
        recorded_data.put(data)
        
producer = multiprocessing.Process(target=record, 
                                   args=(recorded_data,))
producer.start()


num_proc = 2
consumer_pool = multiprocessing.Pool(num_proc)
results = []

for _ in range(num_proc):
    results.append(consumer_pool.apply_async(process, args= (recorded_data,)))

producer.join()

for result in results:
    print(result)

consumer_pool.terminate()