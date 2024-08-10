emptdict={}
def higgestbid():
    highestbidder=''
    hieghestbid=0
    for bidder in empdict:
        bidamount=empdict[bidder]
        if bidamount>hieghestbid:
            

while True:   
   
    name=input("enter your name:")
    value=int(input("enter amount:"))
    emptdict[name]=value
    opt=input("Any other bids 'yes' or 'no':").lower()
    if opt=='yes':
        continue;
    else :
        break;
        
print(emptdict)