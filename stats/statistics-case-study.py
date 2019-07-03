import matplotlib.pyplot as plt 
'''
    Consider the following money transfer amounts and corresponding charges by 3 vendors
'''
transaction_amount = [200, 340, 430, 650, 920]
charges_vendor1 = [11, 17, 29, 33, 44]
charges_vendor2 = [16, 18, 27, 30, 43]
charges_vendor3 = [13, 15, 30, 31, 39]

#Plot a graph (GUI)
plt.plot(charges_vendor1, transaction_amount)
plt.plot(charges_vendor2, transaction_amount)
plt.plot(charges_vendor3, transaction_amount)
plt.xlabel("amount") 
plt.ylabel("charge")  
plt.title("Transactions")  
plt.show()



''' 
Raw Bar Graph

    |XXXXXXXXXXX
200 |YYYYYYYYYYYYYYYY
    |ZZZZZZZZZZZZZ

    |XXXXXXXXXXXXXXXXX
340 |YYYYYYYYYYYYYYYYYY
    |ZZZZZZZZZZZZZZZ

    |XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
430 |YYYYYYYYYYYYYYYYYYYYYYYYYYY
    |ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

    |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
650 |YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    |ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

    |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
920 |YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    |ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
'''
i = 0
for k in transaction_amount:
    res = str(k)
    v1 = "X" * charges_vendor1[i]
    v2 = "Y" * charges_vendor2[i]
    v3 = "Z" * charges_vendor3[i]
    print("    |" + v1)
    print(res + " |" + v2)
    print("    |" + v3)
    print("")
    i = i + 1