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

    def __init__(self, code, fibers) -> None:
        self.code = code
        self.fibers = fibers 

class Node: 

    def __init__(self, code, splices, slitter) -> None:
        self.code = code
        self.slitter = slitter
        self.splices = splices



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

    #create nodes 
    for cbl in cables_arr: 
        print(f'cable: {cbl.code} start: {cbl.start} end: {cbl.end} type: {cbl.type}')


    #sort nodes and puhs them to array 


