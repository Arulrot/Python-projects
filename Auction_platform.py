emptdict={}
def higgestbid():
    winner=''
    hieghestbid=0
    for bidder in emptdict:
        bidamount=emptdict[bidder]
        if bidamount>hieghestbid:
            hieghestbid=bidamount
            winner=bidder
    print(f'\nThe winner is {winner} with the bid amount of {hieghestbid}')
            

while True:   
   
    name=input("\nEnter your name:")
    value=int(input("\nEnter amount:"))
    emptdict[name]=value
    opt=input("\nAny other bids 'yes' or 'no':").lower()
    if opt=='yes':
        continue;
    elif opt=='no':
        higgestbid()
        break;
    else :
        print("\nWrong input")
        break;
        
