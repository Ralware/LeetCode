def rotate(Arr, Index):
        
        for _ in range(Index):
            Arr.insert(0,Arr.pop())
        
        return Arr