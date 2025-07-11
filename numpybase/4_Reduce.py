import numpy as np

# TODO 4. NumPy中的“轴”方向
"""
在NumPy的多维数组中，常有“约减”（Reduce，亦有文献译作“规约”）的提法。
它表示将众多数据按照某种规则合并成一个或几个数据。
“约减”之后，数据的个数在总量上是减少的。
"""
array8 = np.ones((2, 3))
print(array8.sum())  # 6.0

"""
知道了“约减”的含义之后，我们可以推而广之，求N维数组的均值（mean）、最大值（max）和最小值（min）等，
这些操作都属于约减操作。但有时，我们会有这样的需求，对指定维度方向的值进行统计，
如统计某一行（或列）的和、均值、最大值、最小值等。这个时候，就需要给“约减”指令指定方向。
那么该如何指定呢？事实上，诸如sum()、min()、max()，mean()等函数，
它们都有一个名为操作轴（axis）的参数，其默认值为None，也就是不指定约减方向，
它将所有数据都“约减”为一个元素。如果axis的值为0，可简单地理解为从垂直方向进行“约减”。
如果axis的值为1，则可以简单理解为从水平方向进行“约减”
"""
print(array8.sum(axis=0))  # 垂直方向约减  [2. 2. 2.]   使用关键字参数axis=0，显式给出了约减轴的方向为垂直方向，
print(array8.sum(1))  # 水平方向约减  [3. 3.]   仅仅给出整数值1，它等同于axis=1，即在水平方向约减。

"""
对于高维数组而言，“约减”也可以有先后顺序。因此，axis的值还可以是一个向量，比如说axis=[1, 0]，
表示先进行水平方向约减，再进行垂直方向约减。反之，axis=[0, 1]表示先进行垂直方向约减，再进行水平方向约减。
如果没有指定方向，那么将采用默认值None，表示所有维度都会被依次“约减”

比如，对于一个三维的数组[[[1, 1, 1], [2, 2, 2]], [[3, 3, 3],[4, 4,4]]]，它有三层括号，其维度由外到内分别为[0,1,2].
当我们指定sum()函数的axis=0时，就是在第0个维度的元素之间进行求和操作，
即拆掉最外层括号后对应的两个元素（[[1, 1, 1], [2, 2, 2]]和[[3, 3, 3], [4, 4,4]]），
然后对同一个括号层次下的两个张量实施逐元素“约减”操作，其结果为[[4, 4, 4], [6, 6, 6]]。
没有被“约减”的维度，其括号层次保持不变。

类似地，当axis=1时，就是在第1个维度的元素之间进行求和操作，
也就是拆掉中间层括号对应的元素[1, 1, 1], [2, 2, 2]和[3, 3, 3], [4, 4, 4]。
需要注意的是，“约减”操作的实施对象为，原来在同一个括号层次内的对象，即[1, 1,1]和[2, 2, 2]相加，[3, 3, 3]和[4, 4, 4]相加。
没有被“约减”的维度，其括号保持不变，结果得到[[3, 3, 3],[7, 7, 7]]。

类似地，当axis=2时，就是拆掉最内层括号，然后对最内层括号元素实施求和操作，
即1+1+1=3，2+2+2=6，3+3+3=9，4+4+4=12。
实施“约减”操作之后，该层括号消失，其他维度的括号保留。结果得到[[3,6], [9,12]]。
"""
"""
其他可实施约减的函数，如max（最大值）、min（最小值）和mean（均值）等，其轴方向的约减也是类似的
"""
array9 = np.linspace(1, 9, 9).reshape(3, 3)
print(array9.max(0), array9.max(1), array9.max())  # [7. 8. 9.] [3. 6. 9.] 9.0
print(array9.mean(0), array9.mean(1), array9.mean())  # [4. 5. 6.] [2. 5. 8.] 5.0
