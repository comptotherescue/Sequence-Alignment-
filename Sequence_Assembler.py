import sys

class SequenceAssembler:
    def readFile(self, filename):
        f = open(filename, "r")
        data = f.read()
        lstSeq = data.split('>')
        del (lstSeq[0])
        for i in range(len(lstSeq)):
            strtmp = lstSeq[i];
            listtmp = strtmp.split("\n");
            del (listtmp[0])
            tmpstr = "".join(listtmp)
            lstSeq[i] = tmpstr
        return lstSeq

    def computeMaxScore(self, seqlst, maxVal, maxSeq, m, s, d, hmap):
        if len(seqlst) == 1:
            return maxVal, maxSeq
        lMaxval, lMaxSeq = -sys.maxsize-1, ""
        maxi, maxj = 0, 0
        for i in range(len(seqlst)-1):
            for j in range(i+1, len(seqlst)):
                if (seqlst[i], seqlst[j]) not in hmap:
                    val, seq = self.dpCalculation(seqlst[i], seqlst[j],m, s, d)
                    hmap[(seqlst[i], seqlst[j])] = (val, seq)
                else:
                    val , seq = hmap[(seqlst[i], seqlst[j])][0], hmap[(seqlst[i], seqlst[j])][1]
                if lMaxval < val:
                    lMaxSeq = seq
                    lMaxval = val
                    maxi = i
                    maxj = j
        if lMaxval < 0:
            return maxVal, maxSeq
        tmpi = seqlst[maxi]
        tmpj = seqlst[maxj]
        del seqlst[seqlst.index(tmpi)]
        del seqlst[seqlst.index(tmpj)]
        del hmap[(tmpi,tmpj)]
        seqlst.append(maxSeq)
        if maxVal < lMaxval:
            return self.computeMaxScore(seqlst, lMaxval, lMaxSeq, m, s, d, hmap)
        return self.computeMaxScore(seqlst, maxVal, maxSeq, m, s, d, hmap)

    def dpCalculation(self, fi, fj, m, s, d):
        lfi = len(fi)
        lfj = len(fj)
        table = [[0 for x in range(lfj+1)] for y in range(lfi+1)]
        ptr = [[0 for x in range(lfj + 1)] for y in range(lfi + 1)]
        maxi, maxj = -1, -1
        for i in range(1, lfi+1):
            for j in range(1, lfj+1):
                fij = []
                if fi[i-1] == fj[j-1]:
                    fij.append(table[i-1][j-1] + m)
                else:
                    fij.append(table[i-1][j-1] + s)
                fij.append((table[i-1][j]) + d)
                fij.append((table[i][j-1]) + d)
                element = max(fij)
                table[i][j] = element
                ptr[i][j] = fij.index(element)+1
                if table[maxi][maxj] < element:
                    maxi = i
                    maxj = j
        return table[maxi][maxj] , self.getSeq(fi, fj, ptr, maxi, maxj)

    def getSeq(self, seqi, seqj, ptr, maxi, maxj):
        res = seqj[maxj:]
        while(ptr[maxi][maxj] != 0):
            if ptr[maxi][maxj] == 1:

                res = seqi[maxi-1] + res
                maxi -= 1
                maxj -= 1
            elif ptr[maxi][maxj] == 2:
                res = seqi[maxi-1] + res
                maxi -= 1
            elif ptr[maxi][maxj] == 3:
                res = seqj[maxj-1] + res
                maxj -= 1
        res = seqi[0:maxi] + res
        return res
if __name__ == "__main__":
    args = sys.argv
    hmap = dict()
    lst = SequenceAssembler().readFile(args[1])
    outfile = open(args[5], "w+")
    Score, Seq = SequenceAssembler().computeMaxScore(lst, 0, "",  int(args[2]), int(args[3]), int(args[4]), hmap)
    tmp = "Score: "+ str(Score) + "Sequence: " + Seq
    outfile.write(tmp)
    outfile.close()