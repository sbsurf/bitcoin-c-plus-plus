from bitcoin.rpc import RawProxy

p = RawProxy()

# Alice's transaction ID
txid = "7600deebcd15ee4ade18b0c2def96db0b80d1115a164cba68c2e47f9daa412b4"

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx) 

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
  print(output['scriptPubKey']['addresses'], output['value'])
