# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 合并两个有序链表.py
# Time       ：2022/8/1 23:36
# Author     ：Ivan Will
# User       : a1203
# Description：
"""
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
#  示例 2：
#
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
#  提示：
#
#
#  两个链表的节点数目范围是 [0, 50]
#  -100 <= Node.val <= 100
#  l1 和 l2 均按 非递减顺序 排列
#
#
#  Related Topics 递归 链表 👍 2570 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

# leetcode submit region end(Prohibit modification and deletion)
