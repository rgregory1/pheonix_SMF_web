def simplify_timestamp(timestamp):
    chars = '-:. '
    for c in chars:
        timestamp = timestamp.replace(c, '')
    timestamp = timestamp[:-4]
    return(timestamp)
