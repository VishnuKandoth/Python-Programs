from collections import OrderedDict
n=input("Enter no. of Strings :")
#print n
li=[]
for j in range(1,n+1) :
        li.append(raw_input("Enter String : ").lower())
#print li
#st="bbaccc".lower()
for st in li :
            dic = {}
            for i in set(st):
                b = st.count(i, 0, len(st))
                dic[i] = b
            #print dic

            od ="".join(OrderedDict.fromkeys(st).keys())
            #print(od)
            #print len(od)
            c=0

            for i in od :
                #print "ascii of ",i," is ",ord(i)-96,"count : ",dic[i]
                if (ord(i)-96)==dic[i] :
                        c +=1
            if c==len(od) :
                print st,"Yes"
            else :
                print st,"No"