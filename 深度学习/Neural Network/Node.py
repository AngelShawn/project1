# 节点对象计算和记录节点自身的信息(比如输出值、误差项等)，以及与这个节点相关的上下游的连接。实现输出值和误差项的计算
class Node(object):
    def __int__(self,layer_index,node_index):
        '''
        构造结点对象
        layer_index：节点所属的层的编号
        node_index： 节点的编号
        '''
        self.layer_index=layer_index
        self.node_index=node_index
        self.downstream=[]
        self.upstream=[]
        self.output=0
        self.delta=0

    def set_output(self,output):
        '''
        设置节点的输出值。如果节点属于输入层会遇到这个函数
        '''
        self.output=output

    def append_downstream_connection(self,conn):
        '''
        添加一个到下游节点的链接
        '''
        self.downstream.append(conn)

    def append_upstream_connection(self,conn):
        '''
        添加一个到上游节点的链接
        '''
        self.upstream.append(conn)
    def calc_output(self):
        '''
        根据式子1计算节点的输出比如拿节点4举例子。就是要用上流w41*x1+w42*x2+w43*x3+w4b（节点4的偏置项）ret是偏置项
        '''
        output=reduce(lambda ret,conn:ret+conn.upstream_node.output*conn.weight,self.upstream,0)
        self.output=sigmoid(output)

    def calc_hidden_layer_delta(self):
        '''
        节点位于隐藏层，用公式4计算delta
        '''
        downstream_delta=reduce(lambda ret,conn:ret+conn.downstream_node.delta*conn.weight,self.downstream,0.0)
        self.delta=self.output*(1-self.output)*downstream_delta

    def calc_output_layer_delta(self,label):
        '''
        节点属于输出层时，根据公式3计算delta
        '''
        self.delta=self.output*(1-self.output)*(label-self.output)

    def __str__(self):
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.output, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + '\n\tupstream:' + upstream_str

    #测试
    print("123")









