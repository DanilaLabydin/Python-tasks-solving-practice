import multiprocessing as mp


def washer(dishes_d, output):
    for dish in dishes_d:
        print("Washing", dish, "dish")
        output.put(dish)


def dryer(input_d):
    while True:
        dish = input_d.get()
        print("Drying", dish, "dish")
        input_d.task_done()


dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ["salad", "bread", "entree", "desert"]
washer(dishes, dish_queue)
dish_queue.join()
