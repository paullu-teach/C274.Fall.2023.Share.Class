def map_bucket(x):
    buckets = [___, ___]
    for i in range(len(buckets)):
        if x < buckets[i]:
            return(i)
    return(-1)  # Error

if __name__ ==  "__main__":
    print(map_bucket(0.36))
    print(map_bucket(0.81))
    print(map_bucket(0.1))
