def Solutions():
    All_Solutions = []
    for S in range(9,-1,-1):
        for E in range(9,-1,-1):
            for N in range(9,-1,-1):
                for D in range(9,-1,-1):
                    for M in range(9,0,-1):
                        for O in range(9,-1,-1):
                            for R in range(9,-1,-1):
                                for Y in range(9,-1,-1):
                                    if len(set([S,E,N,D,M,O,R,Y])) == 8:
                                        SEND = 1000 * S + 100 * E + 10 * N + D
                                        MORE = 1000 * M + 100 * O + 10 * R + E
                                        MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y
                                        if SEND + MORE == MONEY:
                                            All_Solutions.extend((SEND,MORE,MONEY))
    return All_Solutions

if __name__ == "__main__":
    print("Bài toán:\n")
    print("{:>5}\n{:<5}\n{:>5}\n{:<5}\n{:>5}".format("SEND",'+',"MORE","=","MONEY"))
    SMM = Solutions()
    print("\nĐáp án:\n")
    print("{:>5}\n{:<5}\n{:>5}\n{:<5}\n{:>5}".format(SMM[0],'+',SMM[1],"=",SMM[2]))