# A binary heap is a complete binary tree where each node satisfies the heap property.
# In a min-heap, for any given node, the value of the node is less than or equal to the values of its children.
# In a binary search tree, the left child is always less than the parent, and the right child is always greater.
# However, in a binary heap, there is no such relationship between sibling nodes.

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def heapify_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i //
                               2], self.heap_list[i] = (self.heap_list[i], self.heap_list[i // 2],)
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.heapify_up(self.current_size)

    def heapify_down(self, i):
        while (i * 2) <= self.current_size:
            me = self.min_child(i)
            if self.heap_list[i] > self.heap_list[me]:
                self.heap_list[i], self.heap_list[me] = (
                    self.heap_list[me], self.heap_list[i],)
            i = me

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.heapify_down(i)
            i = i - 1

    def delMin(self):
        if self.current_size == 0:
            return None
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        print(f"Delete Min: {min_val}")
        return min_val


if __name__ == "__main__":
    a = BinaryHeap()
    a.insert(5)
    a.insert(3)
    a.insert(4)
    a.insert(7)
    a.insert(2)
    a.insert(33)
    a.insert(15)
    a.insert(25)
    a.insert(37)
    print(a.heap_list)

    b = [3, 2, 8, 6, 7, 8, 9, 6]
    print("\n", b)

    c = BinaryHeap()
    c.build_heap(b)
    print(c.heap_list)

    c.delMin()
    print(c.heap_list)
