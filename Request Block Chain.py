import requests as req
import random
import time

random.seed(4321)

# get latest block info from blockchain.info
latest = "https://blockchain.info/ko/latestblock"
resp = req.get(latest)

# get json from request
block_json = resp.json()
curr_block_hash = block_json[u'hash']

# set the url for single block api
block_url = "https://blockchain.info/ko/rawblock/"

count = 0
max_count = 10
while count < max_count:

    # set random from 0.5~1 sec
    sec = 0.5 * (random.random() + 1)

    # delay time for random sec.
    time.sleep(sec)

    # set curr_url by concatenating block_url + block_hash
    curr_url = block_url + curr_block_hash

    # request curr_url
    resp = req.request(method='GET', url = curr_url)

    # get json from resp
    block_json = resp.json()

    # print hash from single block
    print block_json[u'hash'], sec, time.strftime('%X %x %Z')

    # get previous block from block info
    curr_block_hash = block_json[u'prev_block']

    count += 1

