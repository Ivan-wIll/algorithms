# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 两数之和.py
# Time       ：2022/7/21 1:45
# Author     ：Ivan Will
# User       : a1203
# Description：两数之和
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 循环
class Solution1(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # head:结果链表, point:当前的指针
        head = point = ListNode()
        # 进位
        flag = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            z = x + y + flag
            point.next = ListNode(z % 10)
            flag = z // 10
            # l1，l2的下一位，考虑空链表的情况
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            point = point.next
        if flag: point.next = ListNode(flag)

        return head.next


# 递归解法
class Solution2(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        z = ListNode((x + y) % 10)
        flag = (x + y) // 10
        z.next = self.addTwoNumbers(l1.next, l2.next)
        if flag:
            z.next = self.addTwoNumbers(z.next, ListNode(flag))

        return z
