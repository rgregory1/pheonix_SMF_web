import pathlib
from smf_web import basedir
import json

def simplify_timestamp(timestamp):
    chars = '-:. '
    for c in chars:
        timestamp = timestamp.replace(c, '')
    timestamp = timestamp[:-6]
    return(timestamp)

def grab_from_temp(session_id, datatype):
    """grabs hero dict from json file in temp folder"""
    suffix = '.json'
    # with open(os.path.join(basedir, 'static','temp', timestamp, datatype + suffix)) as f:
    with open(pathlib.Path(basedir).joinpath('static', 'temp', session_id, datatype + suffix)) as f:
        hero_storage = json.load(f)
    return hero_storage
