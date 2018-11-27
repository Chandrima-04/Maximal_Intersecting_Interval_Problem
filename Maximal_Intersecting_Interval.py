from heapq import heappush, heappop, heapify
class Maximal_intersection:
    def __init__(self, flist):
        self.flist = flist
        
    def heap_push(self,hlist,element):
        heappush(hlist,element)
        return (hlist)

    def heap_pop(self,hlist):
        heappop(hlist)
        return hlist
    
    def intervals(self):
        L = sorted(self.flist)
        i,j = 0, len(L)
        newIns = False
        heap2 = [] 
        half = int(j/2)
        interval_no = []
        while i<j:
            index_val = self.flist.index(L[i])
            if(index_val < half):
                newIns = True
                self.heap_push(heap2,L[i])
                interval_no.append(index_val+1)
            elif (index_val >= half):
                if (newIns == True):
                    print (interval_no)
                newIns = False
                interval_no.remove(index_val-half+1)
                self.heap_pop(heap2)            
            i = i+1
            
"Driver code"
left_list = []
right_list = []
interval = int(input ("Enter number of intervals"))
while interval>0:
    a,b = input ("Enter interval value ").split(' ')
    a,b = int(a), int(b)
    if a == 0 and b==0:
        break   
    left_list.append(a)
    right_list.append(b)
    interval -=1
        
final_list = left_list + right_list
I = Maximal_intersection(final_list)
I.intervals()
