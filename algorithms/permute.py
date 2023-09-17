import time
import itertools


def make_permutes(iterable):
    with open("output.txt", "w") as f:
        for num in itertools.permutations(iterable):
            try:
                s = "".join([str(i) for i in num])
                print(s)
            except Exception as e:
                print(f"Error occured when you tried to get a permute: {e} ")
                return
            
            try:
                f.write(s + "\n")
            except Exception as e:
                print(f"Error occured when you tried to store a permute in the file: {e}")
                return
            

n = int(input())
nums = [0 for _ in range(n)] + [i for i in range(1, n + 1)]
start = time.time()
make_permutes(nums)
print(time.time() - start)

with open(r"output.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
