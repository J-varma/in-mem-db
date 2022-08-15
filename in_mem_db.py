# This is just a rough/draft script which satisfies the core logical requirements. 
# Can be improved by handling exceptions, adding types/readability to variables,...
ct=0
ns=set()
d=dict()
l=[{}]
txnl=[False]
while(1):
    cmd=input().split()
    if cmd[0]=="END" or cmd[0]=="end":
        break
    elif cmd[0]=="SET" or cmd[0]=="set":
        l[ct][cmd[1]]=int(cmd[2])
        #print(l[ct])
    elif cmd[0]=="GET" or cmd[0]=="get":
        print(l[ct][cmd[1]])
    elif cmd[0]=="UNSET" or cmd[0]=="unset":
        l[ct][cmd[1]]=None
    elif cmd[0]=="NAMEEQUALTO":
        pass  # implement later
    elif cmd[0]=="ADD":
        pass  # implement later
    elif cmd[0]=="BEGIN" or cmd[0]=="begin":
        txnl.append(True)
        new=l[ct].copy()
        ct+=1
        l.append(new)
    elif cmd[0]=="ROLLBACK" or cmd[0]=="rb":
        #print(ct,txnl[ct])
        if txnl[ct]==False:
            print("No Transaction")
        else:
            txnl.pop()
            l.pop()
            ct-=1
    elif cmd[0]=="COMMIT" or cmd[0]=="commit":
        if txnl[ct]==False:
            print("No Transaction")
        else:
            txnl=[False]
            temp=l[ct].copy()
            l=[{}]
            ct=0
            l[ct]=temp.copy()
    #print (l)
