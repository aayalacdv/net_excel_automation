class Cable: 
    start = ''
    end = ''

    def __init__(self, code, type) -> None:
        self.code = code
        self.type = type
        self.comput_start_and_end()


    def comput_start_and_end(self): 
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
        self.splices = [] 



if __name__ == '__main__': 

    import pandas as pd 
    import numpy as np 

    data = pd.read_csv('data.csv')
    cables = data[data['element_type'] == 'cable']
    cables_arr = []

    #create cables
    for code in cables['code'].values:
        filter_df = cables[cables['code'] == code]
        cable = Cable(code=code,  type=filter_df['description'].values[0])
        cables_arr.append(cable)



    # for cbl in cables_arr: 
    #     print(f'cable: {cbl.code} start: {cbl.start} end: {cbl.end} type: {cbl.type}')

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
            sj.splices.append(splice)

    print(sj.code)
    for splice in sj.splices:
        print(f'splice: {splice.cable.code}') 


    '''
    Hacemos un linked list por cada rama
    Hacemos las ramas de ramas mirando si hay ramas que tengan las ramas como starting point 
    '''


