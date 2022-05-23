from dis import dis
from tracemalloc import start
import pandas as pd 
import numpy as np
from cable import Cable
from link import FiberLink, LinkType

from node import Node 


#read the data
data = pd.read_csv('data.csv')
cable_data = pd.read_csv('cables.csv')


distribution_points_data = data.where(data['element_type'] == 'distributionpoint').dropna()
spliceboxes_data = data.where(data['element_type'] == 'splicebox').dropna()

splitter_boxes = []


#splitter boxes
sbs = np.array(distribution_points_data['id_element'])
sbs_codes = np.array(distribution_points_data['code'])

joints = np.array(spliceboxes_data['id_element'])
joints_codes = np.array(spliceboxes_data['code'])


cables = []
for cbl in np.array(cable_data['code']): 
    id = cable_data['id_colorpattern'].where(cable_data['code'] == cbl).dropna().values[0]
    size = cable_data['description'].where(cable_data['code'] == cbl).dropna().values[0]
    len = cable_data['length'].where(cable_data['code'] == cbl).dropna().values[0]
    cables.append(
        Cable(code=cbl, id=id,size=size, len=len))

    

nodes = []
#search for the data 
for jnt in joints_codes: 

    outgoing = [cbl for cbl in cables if cbl.start == jnt ]
    incoming = [cbl for cbl in cables if cbl.end == jnt]


    if len(outgoing) == 0: 
        outgoing.append(None)
    if len(incoming) == 0: 
        incoming.append(None)

    node = Node(id=jnt)

    for x in incoming: 
        for y in outgoing: 
            link = FiberLink(incoming=x, node=node, outgoing=y)
            print(f'link type:{link.link_type} in: {x.code if x != None else None } out: {y.code if y != None else None}')
            node.add_link(link)
            nodes.append(node)
