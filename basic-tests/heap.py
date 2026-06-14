class MinHeap(object):
    def __init__(self, key, data):
        self._list = [HeapNode(key, data)]
    
    def __str__(self):
        ret_list = []
        for i in self._list:
            ret_list.append("key: "+str(i.key)+" value: "+i.data+"\n")
        return "".join(ret_list)

    def add_item(self, key, data):
        new_item = HeapNode(key, data)
        self._list.append(new_item)
        son = len(self._list)-1
        parent = self.prev(len(self._list)-1)
        print(self)
        while parent >= 0 and self._list[son].key < self._list[parent].key:
            self._list[son], self._list[parent] = self._list[parent], self._list[son]
            son = parent
            parent = self.prev(parent)
            print(self)
    
    def prev(self, index):
        return (index-1)//2


class HeapNode(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
    
    def __str__(self):
        return f"key: {self.key} data: {self.data}"

if __name__ == "__main__":
    print("--- Teste 1: Inserção Decrescente (Garante ordenação do topo) ---")
    heap = MinHeap(10, "Pedido 10")
    heap.add_item(5, "Pedido 5")
    heap.add_item(2, "Pedido 2")
    heap.add_item(0, "Pedido 0") # Este deve virar o novo topo
    
    print(heap)
    # O topo esperado aqui deve ser (0, "Pedido 0")