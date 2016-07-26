# Doubly Linked List
class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

#Query and Merge Functions:
def Qree(root):
    while root.prev:
        root = root.prev
    i = 1
    while root.next:
        root = root.next
        i += 1
    return i
    

def Merge(root_1, root_2):
    while root_1.next:
        root_1 = root_1.next
    while root_2.prev:
        root_2 = root_2.prev
    root_1.next = root_2
    root_2.prev = root_1
        
# Data Storage       
n_q = map(int, raw_input().strip().split(' '))
n = n_q[0]
q = n_q[1]

node_list = []
queries = []

for x in range(n):
    node_list.append(Node(x, None, None))
for x in range(q):
    queries.append(raw_input().strip().split(' '))

# Do the Queries and Merging    
for x in range(len(queries)):
    if queries[x][0] == 'Q':
        print Qree(node_list[int(queries[x][1]) - 1])

    else:
        Merge(node_list[int(queries[x][1]) - 1], node_list[int(queries[x][2]) - 1])
