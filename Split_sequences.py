import random
import sys
class SplitSequences:
    def readFile(self, filename):
        f = open(filename, "r")
        data = f.read()
        lstSeq = data.split('>')
        del (lstSeq[0])
        for i in range(len(lstSeq)):
            strtmp = lstSeq[i];
            listtmp = strtmp.split("\n");
            del (listtmp[0])
            lstSeq[i] = "".join(listtmp)
        return lstSeq

    def SplitSequence(self, sequence, x, y):
        lst = []
        for seq in sequence:
            i, size = 0, len(seq)-1
            while True:
                rlength = random.randint(x, y)
                if i+rlength > size:
                    break
                nseq = seq[i:rlength+i]
                lst.append(nseq)
                i += rlength+1
        return lst
    def saveFasta(self,outfile,lst):
        file = open(outfile,'a+')
        i = 1
        for seq in lst:
            nseq = ">Fragment Number"+ str(i) +"\n" + seq + "\n"
            i += 1
            file.write(nseq)
        file.close()

if __name__ == "__main__":
    args = sys.argv
    lst = SplitSequences().readFile(args[1])
    lst = SplitSequences().SplitSequence(lst, int(args[2]), int(args[3]))
    SplitSequences().saveFasta(args[4], lst)

