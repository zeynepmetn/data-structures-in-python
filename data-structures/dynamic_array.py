import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0 # eleman sayisi
        self.capacity = 1 # kapasite
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds !")
        
        return self.A[k]
    
    def append(self, eleman):
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = eleman
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]
      
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """yeni array dondurur"""
        return (new_cap*ctypes.py_object)()
    

arr = DynamicArray()
arr.append(1)
print("ilk eleman eklendi: ", arr[0])

arr.append(3)
print("2.eleman eklendi: ", arr[1])

print(arr[0], arr[1])