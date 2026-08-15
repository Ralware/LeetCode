def containsNearbyDuplicate(Nums, K):

        Seen = {}

        for Index in range(len(Nums)):
            Value = Nums[Index]

            if Value in Seen:
                if Index - Seen[Value] <= K:
                    return True

            Seen[Value] = Index

        return False

                 



print(containsNearbyDuplicate([1,2,3,1],3))