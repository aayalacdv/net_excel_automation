
from operator import length_hint


class Conection:

    def __init__(self, node, conn_type) -> None:
        self.conn_type = conn_type
        self.node = node


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
        self.slitter = None
        self.next = []
        self.prev = []
        self.splices = []


if __name__ == '__main__':

    import pandas as pd

    data = pd.read_csv('data.csv')
    cables = pd.read_excel('cables.xls')
    cables_arr = []

    # create cables
    for code in cables['code'].values:
        filter_df = cables[cables['code'] == code]
        length = filter_df['length'].values[0]
        cable = Cable(
            code=code,  type=filter_df['description'].values[0], length=length)
        cables_arr.append(cable)

    # for cbl in cables_arr:
    #     print(
    #         f'cable: {cbl.code} start: {cbl.start} end: {cbl.end} type: {cbl.type} len:{cbl.length}')

    # create nodes
    # everything that isn't a cable should become a node
    candidate_nodes = data[data['element_type'] != 'cable']

    nodes = []
    sj = None
    # find the root node
    for node in candidate_nodes['code'].values:
        if node[0] == 'S' and node[1] == 'J':
            sj = Node(code=node)
            nodes.append(sj)

    # find the cables that go to in the sj
    for cable in cables_arr:
        if cable.start == sj.code:
            splice = Splice(cable=cable, fibers=[1, 2])
            sj.next.append(splice.cable.end)
            sj.splices.append(splice)

    print(sj.code)
    print(sj.next)
    print(sj.prev)

    '''
    Encontramos de momento los identificadores de Next de cada SJ y empezamos a hacer la rama

    '''
    head = Node(code=sj.next[1])
    branch = []
    branches = []
    branch.append(head)

    def get_main_cable(node):
        main = None
        # get the root of the cable
        for cbl in cables_arr:
            if cbl.end == node.code:
                main = cbl

        return main

    def is_slitter(main, cable):
        if main.type == cable.type:
            return True

        return False

    # compare types so we can sort the list

    def compare_cbl_type(cbl1, cbl2):
        type1 = int(cbl1.type.split()[0])
        type2 = int(cbl2.type.split()[0])

        if type1 < type2:
            return -1

        if type1 > type2:
            return 1

        if type1 == type2:
            return 0

    def cmp_cable_length(l1, l2): 

        if l1.length < l2.length: 
            return -1

        else: 
            return 1

    def sort_cables(arr):
        for n in range(len(arr)):
            cable = arr[n]
            for i in range(1, len(arr)):
                cmp = compare_cbl_type(cable, arr[i])

                if cmp == -1:
                    arr[n] = arr[i]
                    arr[i] = cable
                if cmp == 0: 
                     cmp2 = cmp_cable_length(cable, arr[i])
                     if cmp2 == -1: 
                        arr[n] = arr[i]
                        arr[i] = cable


    def compute_conections(node):

        main = get_main_cable(node=node)
        # get the rest of conns and sort them by type and later by lenght if size its the same
        cables = [cable for cable in cables_arr if cable.start == node.code]

        if len(cables) == 0:
            return 
     
        sort_cables(arr=cables)

        cmp = compare_cbl_type(cbl1=main, cbl2=cables[0])
        if cmp == 0:
            node.slitter = cables[0]
            node.splices = [
                cable for cable in cables if cable.code != cables[0].code]
        else:

            node.splices = cables

    def find_next(head, branch):

        # find the cables that connect
        for cable in cables_arr:
            if cable.start == head.code:
                new_node = Node(cable.end)
                head.next.append(new_node.code)
                new_node.prev.append(cable.start)
                # compute slitter and splices for head we need the lenght of cable in case type is not an option
                compute_conections(node=head)
                branch.append(new_node)
                find_next(new_node, branch)

    find_next(head=head, branch=branch)

    def print_node(node):
            print(f'Node: {node.code}')
            print(f'Prev: {node.prev}')
            print(f'Next: {node.next}')
            if node.slitter != None: 
                print(f'Slitter: {node.slitter.code}')
            else: 
                print('Slitter: ')
            print(f'Splices: {[splice.code for splice in node.splices]}')

    right_arrow = '\U000027A1'
    down_arrow = '\U00002B07'

    for node in branch:
        print_node(node)
