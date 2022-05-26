

class Cable: 
    start = ''
    end = ''

    def __init__(self, code, type, length) -> None:
        self.code = code
        self.type = type
        self.length = length 
        self.compute_start_and_end()


    def compute_start_and_end(self): 
        slivers = self.code.split('-')
        self.start = slivers[2]
        self.end = slivers[3]

class Splice: 

    def __init__(self, cable, fibers) -> None:
        self.cable = cable 
        self.fibers = fibers 


class Node: 

    def __init__(self, code) -> None:
        self.code = code
        self.slitter = ''
        self.next = []
        self.prev = []
        self.splices = [] 



if __name__ == '__main__': 

    import pandas as pd 
    import numpy as np 

    data = pd.read_csv('data.csv')
    cables = pd.read_excel('cables.xls')
    cables_arr = []

    #create cables
    for code in cables['code'].values:
        filter_df = cables[cables['code'] == code]
        len = filter_df['length'].values[0]
        print(len)
        cable = Cable(code=code,  type=filter_df['description'].values[0], length=len)
        cables_arr.append(cable)



    for cbl in cables_arr: 
        print(f'cable: {cbl.code} start: {cbl.start} end: {cbl.end} type: {cbl.type} len:{cbl.length}')

    #create nodes 
    #everything that isn't a cable should become a node
    candidate_nodes = data[data['element_type'] != 'cable']

    nodes = [] 
    sj = None
    #find the root node
    for node in candidate_nodes['code'].values: 
        if node[0] == 'S' and node[1] == 'J': 
            sj = Node(code=node)
            nodes.append(sj)



    #find the cables that go to in the sj
    for cable in cables_arr: 
        if cable.start == sj.code: 
            splice = Splice(cable=cable, fibers=[1,2])
            sj.next.append(splice.cable.end)
            sj.splices.append(splice)

    print(sj.code)
    print(sj.next)
    print(sj.prev)

    '''
    Encontramos de momento los identificadores de Next de cada SJ y empezamos a hacer la rama

    '''
    head = Node(code=sj.next[2])
    branch = []
    branches = []
    branch.append(head)

    def find_next(head, branch): 
        
        #find the cables that connect
        for cable in cables_arr: 
            if cable.start == head.code: 
                new_node = Node(cable.end)
                head.next.append(new_node.code)
                new_node.prev.append(cable.start)

                #compute slitter and splices for head we need the lenght of cable in case type is not an option 

                branch.append(new_node)
                find_next(new_node, branch)
    

    find_next(head=head, branch=branch)
    
    
    def print_node():

        for node in branch: 
            print(f'Node: {node.code}')
            print(f'Prev: {node.prev}')
            print(f'Next: {node.next}')

    right_arrow = '\U000027A1'
    down_arrow ='\U00002B07' 

    print_node()










    



    


