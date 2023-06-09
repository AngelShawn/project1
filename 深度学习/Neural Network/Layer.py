#负责初始化一层，并作为Node的对象，对Node提供集合的操作
from Node import Node
from ConstNode import ConstNode

class Layer(object):
    '''
    初始化某一层
    layer_index: 层编号
    node_count: 层当中所包含的节点个数
    '''
    def __init__(self,layer_index,node_count):
       self.layer_index=layer_index
       self.nodes=[]
       for i in range(node_count):
          self.nodes.append(Node(layer_index,i))
       self.nodes.append(ConstNode(layer_index,node_count))

    def set_output(self,data):
        '''
        设置层的输出，当处于输入层的时候会用到
        '''
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])

    def calc_output(self):
        '''
        计算层的输出向量
        '''
        for node in self.nodes[:-1]:
            node.calc_output()

    def dump(self):
        '''
        打印层的信息
        '''
        for node in self.nodes:
            print(node)


