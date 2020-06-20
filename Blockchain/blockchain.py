# Libraries
import datetime
import json
from flask import Flask, jsonify
import hashlib

# Building blockchain
class blockchain:

	def __int__(self):
		self.chain = []
		self.create_block(proof = 1, previous_hash = "0")   # Genesis Block

	def create_block(self, proof, previous_hash):
		block = { "index" : len(self.chain) + 1,
                   "timestamp" : str(datetime.datetime.now()),
                   "proof" : proof,
                   "previous_hash" : previous_hash
             	}                                         # data will be added at second module
        self.chain.append(block)
        return block
    
  def get_previous_block(self):
      self.chain[-1]    

  def proof_of_work(self, previous_proof):
    	new_proof = 1
    	check_proof = False
    	while check_proof is False:
    		hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()   
        # we want asymmetrical and complex str in sah256
        # encode modul gives byte datatype
        # hexdigest returns hexddeciaml characters

        if hash_operation[:4] == '0000':
          check_proof = True
        else:
          check_proof = False
          new_proof += 1
      return new_proof  

  def hash(self, block):
      encoded_block = json.dumps(block, sort_keys=True).encode()
      return hashlib.sha256(encoded_block).hexdigest()

  def is_chain_valid(self, chain):
      
# Mining block  
    






