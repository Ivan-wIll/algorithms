# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : LRU缓存.py
# Time       ：2022/7/23 22:14
# Author     ：Ivan Will
# User       : a1203
# Description：
#
#  请你设计并实现一个满足
#  LRU (最近最少使用) 缓存 约束的数据结构。
#
#
#
#  实现
#  LRUCache 类：
#
#
#
#
#
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
#
#
#
#
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
#  示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
#  提示：
#
#
#  1 <= capacity <= 3000
#  0 <= key <= 10000
#  0 <= value <= 10⁵
#  最多调用 2 * 10⁵ 次 get 和 put
#
#
#  Related Topics 设计 哈希表 链表 双向链表 👍 2288 👎 0

"""

# 方法1：暴力解答，不满足时间复杂度O(1)。。。
from collections import OrderedDict


class LRUCache0:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if self.cache.get(key) is not None:
            self.record(key)
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache.update({key: value})
        self.record(key)
        if len(self.queue) > self.capacity:
            self.cache.pop(self.queue[0])
            self.queue.pop(0)
        return None

    def record(self, key: int) -> None:
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)
        return None


# debug:
# c = LRUCache0(2)
# print(c.put(1, 1), c.cache, c.queue)
# print(c.put(2, 2), c.cache, c.queue)
# print(c.get(1), c.cache, c.queue)
# print(c.put(3, 3), c.cache, c.queue)


# 方法二：双向链表    python中结合哈希表和双链表的一种数据结构：OrderedDict()
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache1:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# 。。。
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    """双链表"""

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: ListNode) -> ListNode:
        """在头节点之后插入"""
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        return node

    def remove(self, node: ListNode) -> ListNode:
        """删除node节点"""
        node.next.prev, node.prev.next = node.prev, node.next
        return node


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d_list = DoubleLinkedList()
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            node = self.hashmap[key]
            self.d_list.remove(node)
            self.d_list.add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if key in self.hashmap:
            node = self.hashmap[key]
            node = self.d_list.remove(node)
            node.value = value
        self.hashmap[key] = self.d_list.add_to_head(node)
        if len(self.hashmap) > self.capacity:
            self.hashmap.pop(self.d_list.tail.prev.key)
            self.d_list.remove(self.d_list.tail.prev)


c = LRUCache2(2)
print(c.put(1, 1))
print(c.put(2, 2))
print(c.get(1))
print(c.put(3, 3))
print(c.put(3, 3))
