from numpy import random
#Connection对象,主要职责是记录连接的权重，以及这个链接所关联的上下游节点
class Connection(object):
    def __init__(self, upstream_node, downstream_node):
        '''
            初始化链接，权重初始化是一个很小的随机数
            upstreamnode 链接的上游节点
            downstreamnode 连接的下游节点
            '''
        self.upstream_node=upstream_node
        self.downstream_node=downstream_node
        self.weight=random.uniform(-0.1,0.1)
        #uniform生成随机函数在-0.1到0.1内
        self.gradient=0.0

    def calc_gradient(self):
        '''
        计算梯度
        '''
        self.gradient=self.downstream_node.delta*self.upstream_node.output

    def get_gradient(self):
        '''
        根据梯度下降算法更新权重
        '''
        return self.gradient

    def update_weight(self,rate):
        '''
        根据梯度下降算法更新权重
        '''
        self.calc_gradient()
        self.weight+=rate*self.gradient

    def __str__(self):
        '''
        打印链接信息
        '''
        return '(%u-%u) -> (%u-%u) = %f' % (
            self.upstream_node.layer_index,
            self.upstream_node.node_index,
            self.downstream_node.layer_index,
            self.downstream_node.node_index,
            self.weight)

    #测试
    print("123")



