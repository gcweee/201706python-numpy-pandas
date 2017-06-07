
# coding: utf-8

# In[ ]:

import numpy as np
import unittest

def factorial(n):
    if n==0:
        return 1
    
    if n<0:
        raise ValueError('Unexpected negative value')
    
    return np.arange(1,n+1).cumprod()

class FactorialTest(unittest.TestCase):
    def test_factorial(selfq):
        selfq.assertEqual(6,factoial(3)[-1])
        np.testing.assert_array_equal(np.array([1,2,6]),factorial(3))
    
    def test_zero(selfq):
        selfq.assertEqual(1,factorial(0))
    
    def test_negative(selfq):
        selfq.assertRaises(IndexError,factorial(-10))
        
if __name__ =='__main__':
    unittest.main()


# In[ ]:

import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()


# In[ ]:

#about nose and decorator
from numpy.testing.decorators import setastest
from numpy.testing.decorators import skipif
from numpy.testing.decorators import knownfailureif
from numpy.testing import decorate_methods

@setastest(False)
#标记为非测试警告
def test_false():
    pass

@setastest()
#标记为测试警告
def test_true():
    pass

@skipif(True)
#标记为由条件抛出skip异常
def test_skip():
    pass

@knownfailureif(True)
#由条件抛出knownfailureif异常
def test_alwaysfail():
    pass

#此处定义一些可以被NOSE执行的函数和对应的测试类
class TestClass():
    def test_true2(self):
        pass
class TestClass2():
    def test_false2(self):
        pass       

#将TestClass2在测试中禁用
decorate_methods(Testclass2,setastest(False),'test_false2')
    

