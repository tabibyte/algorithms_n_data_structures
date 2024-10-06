class dynamic_array:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity

    def add(self,value):
        if self.size == self.capacity:
            self.grow_size()
        self.array[self.size] = value
        self.size += 1

    def remove_index(self, index):
        if index < 0 or index >= self.size:
            return "Out of Bounds"
    
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
    
        self.array[self.size - 1] = None
        self.size -= 1


    def grow_size(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def get_index_value(self,index):
        if not isinstance(index, int):
            return "Not a Number"
        
        if index < 0 or index >= self.size:
            return "Out of Bounds"
        
        return self.array[index]
    
    def set_index_value(self, index, value):
        if not isinstance(index, int):
            return "Not a Number"

        if index < 0 or index >= self.size:
            return "Out of Bounds"

        self.array[index] = value

    def length(self):
        return self.size