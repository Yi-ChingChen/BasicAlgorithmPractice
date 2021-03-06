# _*_coding:utf-8_*_
'''
剑指offer 10_2  
题目：
  青蛙跳台阶问题

  一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶，求该青蛙跳上一个n级的台阶总共有多少种跳法。
  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
  输入：n = 2
  输出：2
  
示例 2：
  输入：n = 7
  输出：21
  
示例 3：
  输入：n = 0
  输出：1
  
提示：

0 <= n <= 100
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        通过看网友的解法，我发现了一些规律
        那就是类似于斐波那契数列的了，
        因为从大佬列举的结果中发现规律：
        结果：    1,2,3,5,8,13,21
        下标：    1,2,3,4,5,6, 7
        所以：Xn+1 = Xn + Xn-1
        果然，高手在评论席
        :param n:
        :return:
        '''
        pass


def climbStairs1(n):
    '''
    斐波那契数列固然可以解决问题，但是我们下面这种是最常规的斐波那契数列
    也就是使用递归方法解决，但是递归会设计大量的重复计算
    所以需要改进。。。
    :param n:
    :return:
    '''
    if 0<=n<=100:
      f1, f2 = 1, 2
      while n > 1:
          f1, f2 = f2, f1 + f2
          n -= 1
      return f1%1000000007


def climbStairs2(n):
    '''
    改进递归
    为了避免重复计算，因此每次跳台阶的方法数，要是我们记下来就可以了
    这样就不会重复计算了，用一个数组dp就可以解决
    dp[n] = dp[n-1] + dp[n-2]
    这样的时间复杂度为O(n)，空间复杂度为O(n)
    :param n:
    :return:
    '''
    if n<=0<=100:
      if n == 0:
        return 1
      if n <= 2:
          return n
      dp = [0] * n
      dp[0], dp[1] = 1, 2
      for i in range(3, n+1):
          dp[i] = dp[i - 1] + dp[i - 2]
      return dp[n]%1000000007


def climbStairs(n):
    '''
    实际上，我们还可以对上面方法进行改进
    就是不必将所有的记录都记起来，假设我们有三层楼梯
    也只需要知道跳2阶和1阶的方法数是多少就可以算出3阶了
    这样每次就只需要保留 n-1阶 和 n-2 阶的方法数
    :param n:
    :return:
    '''
    if 0<=n<=100:
      if n == 0:
        return 1
      if n <= 2:
          return n
      a, b = 1, 2
      for i in range(3, n + 1):
          a, b = b, a + b
      return b%1000000007


res = climbStairs(5)
print(res)

'''

'''
