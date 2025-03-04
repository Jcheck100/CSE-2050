def _trib(k, cache=None):
    if cache is None:
        cache = {1: 0, 2: 0, 3: 1}
    if k not in cache:
        cache[k] = _trib(k-1, cache) + _trib(k-2, cache) + _trib(k-3, cache)
    return cache[k]

def trib(k):
    return _trib(k, {1: 0, 2: 0, 3: 1})