"""两数相加"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # 数据结构
        if l1 is None: return l2
        if l2 is None: return l1  # 判断是否有空链表
        head = point = ListNode()  # 创建节点0，head一直指向头节点用于最后返回值，point用于添加新节点
        flag = 0  # 进位标记，默认为0
        while l1 and l2:  # 都不为空时
            new = (l1.val + l2.val + flag) % 10  # 新建节点的值
            flag = (l1.val + l2.val + flag) // 10  # 进位标记
            point.next = ListNode(new)  # 创建节点
            point = point.next  # 指针后移
            if l1.next and l2.next:  # 下一个都不为空，都后移
                l1 = l1.next
                l2 = l2.next
            elif l2.next and (l1.next is None):  # 有空的就令其为0
                l1.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
            elif l1.next and (l2.next is None):
                l2.next = ListNode(0)
                l2 = l2.next
                l1 = l1.next
            else:  # 都为空了则退出
                break
        if flag == 1: point.next = ListNode(1)
        return head.next
