import re

def default(value, _default):
    return value if value is not None else _default

def _partition_str(text: str, substring: str):
    elem = text
    l = len(substring)
    while True:
        i = elem.find(substring)
        if i == -1:
            break
        yield elem[:i]
        yield elem[i:i+l]
        elem = elem[i+l:]
    yield elem

def partition_re(text, pattern):
    acc = []
    i = 0
    for match in re.finditer(pattern, text):
        acc.append(text[i:match.start()])
        acc.append(match[0])
        i = match.end()    
    if i < len(text):
        acc.append(text[i:])
    return acc

def partition(text, pattern):
    if isinstance(pattern, str):
        return _partition_str(text, pattern)
    if isinstance(pattern, re.Pattern):
        return partition_re(text, pattern)

def map_partition(f, partitioned_data):
    acc = []
    for i, x in enumerate(partitioned_data):
        if i % 2 == 0:
            acc.append(x)
        else:
            acc.append(f(x))
    return acc

def patternize(pattern: str):
    if (not isinstance(pattern, re.Pattern)
        and pattern.startswith("/")
        and pattern.endswith("/")):
        return re.compile(pattern[1:-1])
    return pattern

