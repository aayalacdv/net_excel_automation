''''
honestly do i want this thing to be this smart???? nah at first 
adjacency matrix is the first choice[]
struct node
{
    code: 
    slitter: cable 
    splice:[struct {cable, fiber}]
}

cable
size
lenght 
code

splitter
code
ports 


Los links de las SJs se hacen con splitters por eso lo dejamos como splitter
link type:LinkType.SPLITTER in: None out: BAM-CL008-SJ14111-SB42113
link type:LinkType.SPLITTER in: None out: BAM-CL008-SJ14111-J14119
link type:LinkType.SPLITTER in: None out: BAM-CL008-SJ14111-SB42110

Hay que particularizar para la longitud del cable porque de momento solo clasifica en función del número de fibras  
En el 90 % de los casos parece acertar, por eso tenemos que incluir un if extra comprobando si ya tenemos otro enlace en el cable
link type:LinkType.SLITTER in: BAM-CL008-SB42113-J14114 out: BAM-CL008-J14114-SB42123
link type:LinkType.SLITTER in: BAM-CL008-SB42113-J14114 out: BAM-CL008-J14114-SB42121

link type:LinkType.SLITTER in: BAM-CL008-SJ14111-J14119 out: BAM-CL008-J14119-J14118
link type:LinkType.SPLICE in: BAM-CL008-SJ14111-J14119 out: BAM-CL008-J14119-SB42129
link type:LinkType.SLITTER in: BAM-CL008-J14119-J14118 out: BAM-CL008-J14118-J14121
link type:LinkType.SPLICE in: BAM-CL008-J14119-J14118 out: BAM-CL008-J14118-SB42125
link type:LinkType.SPLICE in: BAM-CL008-J14118-J14121 out: BAM-CL008-J14121-SB42132

'''