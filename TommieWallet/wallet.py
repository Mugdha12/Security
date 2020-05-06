#!/usr/bin/python

# dictionaries to strings using json
import json

# to send requests to server
import requests

# for command-line arguments
import sys 

# all the crypto stuff is here
import tommieutils as tu


######### YOUR CODE HERE ############

r=requests.get("http://127.0.0.1:8080/showchainraw")
d=json.loads(r.text)
chain=d['blocks']
f=open(sys.argv[1],"r")
s=sys.argv[1]
if s.find("keys/") > -1:
	s=s.replace("keys/","")
s=s.replace("pk.txt","")
print "Welcome, " + s.upper() + "."
pubKey=f.read()
outNumber=0
transid=0
f.close()



def setOutNumber(outNum):
    global outNumber
    outNumber=outNum

def setTransId(id):
    global transid
    transid=id

def emptyCreateTransaction():
    emptyCreateTrans = {
        'transtype' : '0',
        'outs' : [],
        'sigs' : []
    }
    return emptyCreateTrans

def emptyPayTransaction():
    emptyPayTrans = {
        'transtype' : '1',
        'ins' : [],
        'outs' : [],
        'sigs' : []
    }
    return emptyPayTrans

def emptyMineTransaction():
    emptyMinedTrans = {
        'prevmine' : '',
        'transtype' : '2',
        'outs': [],
        'nonce' : '',
        'timestamp':''
    }
    return emptyMinedTrans

def emptyBlock():
    emptyBlock = {
        'id':'',
        'prevhash':'',
        'timestamp':'',
        'transactions':{},
        'currhash':''
    }
    return emptyBlock

def checkAvail(id, outNum):
    used=[]
    for block in chain:
        currtrans=block['transactions']
        if(currtrans['transtype']=='1'):
            for x in currtrans['ins']:
                outNumResult = x['outnum'] == (outNum)
                idRes=str(x['transid']) == str(id)
                if( outNumResult & idRes):
                    return False
    return True
		
def countCoins():
	sum = 0
	blockChain=[]
	hold=tu.sha256(pubKey)
	for block in chain:
		transactions=block['transactions']
		outs=transactions['outs']
		outNum=0
		id=block['id']
		for rec in outs:
			if rec['recipient'] == hold:
				if(checkAvail(id,outNum)):
					sum=sum+rec['value']
					setOutNumber(outNum)
					setTransId(id)
			outNum =outNum+1
	
	return sum	
	
def payTransaction():
	if(s == "alice"):
		print "Who would you like to pay (Bob, Carlos, Dawn,Eve):"
	elif(s =="bob"):
		print "Who would you like to pay (Alice, Carlos, Dawn,Eve):" 
	elif(s =="carlos"):
		print "Who would you like to pay (Alice, Bob, Dawn,Eve):"
	elif(s =="dawn"):
		print "Who would you like to pay (Alice, Bob, Carlos,Eve):"
	elif(s == "eve"):
		print "Who would you like to pay (Alice, Bob, Carlos,Dawn):"
	else:
		print "Who would you like to pay (Alice, Bob, Carlos,Dawn,Eve):"

	userName=raw_input()
	print "How much would you like to pay:"
	amount=raw_input()
	
	availCoins=countCoins()
	payTrans=emptyPayTransaction()
	
	if availCoins < int(amount):
		print "This is transaction is  not possible because of insufficient coins"
	else:
		#payTrans['ins'].append(in)
		#print payTrans['ins']
		print "Transaction is possible"
		
coins=countCoins()
print "You currently have " + str(coins) + " tommie coins"
print "What would you like to do (pay,mine,quit:)"
transName = raw_input()
if(transName == "pay"):
    payTransaction()
