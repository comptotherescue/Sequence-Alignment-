import random
import sys

class Mutation:
    def genFirstSequence(self, num, A, C, G, T):
        sumTotal = A + C + G + T
        pA = A / sumTotal
        pC = pA + C / sumTotal
        pG = pC + G / sumTotal
        pT = pG + T / sumTotal
        strlst = []
        for i in range(num):
            strlst.append(self.get_ACGT(pA, pC, pG, pT))
        return strlst

    def get_ACGT(self, pA, pC, pG, pT):
        rnum = random.random()
        if rnum <= pA:
            return "A"
        elif rnum > pA and rnum <= pC:
            return "C"
        elif rnum > pC and rnum <= pG:
            return "G"
        elif rnum > pG and rnum <= pT:
            return "T"

    def get_newch(self, ch):
        resch = ch
        while resch == ch:
            rnum = random.random()
            if rnum <= 0.25:
                resch = "A"
            elif rnum > 0.25 and rnum <= 0.5:
                resch = "C"
            elif rnum > 0.5 and rnum <= 0.75:
                resch = "G"
            else:
                resch = "T"
        return resch

    def get_mutation(self, ch, pM):
        rnum = random.random()
        if rnum <= pM:
            coinflip = random.random()
            if coinflip <= 0.5:
                return self.get_newch(ch)
            else:
                return None
        return ch

    def get_sequences(self, strlst, pM):
        res = []
        for ch in strlst:
            nch = self.get_mutation(ch, pM)
            if nch:
                res.append(nch)
        return res

    def saveFastaFile(self, str, file, seqNum):
        tmp = ">Sequence number" + seqNum +"\n"
        outfile = open(file, "a+")
        i = 0
        for ch in str:
            if i > 80:
                i = 0
                tmp += "\n"
                outfile.write(tmp)
                tmp = ""
            tmp += ch
            i += 1
        tmp += "\n\n"
        outfile.write(tmp)
        outfile.close()
if __name__ == "__main__":
    args = sys.argv
    strlst = Mutation().genFirstSequence(int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
    n = int(args[6])
    Mutation().saveFastaFile("".join(strlst), args[8], "1")
    for i in range(n-1):
        Mutation().saveFastaFile("".join(Mutation().get_sequences(strlst, float(args[7]))), args[8], str(i+2))
