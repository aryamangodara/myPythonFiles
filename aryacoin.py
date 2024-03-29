"""@author: Aryaman Godara
I am trying to make a cryptocurrency
"""
import datetime
import hashlib
import json
from flask import Flask,jsonify,request
import requests
from uuid import uuid4
from urllib.parse import urlparse

#build a bockchain

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.transactions=[]
        self.create_block(proof=1,previous_hash='0')
        self.nodes=set()
    
    def create_block(self,proof,previous_hash):
        block={
            "index":len(self.chain)+1,
            'timestamp':str(datetime.datetime.now()),
            'proof':proof,
            'previous_hash':previous_hash,
            'transactions':self.transactions,
            }
        self.transactions=[]
        self.chain.append(block)
        return block
    def get_previous_block(self):
        return self.chain[-1]
    def proof_of_work(self,previous_proof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2-previous_proof**2).encode()).hexdigest()
            if(hash_operation[:4]=='0000'):
                check_proof=True
            else:
                new_proof += 1
        return new_proof
    def hash(self,block):
        encodedBlock=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    def add_transaction(self,sender,reciever,amount):
        self.transactions.append({'sender':sender,'reciever':reciever,'amount':amount})
        previous_block=self.get_previous_block()
        return previous_block['index']+1
    def add_node(self,address):
        parsedUrl=urlparse(address)
        self.nodes.add(parsedUrl.netloc)
    def replace_chain(self):
        network=self.nodes
        longestChain=None
        max_length=len(self.chain)
        for nodes in network:
            response = requests.get(f'http://{nodes}/get_chain')
            if(response.status_code==200):
                length=response.json()['length']
                chain = response.json()['chain']
                if(length>max_length and self.is_chain_valid(chain)):
                    max_length=length
                    longestChain=chain
        if(longestChain):
            self.chain=longestChain
            return True
        return False

#mine a block


#create a webapp
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#Creating an adress for the node on Port 5000
node_adreess = str(uuid4()).replace('-','')



#implement a blockchain
blockchain=Blockchain()

@app.route('/mine_block',methods = ['GET'])
def mine_block():
    previous_block=blockchain.get_previous_block()
    previous_proof=previous_block['proof']
    proof=blockchain.proof_of_work(previous_proof)
    previous_hash=blockchain.hash(previous_block)
    block=blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions':block['transactions'],
                }
    return jsonify(response), 200

#get the full chain
@app.route('/get_chain',methods = ['GET'])
def get_chain():
    response={
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
              }
    return jsonify(response) , 200
    
#validate the chain
@app.route('/validate_chain',methods = ['GET'])
def validate_chain():
    if (blockchain.is_chain_valid(blockchain.chain)):
        response={'message':'the chain is valid'}
    else:
        response={
        'message':'oh no ! there is a trouble , chain is not valid'
        }
    return jsonify(response),200

# Decentralisation of the currency

#Run the app
app.run(host='0.0.0.0',port=5000)






