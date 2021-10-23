from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mineBlock():
    previousBlock = blockchain.printPreviousBlock()
    previousProof = previousBlock['proof']
    previousHash = blockchain.hash(previousBlock)
    proof = blockchain.proofOfWork(previousProof)
    block = blockchain.createBlock(proof, previousHash)

    response = {
        'message': 'Nuevo bloque minado',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previousHash': block['previousHash']
    }

    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def displayChain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

@app.route('/valid', methods = ['GET'])
def valid():
    valid = blockchain.chainValid()

    if valid:
        response = {'message': 'Blockchain funcionando :)'}
    else:
        response =  {'message': 'Blockchain inservible :('}
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 66700)