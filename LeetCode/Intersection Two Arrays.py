def intersection(Nums1, Nums2):
        
        Intersec = []
        Nums1 = set(Nums1)
        Nums2 = set(Nums2)

        for Value in Nums1:
            if Value in Nums2:
                Intersec.append(Value)

        return Intersec