import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds")
        
        return self.A[k]

    def append(self, eleman):
        if self.n == self.capacity:
            self._resize(self.capacity*2)
        
        self.A[self.n] = eleman
        self.n += 1


    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_cap

    def display_array(self):
        if self.n >= 1:
            for i in range(self.n):
                print("dizi elemanlari: ", self.A[i])
        else:
            print("dizi bos")

    def eleman_sayisi(self):
        print("eleman sayisi: ", self.n)
   
    def kapasite(self):
        print("kapasite: ", self.capacity)

arr = DynamicArray()
arr.append(1)
arr.display_array()
arr.eleman_sayisi()
arr.kapasite()
print()
arr.append(2)
arr.display_array()
arr.eleman_sayisi()
arr.kapasite()
print()
arr.append(3)
arr.display_array()
arr.eleman_sayisi()
arr.kapasite()
print()
arr.append(4)
arr.display_array()
arr.eleman_sayisi()
arr.kapasite()
print()
arr.append(5)
arr.display_array()
arr.eleman_sayisi()
arr.kapasite()

