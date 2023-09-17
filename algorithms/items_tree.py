class TreeStore():
    def __init__(self, items_list):
        self.items_list = items_list
    
    def getAll(self):
        return self.items_list

    def getItem(self, id):
        for item in self.items_list:
            if item["id"] == id:
                return item
            
        return None

    def getChildren(self, id):
        output = []
        for item in self.items_list:
            if item["parent"] == id:
                output.append(item)

        return output
             
    def getAllParents(self, id):
        output = []
        
        temp_id = id
    
        while True:
            for item in self.items_list:
                if item["id"] == temp_id:
                    output.append(item)
                    parent_id = item.get("parent")
                    temp_id = parent_id
                    if parent_id == 'root':
                        return output[1:]
                
                
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
print(ts.getAll())
print()
print(ts.getItem(7))
print()
print(ts.getChildren(4))
print()
print(ts.getChildren(5))
print()
print(ts.getAllParents(7))
