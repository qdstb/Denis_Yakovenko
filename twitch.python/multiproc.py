import multiprocessing
import threading
import json
import copy
res = []



def test_output(num):
    for i in range(100):
        out = f"proc {num} says {i}"
        print(out)
        res.append(out)
        print(f"proc {num} says {i}")
    print(f"the end of proc {num}")
    print(res)


def generate_batch(lock, sample, size):
    for i in range(size):
        sample_copy= copy.deepcopy(sample)
        sample_copy["Name"] = f"{sample_copy['Name']} - {i+1}"

        with lock:
            with open("res.json", 'a') as f:
                f.write(f"{json.dumps(sample_copy)},")

# if __name__ == "__main__":

#     with open(""):

#     procs = []
    
#     for i in range(4):
#         p = multiprocessing.Process(target= test_output, args=(i+1,))
#         procs.append(p)
#         p.start()
#     for p in procs:
#         p.join()    
#     print("the end of the program")
#     print(res)