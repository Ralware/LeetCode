def containsDuplicate(Nums):
        
        Seen = set()

        for Value in Nums:

            if not Value in Seen:
                Seen.add(Value)    
            else:
                return True

        return False