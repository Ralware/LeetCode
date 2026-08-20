def topKFrequent(Nums,Tops):
    Seen = {}
    
    for No in Nums:
        if not No in Seen:
            Seen[No] = 0

        if No in Seen:
            Seen[No] +=1
    
    Pairs = list(Seen.items())

# Still Need To Analyze This Part More ! 

    Pairs.sort(key=lambda x: x[1], reverse=True)

    TopK = Pairs[:Tops]

    return [x[0] for x in TopK]
    
