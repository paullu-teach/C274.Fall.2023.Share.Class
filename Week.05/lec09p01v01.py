def map_bucket(x):
    buckets = [0.2, 0.4, ___, ___, 1.0]
    for i in range(len(buckets)):
        if x < buckets[i]:
            return(i)
    return(-1)  # Error

if __name__ ==  "__main__":
    print(map_bucket(0.36))
    print(map_bucket(0.81))
    print(map_bucket(0.1))
