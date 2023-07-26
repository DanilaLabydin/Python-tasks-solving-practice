reservoir_quantity = int(input())
volumes = list(map(int, input().split()))


def full_reservoirs_evenly(volumes_all_reservoirs):
    max_volume_to_full = volumes_all_reservoirs[0]

    for i in range(len(volumes_all_reservoirs)):
        if volumes_all_reservoirs[i] < max_volume_to_full:
            return -1
        max_volume_to_full = volumes_all_reservoirs[i]

    return max(volumes_all_reservoirs) - min(volumes_all_reservoirs)


answer = full_reservoirs_evenly(volumes)
print(answer)
